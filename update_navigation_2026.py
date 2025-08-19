
#!/usr/bin/env python3
import os
import glob

# List of all HTML files that need updating
html_files = [
    'index.html', 'contact.html', 'people.html', 'sponsorship.html', 'submission.html',
    'festival-2022.html', 'festival-2023.html', 'festival-2024.html', 'festival-2025.html', 'festival-2026.html',
    'honoree-2022.html', 'honoree-2023.html', 'honoree-2024.html', 'honoree-2025.html', 'honoree-2026.html',
    'mentions-2022.html', 'mentions-2023.html', 'mentions-2024.html', 'mentions-2025.html', 'mentions-2026.html',
    'program-2022.html', 'program-2023.html', 'program-2024.html', 'program-2025.html', 'program-2026.html',
    'schedule-2022.html', 'schedule-2023.html', 'schedule-2024.html', 'schedule-2025.html', 'schedule-2026.html',
    'selections-2022.html', 'selections-2023.html', 'selections-2024.html', 'selections-2025.html', 'selections-2026.html',
    'speakers-2022.html', 'speakers-2023.html', 'speakers-2024.html', 'speakers-2025.html', 'speakers-2026.html'
]

def update_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the events dropdown content start
        events_start = '<div class="nav-dropdown">\n                        <a href="#" class="nav-link">EVENTS <span class="dropdown-arrow">▼</span></a>\n                        <div class="dropdown-content">'
        
        # Look for the pattern that indicates 2025 is the first entry (meaning 2026 is missing)
        pattern_to_find = events_start + '\n                            <div class="nav-dropdown nested">\n                                <a href="https://wp.nyu.edu/sff/2025-festival/" target="_blank">2025'
        
        if pattern_to_find in content:
            # Replace with 2026 section first, then 2025
            replacement = events_start + '''
                            <div class="nav-dropdown nested">
                                <a href="festival-2026.html">2026 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="program-2026.html">Program</a>
                                    <a href="schedule-2026.html">Event Schedule</a>
                                    <a href="selections-2026.html">Official Selections</a>
                                    <a href="mentions-2026.html">Honorable Mentions</a>
                                    <a href="speakers-2026.html">Speakers</a>
                                    <a href="honoree-2026.html">Honoree</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="https://wp.nyu.edu/sff/2025-festival/" target="_blank">2025'''
            
            content = content.replace(pattern_to_find, replacement)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated {filename}")
            return True
        else:
            print(f"2026 section already exists or pattern not found in {filename}")
            return False
        
    except Exception as e:
        print(f"Error updating {filename}: {e}")
        return False

def main():
    updated_count = 0
    for filename in html_files:
        if update_file(filename):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} files successfully.")

if __name__ == "__main__":
    main()
