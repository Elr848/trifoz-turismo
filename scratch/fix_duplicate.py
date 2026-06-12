def fix_duplicated_script():
    """Remove the second duplicate <script> block from index.html"""
    with open("index.html", encoding="utf-8") as f:
        content = f.read()

    # The pattern is:
    # First block ends at:  </script>  (line 3235)
    # Then immediately follows a duplicate:
    #   <script src="Draggable.min.js"></script>
    #   <script>... duplicate DOMContentLoaded ...</script>
    # We want to remove from the duplicate Draggable.min.js line through the closing </script> of the second block

    # Strategy: find second occurrence of the Draggable script src
    draggable_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Draggable.min.js"></script>'
    first_idx = content.find(draggable_tag)
    second_idx = content.find(draggable_tag, first_idx + 1)

    if second_idx == -1:
        print("ERROR: Could not find duplicate Draggable.min.js import! Aborting.")
        return

    print(f"First Draggable import at char position: {first_idx}")
    print(f"Second Draggable import (DUPLICATE) at char position: {second_idx}")

    # Find the end of the second <script>...</script> block that follows second_idx
    # The second block starts with the second draggable import and ends with:
    #     </script> (which is the end of the DOMContentLoaded block)
    # We need to find the very last </script> before the <!-- Lightbox Modal --> comment

    lightbox_comment = '<!-- Lightbox Modal -->'
    lightbox_idx = content.find(lightbox_comment)

    if lightbox_idx == -1:
        print("ERROR: Could not find Lightbox Modal comment!")
        return

    print(f"Lightbox Modal comment found at char position: {lightbox_idx}")

    # The </script> closing the second JS block is right before the lightbox comment
    closing_script = '</script>'
    # Find the last </script> before the lightbox comment
    search_region = content[second_idx:lightbox_idx]
    last_close_in_region = search_region.rfind(closing_script)

    if last_close_in_region == -1:
        print("ERROR: Could not find closing </script> of duplicate block!")
        return

    # The absolute positions of what to remove
    remove_start = second_idx
    remove_end = second_idx + last_close_in_region + len(closing_script)

    print(f"Will remove chars {remove_start} to {remove_end}")
    print(f"Preview of removed content start: {content[remove_start:remove_start+120]!r}")
    print(f"Preview of removed content end: {content[remove_end-80:remove_end]!r}")

    # Verify before and after are sensible
    before_chunk = content[remove_start - 50: remove_start]
    after_chunk = content[remove_end: remove_end + 100]
    print(f"\nBEFORE the removal point: ...{before_chunk!r}")
    print(f"AFTER the removal point: {after_chunk!r}...")

    # Perform the removal
    new_content = content[:remove_start] + content[remove_end:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSUCCESS! Removed {remove_end - remove_start} characters of duplicate script.")
    print(f"New total length: {len(new_content)} chars (was {len(content)} chars)")


if __name__ == "__main__":
    fix_duplicated_script()
