from html.parser import HTMLParser
import sys

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags_stack = []
        self.errors = []
        self.self_closing = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }

    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.tags_stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.self_closing:
            return
        if not self.tags_stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
        
        expected_tag, pos = self.tags_stack.pop()
        if expected_tag != tag:
            self.errors.append(
                f"Mismatched end tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}. "
                f"Expected </{expected_tag}> (opened at line {pos[0]}, col {pos[1]})"
            )
            # Put back expected tag to recover
            self.tags_stack.append((expected_tag, pos))

def validate_file(filepath):
    print(f"Validating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    parser = HTMLValidator()
    parser.feed(html)
    
    if parser.tags_stack:
        for tag, pos in reversed(parser.tags_stack):
            parser.errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}, col {pos[1]}")
            
    if parser.errors:
        print(f"FOUND {len(parser.errors)} ERRORS:")
        for err in parser.errors[:20]:
            print(f"  {err}")
    else:
        print("No tag mismatches found!")

if __name__ == '__main__':
    validate_file('index.html')
    validate_file('index-pt.html')
