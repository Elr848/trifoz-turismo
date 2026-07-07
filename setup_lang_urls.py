"""Generate pt/index.html and en/index.html with corrected relative asset paths."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))


def fix_paths(content: str, subdir: str) -> str:
    prefix = "../"

    for attr in ("href", "src"):
        content = re.sub(
            rf'({attr}=")(?!https?:|#|mailto:|tel:|\.\./|/)(images/)',
            rf"\1{prefix}\2",
            content,
        )
        content = re.sub(
            rf'({attr}=")(?!https?:|#|mailto:|tel:|\.\./|/)(favicon)',
            rf"\1{prefix}\2",
            content,
        )

    content = content.replace("url('images/", "url('../images/")
    content = content.replace('url("images/', 'url("../images/')
    content = content.replace('href="index.html"', 'href="../"')
    content = content.replace('href="index-pt.html"', 'href="/pt/"')
    content = content.replace('href="index-en.html"', 'href="/en/"')

    if subdir == "pt":
        content = content.replace(
            "https://trifoz-turismo.com/index-pt.html",
            "https://trifoz-turismo.com/pt/",
        )
        content = content.replace(
            'content="https://trifoz-turismo.com/index-pt.html"',
            'content="https://trifoz-turismo.com/pt/"',
        )
    else:
        content = content.replace(
            "https://trifoz-turismo.com/index-en.html",
            "https://trifoz-turismo.com/en/",
        )
        content = content.replace(
            'content="https://trifoz-turismo.com/index-en.html"',
            'content="https://trifoz-turismo.com/en/"',
        )
        content = content.replace(
            'hreflang="en" href="https://trifoz-turismo.com/index-en.html"',
            'hreflang="en" href="https://trifoz-turismo.com/en/"',
        )

    return content


REDIRECT_PT = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="https://trifoz-turismo.com/pt/">
    <meta http-equiv="refresh" content="0; url=/pt/">
    <title>Redirecionando…</title>
    <script>location.replace("/pt/");</script>
</head>
<body><p><a href="/pt/">Trifoz Turismo (PT)</a></p></body>
</html>
"""

REDIRECT_EN = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="https://trifoz-turismo.com/en/">
    <meta http-equiv="refresh" content="0; url=/en/">
    <title>Redirecting…</title>
    <script>location.replace("/en/");</script>
</head>
<body><p><a href="/en/">Trifoz Turismo (EN)</a></p></body>
</html>
"""


def main():
    for sub, src in [("pt", "index-pt.html"), ("en", "index-en.html")]:
        os.makedirs(os.path.join(BASE, sub), exist_ok=True)
        with open(os.path.join(BASE, src), encoding="utf-8") as f:
            content = fix_paths(f.read(), sub)
        out = os.path.join(BASE, sub, "index.html")
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Created {out} ({len(content) // 1024} KB)")

    with open(os.path.join(BASE, "index-pt.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(REDIRECT_PT)
    with open(os.path.join(BASE, "index-en.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(REDIRECT_EN)
    print("Created redirect stubs for legacy URLs")


if __name__ == "__main__":
    main()
