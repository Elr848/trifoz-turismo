import re

def clean_html(content):
    # Remove script contents to compare HTML structure
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    # Remove styles
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    # Remove whitespace
    content = re.sub(r'\s+', ' ', content)
    return content

with open('index.html', 'r', encoding='utf-8') as f:
    es = f.read()

with open('index-pt.html', 'r', encoding='utf-8') as f:
    pt = f.read()

print(f"index.html length: {len(es)}")
print(f"index-pt.html length: {len(pt)}")

# Let's count some key elements
for tag in ['section', 'div', 'img', 'script', 'a', 'span', 'p', 'h1', 'h2', 'h3', 'h4']:
    es_count = len(re.findall(f'<{tag}\\b', es))
    pt_count = len(re.findall(f'<{tag}\\b', pt))
    print(f"{tag}: ES={es_count}, PT={pt_count}")
