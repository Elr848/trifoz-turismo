def find_cards():
    with open("index.html", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if "card-item-3d" in line:
            print(f"Line {i+1}: {line.strip()}")
            # print next 5 lines
            for j in range(1, 6):
                if i+j < len(lines):
                    print(f"  + {lines[i+j].strip()}")

if __name__ == "__main__":
    find_cards()
