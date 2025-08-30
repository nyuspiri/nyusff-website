
#!/usr/bin/env python3
import os
import re

# List of HTML files to update
html_files = [
    'contact.html', 'people.html', 'sponsorship.html', 'submission.html',
    'festival-2022.html', 'festival-2023.html', 'festival-2024.html', 'festival-2025.html', 'festival-2026.html',
    'honoree-2022.html', 'honoree-2023.html', 'honoree-2024.html', 'honoree-2025.html', 'honoree-2026.html',
    'mentions-2022.html', 'mentions-2023.html', 'mentions-2024.html', 'mentions-2025.html', 'mentions-2026.html',
    'program-2022.html', 'program-2023.html', 'program-2024.html', 'program-2025.html', 'program-2026.html',
    'schedule-2022.html', 'schedule-2023.html', 'schedule-2024.html', 'schedule-2025.html', 'schedule-2026.html',
    'selections-2022.html', 'selections-2023.html', 'selections-2024.html', 'selections-2025.html', 'selections-2026.html',
    'speakers-2022.html', 'speakers-2023.html', 'speakers-2024.html', 'speakers-2025.html', 'speakers-2026.html'
]

def fix_navigation_in_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix 2025 links
        content = re.sub(r'<a href="https://wp\.nyu\.edu/sff/2025-program/" target="_blank">Program</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-program/" target="_blank">Program</a>', content)
        content = re.sub(r'<a href="program-2025\.html">Program</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-program/" target="_blank">Program</a>', content)
        content = re.sub(r'<a href="schedule-2025\.html">Event Schedule</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-event-schedule/" target="_blank">Event Schedule</a>', content)
        content = re.sub(r'<a href="selections-2025\.html">Official Selections</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-official-selections/" target="_blank">Official Selections</a>', content)
        content = re.sub(r'<a href="mentions-2025\.html">Honorable Mentions</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-honorable-mentions/" target="_blank">Honorable Mentions</a>', content)
        content = re.sub(r'<a href="speakers-2025\.html">Speakers</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-speakers/" target="_blank">Speakers</a>', content)
        content = re.sub(r'<a href="honoree-2025\.html">Honoree</a>', 
                        '<a href="https://wp.nyu.edu/sff/2025-honoree/" target="_blank">Honoree</a>', content)
        
        # Fix 2024 links
        content = re.sub(r'<a href="program-2024\.html">Program</a>', 
                        '<a href="https://wp.nyu.edu/sff/2024-program/" target="_blank">Program</a>', content)
        content = re.sub(r'<a href="schedule-2024\.html">Event Schedule</a>', 
                        '<a href="https://wp.nyu.edu/sff/2024-event-schedule/" target="_blank">Event Schedule</a>', content)
        content = re.sub(r'<a href="selections-2024\.html">Official Selections</a>', 
                        '<a href="https://wp.nyu.edu/sff/2024-official-selections/" target="_blank">Official Selections</a>', content)
        content = re.sub(r'<a href="mentions-2024\.html">Honorable Mentions</a>', 
                        '<a href="https://wp.nyu.edu/sff/2024-honorable-mentions/" target="_blank">Honorable Mentions</a>', content)
        content = re.sub(r'<a href="speakers-2024\.html">Speakers</a>', 
                        '<a href="https://wp.nyu.edu/sff/2024-speakers/" target="_blank">Speakers</a>', content)
        content = re.sub(r'<a href="honoree-2024\.html">Honoree</a>', 
                        '<a href="https://wp.nyu.edu/sff/2024-honoree/" target="_blank">Honoree</a>', content)
        
        # Fix 2023 links
        content = re.sub(r'<a href="program-2023\.html">Program</a>', 
                        '<a href="https://wp.nyu.edu/sff/2023-program/" target="_blank">Program</a>', content)
        content = re.sub(r'<a href="schedule-2023\.html">Event Schedule</a>', 
                        '<a href="https://wp.nyu.edu/sff/2023-event-schedule/" target="_blank">Event Schedule</a>', content)
        content = re.sub(r'<a href="selections-2023\.html">Official Selections</a>', 
                        '<a href="https://wp.nyu.edu/sff/2023-official-selections/" target="_blank">Official Selections</a>', content)
        content = re.sub(r'<a href="mentions-2023\.html">Honorable Mentions</a>', 
                        '<a href="https://wp.nyu.edu/sff/2023-honorable-mentions/" target="_blank">Honorable Mentions</a>', content)
        content = re.sub(r'<a href="speakers-2023\.html">Speakers</a>', 
                        '<a href="https://wp.nyu.edu/sff/2023-speakers/" target="_blank">Speakers</a>', content)
        content = re.sub(r'<a href="honoree-2023\.html">Honoree</a>', 
                        '<a href="https://wp.nyu.edu/sff/2023-honoree/" target="_blank">Honoree</a>', content)
        
        # Fix 2022 links
        content = re.sub(r'<a href="program-2022\.html">Program</a>', 
                        '<a href="https://wp.nyu.edu/sff/program/" target="_blank">Program</a>', content)
        content = re.sub(r'<a href="schedule-2022\.html">Event Schedule</a>', 
                        '<a href="https://wp.nyu.edu/sff/2022-event-schedule/" target="_blank">Event Schedule</a>', content)
        content = re.sub(r'<a href="speakers-2022\.html">Speakers</a>', 
                        '<a href="https://wp.nyu.edu/sff/2022-guest-speakers/" target="_blank">Speakers</a>', content)
        content = re.sub(r'<a href="honoree-2022\.html">Honoree</a>', 
                        '<a href="https://wp.nyu.edu/sff/2022-honoree/" target="_blank">Honoree</a>', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed navigation links in {filename}")
        return True
        
    except Exception as e:
        print(f"Error updating {filename}: {e}")
        return False

def main():
    updated_count = 0
    for filename in html_files:
        if fix_navigation_in_file(filename):
            updated_count += 1
    
    print(f"\nFixed navigation links in {updated_count} files.")

if __name__ == "__main__":
    main()
