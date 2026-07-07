"""Add destinations to trifoz-i18n using exec on JS-like array (trusted local source)."""
import json
import os
import re
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = ["index.html", "index-pt.html", "index-en.html"]


def extract_destinations(fn: str) -> list:
    result = subprocess.run(
        ["git", "show", f"HEAD:{fn}"],
        capture_output=True,
        cwd=BASE,
    )
    text = result.stdout.decode("utf-8", errors="replace")
    match = re.search(r"const destinations = (\[[\s\S]*?\]);", text)
    if not match:
        raise ValueError(f"No destinations in {fn}")
    js = match.group(1)
    js = re.sub(r"(\w+)\s*:", r'"\1":', js)
    js = js.replace("'", '"')
    return json.loads(js)


for fn in FILES:
    path = os.path.join(BASE, fn)
    with open(path, encoding="utf-8") as f:
        html = f.read()

    block = re.search(
        r'<script type="application/json" id="trifoz-i18n">(.*?)</script>',
        html,
        re.S,
    )
    if not block:
        continue

    data = json.loads(block.group(1))
    if data.get("destinations"):
        print(f"{fn}: ok")
        continue

    data["destinations"] = extract_destinations(fn)
    replacement = (
        '<script type="application/json" id="trifoz-i18n">'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "</script>"
    )
    html = html.replace(block.group(0), replacement)

    pair = (
        '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n'
        '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Draggable.min.js"></script>\n'
    )
    while html.count(pair) > 1:
        html = html.replace(pair, "", 1)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"{fn}: fixed ({len(data['destinations'])} items)")
