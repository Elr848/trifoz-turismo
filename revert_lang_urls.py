"""Revert URL structure: restore index-pt.html / index-en.html, remove pt/ and en/."""
import os
import re
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))


def restore_root_paths(content: str, lang: str) -> str:
    content = content.replace("../images/", "images/")
    content = content.replace("url('../images/", "url('images/")
    content = content.replace('url("../images/', 'url("images/')
    content = content.replace('href="../favicon', 'href="favicon')
    content = content.replace('href="../"', 'href="index.html"')

    content = content.replace('href="/pt/"', 'href="index-pt.html"')
    content = content.replace('href="/en/"', 'href="index-en.html"')

    if lang == "pt":
        content = content.replace(
            'content="https://trifoz-turismo.com/pt/"',
            'content="https://trifoz-turismo.com/index-pt.html"',
        )
        content = content.replace(
            '"url": "https://trifoz-turismo.com/pt/"',
            '"url": "https://trifoz-turismo.com/index-pt.html"',
        )
    else:
        content = content.replace(
            'hreflang="en" href="https://trifoz-turismo.com/en/"',
            'hreflang="en" href="https://trifoz-turismo.com/index-en.html"',
        )
        content = content.replace(
            'content="https://trifoz-turismo.com/en/"',
            'content="https://trifoz-turismo.com/index-en.html"',
        )
        content = content.replace(
            '"url": "https://trifoz-turismo.com/en/"',
            '"url": "https://trifoz-turismo.com/index-en.html"',
        )

    return content


def main():
    for lang, src_dir, dest in [
        ("pt", os.path.join(BASE, "pt", "index.html"), os.path.join(BASE, "index-pt.html")),
        ("en", os.path.join(BASE, "en", "index.html"), os.path.join(BASE, "index-en.html")),
    ]:
        with open(src_dir, encoding="utf-8") as f:
            content = restore_root_paths(f.read(), lang)
        with open(dest, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Restored {dest}")

    for folder in ("pt", "en"):
        path = os.path.join(BASE, folder)
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Removed {path}/")


if __name__ == "__main__":
    main()
