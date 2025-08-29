
import os
import re

# Get all HTML files in the current directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

def add_favicon(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if favicon is already present
        if 'favicon-32x32.png' in content:
            print(f"- Favicon already exists in {filename}")
            return False
            
        # Pattern to match the title tag and add favicon after it
        title_pattern = r'(<title>.*?</title>)'
        favicon_line = '\n    <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png">'
        
        if re.search(title_pattern, content, re.DOTALL):
            updated_content = re.sub(title_pattern, r'\1' + favicon_line, content, flags=re.DOTALL)
            
            if updated_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✓ Added favicon to {filename}")
                return True
        else:
            print(f"- No title tag found in {filename}")
        
        return False
        
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")
        return False

def main():
    print("Adding favicon to all HTML files...")
    updated_count = 0
    
    # Skip index.html since we already updated it manually
    files_to_update = [f for f in html_files if f != 'index.html']
    
    for filename in files_to_update:
        if add_favicon(filename):
            updated_count += 1
    
    print(f"\nCompleted: Added favicon to {updated_count} files.")

if __name__ == "__main__":
    main()
