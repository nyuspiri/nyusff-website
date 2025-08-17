
#!/usr/bin/env python3
import os
import glob

# Updated navigation content
navigation_content = '''                            <div class="nav-dropdown nested">
                                <a href="https://wp.nyu.edu/sff/2025-festival/" target="_blank">2025 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="https://wp.nyu.edu/sff/2025-program/" target="_blank">Program</a>
                                    <a href="https://wp.nyu.edu/sff/2025-event-schedule/" target="_blank">Event Schedule</a>
                                    <a href="https://wp.nyu.edu/sff/2025-official-selections/" target="_blank">Official Selections</a>
                                    <a href="https://wp.nyu.edu/sff/2025-honorable-mentions/" target="_blank">Honorable Mentions</a>
                                    <a href="https://wp.nyu.edu/sff/2025-speakers/" target="_blank">Speakers</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="https://wp.nyu.edu/sff/2024-festival/" target="_blank">2024 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="https://wp.nyu.edu/sff/2024-program/" target="_blank">Program</a>
                                    <a href="https://wp.nyu.edu/sff/2024-event-schedule/" target="_blank">Event Schedule</a>
                                    <a href="https://wp.nyu.edu/sff/2024-official-selections/" target="_blank">Official Selections</a>
                                    <a href="https://wp.nyu.edu/sff/2024-honorable-mentions/" target="_blank">Honorable Mentions</a>
                                    <a href="https://wp.nyu.edu/sff/2024-speakers/" target="_blank">Speakers</a>
                                    <a href="https://wp.nyu.edu/sff/2024-honoree/" target="_blank">Honoree</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="https://wp.nyu.edu/sff/2023-festival/" target="_blank">2023 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="https://wp.nyu.edu/sff/2023-program/" target="_blank">Program</a>
                                    <a href="https://wp.nyu.edu/sff/2023-event-schedule/" target="_blank">Event Schedule</a>
                                    <a href="https://wp.nyu.edu/sff/2023-official-selections/" target="_blank">Official Selections</a>
                                    <a href="https://wp.nyu.edu/sff/2023-honorable-mentions/" target="_blank">Honorable Mentions</a>
                                    <a href="https://wp.nyu.edu/sff/2023-speakers/" target="_blank">Speakers</a>
                                    <a href="https://wp.nyu.edu/sff/2023-honoree/" target="_blank">Honoree</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="https://wp.nyu.edu/sff/2022-festival/" target="_blank">2022 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="https://wp.nyu.edu/sff/program/" target="_blank">Program</a>
                                    <a href="https://wp.nyu.edu/sff/2022-event-schedule/" target="_blank">Event Schedule</a>
                                    <a href="https://wp.nyu.edu/sff/2022-guest-speakers/" target="_blank">Speakers</a>
                                    <a href="https://wp.nyu.edu/sff/2022-honoree/" target="_blank">Honoree</a>
                                </div>
                            </div>'''

# Files to update (excluding index.html and about.html as they're already updated)
html_files = [
    'contact.html', 'people.html', 'sponsorship.html', 'submission.html',
    'festival-2022.html', 'festival-2023.html', 'festival-2024.html', 'festival-2025.html',
    'honoree-2022.html', 'honoree-2023.html', 'honoree-2024.html', 'honoree-2025.html',
    'mentions-2022.html', 'mentions-2023.html', 'mentions-2024.html', 'mentions-2025.html',
    'program-2022.html', 'program-2023.html', 'program-2024.html', 'program-2025.html',
    'schedule-2022.html', 'schedule-2023.html', 'schedule-2024.html', 'schedule-2025.html',
    'selections-2022.html', 'selections-2023.html', 'selections-2024.html', 'selections-2025.html',
    'speakers-2022.html', 'speakers-2023.html', 'speakers-2024.html', 'speakers-2025.html'
]

def update_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the start and end of the events dropdown content
        start_marker = '<div class="nav-dropdown">\n                        <a href="#" class="nav-link">EVENTS <span class="dropdown-arrow">▼</span></a>\n                        <div class="dropdown-content">'
        end_marker = '                        </div>\n                    </div>'
        
        start_pos = content.find(start_marker)
        if start_pos == -1:
            print(f"Could not find navigation section in {filename}")
            return False
        
        # Find the end position after the start marker
        search_start = start_pos + len(start_marker)
        end_pos = content.find(end_marker, search_start)
        if end_pos == -1:
            print(f"Could not find end of navigation section in {filename}")
            return False
        
        # Replace the content between markers
        new_content = (
            content[:start_pos + len(start_marker)] + 
            '\n' + navigation_content + '\n                        ' +
            content[end_pos:]
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {filename}")
        return True
        
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
