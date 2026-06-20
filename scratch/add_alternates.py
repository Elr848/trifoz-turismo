def main():
    for filename in ['index.html', 'index-pt.html', 'index-en.html']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        old_block = '<link rel="alternate" hreflang="x-default" href="https://trifoz-turismo.com/" />'
        new_block = '<link rel="alternate" hreflang="en" href="https://trifoz-turismo.com/index-en.html" />\n    <link rel="alternate" hreflang="x-default" href="https://trifoz-turismo.com/" />'
        
        if old_block in content:
            content = content.replace(old_block, new_block)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Added alternate to {filename}')
        else:
            print(f'Warning: alternate block not found in {filename}')

if __name__ == '__main__':
    main()
