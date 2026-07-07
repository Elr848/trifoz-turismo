"""Apply performance and SEO fixes to main HTML pages."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
PAGES = [
    os.path.join(BASE, "index.html"),
    os.path.join(BASE, "pt", "index.html"),
    os.path.join(BASE, "en", "index.html"),
]

OLD_FONTS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style"
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Oswald:wght@500;700&family=Open+Sans:wght@300;400;600;700&display=swap">
    <link
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Oswald:wght@500;700&family=Open+Sans:wght@300;400;600;700&display=swap"
        rel="stylesheet">"""

NEW_FONTS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
    <link rel="preload" as="style"
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Oswald:wght@700&family=Open+Sans:wght@400;700&display=swap">
    <link
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Oswald:wght@700&family=Open+Sans:wght@400;700&display=swap"
        rel="stylesheet">"""

OLD_FA_BLOCK = """    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
        crossorigin="anonymous" referrerpolicy="no-referrer">"""

NEW_FA_BLOCK = """    <link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" as="style"
        integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
        crossorigin="anonymous" referrerpolicy="no-referrer">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
        crossorigin="anonymous" referrerpolicy="no-referrer" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></noscript>"""

AGGREGATE_RATING = re.compile(
    r',\s*"aggregateRating":\s*\{\s*'
    r'"@type":\s*"AggregateRating",\s*'
    r'"ratingValue":\s*"5",\s*'
    r'"bestRating":\s*"5",\s*'
    r'"ratingCount":\s*"47",\s*'
    r'"reviewCount":\s*"47"\s*'
    r'\}',
    re.MULTILINE,
)


def optimize(path: str) -> list[str]:
    changes = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if OLD_FONTS in content:
        content = content.replace(OLD_FONTS, NEW_FONTS)
        changes.append("fonts")

    # PT may already have async FA with different formatting
    if OLD_FA_BLOCK in content:
        content = content.replace(OLD_FA_BLOCK, NEW_FA_BLOCK)
        changes.append("fontawesome")

    content, n = AGGREGATE_RATING.subn("", content)
    if n:
        changes.append("aggregateRating")

    content = content.replace(
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>',
        '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>',
    )
    content = content.replace(
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Draggable.min.js"></script>',
        '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Draggable.min.js"></script>',
    )

    content = content.replace(
        "window.open(url, '_blank');",
        "window.open(url, '_blank', 'noopener,noreferrer');",
    )

    # Fix YouTube links missing noopener
    content = re.sub(
        r'(href="https://youtu\.be/[^"]+" target="_blank")\s*\n\s*(class="btn-video-elegant")',
        r'\1 rel="noopener noreferrer" \2',
        content,
    )

    if path.endswith(os.path.join(BASE, "index.html")):
        content = content.replace('href="index-pt.html"', 'href="/pt/"')
        content = content.replace('href="index-en.html"', 'href="/en/"')
        content = content.replace('href="index.html"', 'href="/"')
        changes.append("lang-links")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return changes


def main():
    for page in PAGES:
        if os.path.exists(page):
            changes = optimize(page)
            print(f"{page}: {', '.join(changes) or 'no changes'}")


if __name__ == "__main__":
    main()
