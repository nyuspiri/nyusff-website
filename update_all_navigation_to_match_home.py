
#!/usr/bin/env python3
import os
import re

# List of all HTML files that need updating (excluding index.html since it's the reference)
html_files = [
    'contact.html', 'people.html', 'sponsorship.html', 'submission.html',
    'festival-2022.html', 'festival-2023.html', 'festival-2024.html', 'festival-2025.html', 'festival-2026.html',
    'honoree-2022.html', 'honoree-2023.html', 'honoree-2024.html', 'honoree-2025.html', 'honoree-2026.html',
    'mentions-2022.html', 'mentions-2023.html', 'mentions-2024.html', 'mentions-2025.html', 'mentions-2026.html',
    'program-2022.html', 'program-2023.html', 'program-2024.html', 'program-2025.html', 'program-2026.html',
    'schedule-2022.html', 'schedule-2023.html', 'schedule-2024.html', 'schedule-2025.html', 'schedule-2026.html',
    'selections-2022.html', 'selections-2023.html', 'selections-2024.html', 'selections-2025.html', 'selections-2026.html',
    'speakers-2022.html', 'speakers-2023.html', 'speakers-2024.html', 'speakers-2025.html', 'speakers-2026.html',
    'news-award-winners.html', 'news-tv-special.html'
]

# The correct navigation structure from index.html
correct_navigation = '''                <div class="nav-menu">
                    <a href="index.html" class="nav-link">HOME</a>
                    <a href="submission.html" class="nav-link">SUBMISSION</a>
                    <div class="nav-dropdown">
                        <a href="#" class="nav-link">ABOUT <span class="dropdown-arrow">▼</span></a>
                        <div class="dropdown-content">
                            <a href="about.html">About</a>
                            <a href="people.html">People</a>
                            <a href="sponsorship.html">Sponsorship</a>
                            <a href="contact.html">Contact</a>
                        </div>
                    </div>
                    <div class="nav-dropdown">
                        <a href="#" class="nav-link">EVENTS <span class="dropdown-arrow">▼</span></a>
                        <div class="dropdown-content">
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
                            </div>
                        </div>
                    </div>
                </div>
                <button class="mobile-menu-toggle" aria-label="Toggle Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </nav>'''

def update_navigation_in_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the nav-menu div and replace everything until the closing nav tag
        nav_menu_start = '<div class="nav-menu">'
        nav_end = '</nav>'
        
        start_pos = content.find(nav_menu_start)
        if start_pos == -1:
            print(f"Could not find nav-menu in {filename}")
            return False
        
        # Find the closing nav tag after the nav-menu
        search_start = start_pos
        nav_end_pos = content.find(nav_end, search_start)
        if nav_end_pos == -1:
            print(f"Could not find closing nav tag in {filename}")
            return False
        
        # Replace the entire navigation content
        new_content = (
            content[:start_pos] + 
            correct_navigation +
            content[nav_end_pos + len(nav_end):]
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated navigation in {filename}")
        return True
        
    except Exception as e:
        print(f"Error updating {filename}: {e}")
        return False

def main():
    print("Updating all HTML files to match home page navigation...")
    updated_count = 0
    
    for filename in html_files:
        if update_navigation_in_file(filename):
            updated_count += 1
    
    print(f"\nCompleted: Updated navigation in {updated_count} files to match home page.")

if __name__ == "__main__":
    main()
