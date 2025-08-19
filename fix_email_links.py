
import os
import glob

def update_email_in_file(filepath):
    """Update mailto links to Gmail links in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple string replacement for mailto links
        old_link = 'href="mailto:nyusportsfilmfestival@nyu.edu"'
        new_link = 'href="https://mail.google.com/mail/?view=cm&fs=1&to=nyusportsfilmfestival@nyu.edu" target="_blank"'
        
        if old_link in content:
            updated_content = content.replace(old_link, new_link)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✓ Updated {filepath}")
            return True
        else:
            print(f"- No email links to update in {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ Error updating {filepath}: {e}")
        return False

def main():
    # Find all HTML files
    html_files = glob.glob("*.html")
    
    updated_count = 0
    print("Checking HTML files for email links to update...")
    
    for filepath in html_files:
        if update_email_in_file(filepath):
            updated_count += 1
    
    print(f"\nCompleted: Updated {updated_count} files with Gmail email links.")

if __name__ == "__main__":
    main()
