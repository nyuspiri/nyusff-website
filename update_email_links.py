
import os
import re

# Files that need email link updates
html_files = [
    'people.html',
    'submission.html',
    'festival-2022.html',
    'festival-2023.html', 
    'festival-2024.html',
    'festival-2025.html',
    'honoree-2022.html',
    'honoree-2023.html',
    'honoree-2024.html', 
    'honoree-2025.html',
    'mentions-2022.html',
    'mentions-2023.html',
    'mentions-2024.html',
    'mentions-2025.html',
    'program-2022.html',
    'program-2023.html',
    'program-2024.html',
    'program-2025.html',
    'schedule-2022.html',
    'schedule-2023.html',
    'schedule-2024.html',
    'schedule-2025.html',
    'selections-2022.html',
    'selections-2023.html',
    'selections-2024.html',
    'selections-2025.html',
    'speakers-2022.html',
    'speakers-2023.html',
    'speakers-2024.html',
    'speakers-2025.html'
]

def update_email_links(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find mailto email links in footer
        mailto_pattern = r'<a href="mailto:nyusportsfilmfestival@nyu\.edu"([^>]*)>Email</a>'
        gmail_replacement = r'<a href="https://mail.google.com/mail/?view=cm&fs=1&to=nyusportsfilmfestival@nyu.edu" target="_blank"\1>Email</a>'
        
        # Replace the mailto links with Gmail links
        updated_content = re.sub(mailto_pattern, gmail_replacement, content)
        
        # Check if any changes were made
        if updated_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated email links in {filename}")
            return True
        else:
            print(f"No email links found to update in {filename}")
            return False
            
    except Exception as e:
        print(f"Error updating {filename}: {e}")
        return False

def main():
    updated_count = 0
    for filename in html_files:
        if update_email_links(filename):
            updated_count += 1
    
    print(f"\nUpdated email links in {updated_count} files successfully.")

if __name__ == "__main__":
    main()
