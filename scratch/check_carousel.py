import re

def check_carousel():
    with open("index.html", encoding="utf-8") as f:
        html = f.read()

    # Find all card-item-3d
    cards = re.findall(r'<div class="card-item-3d".*?</div>\s*</div>\s*</div>', html, re.DOTALL)
    print(f"Number of 3D cards: {len(cards)}")
    for i, card in enumerate(cards):
        print(f"Card {i}: {card[:250].strip()}...")

if __name__ == "__main__":
    check_carousel()
