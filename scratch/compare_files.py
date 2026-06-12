def compare():
    with open("index.html", "r", encoding="utf-8") as f:
        html_es = f.read()
    with open("index-pt.html", "r", encoding="utf-8") as f:
        html_pt = f.read()

    # Find where <section class="attractions"> starts in both
    pos_es = html_es.find('<section class="attractions">')
    pos_pt = html_pt.find('<section class="attractions">')

    print(f"ES position: {pos_es}")
    print(f"PT position: {pos_pt}")

    # Check if index-pt.html contains data-src in card-item-3d
    data_src_count_es = html_es.count('data-src=')
    data_src_count_pt = html_pt.count('data-src=')
    print(f"data-src count - ES: {data_src_count_es}, PT: {data_src_count_pt}")

if __name__ == "__main__":
    compare()
