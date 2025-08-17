
import os
import re

# HTML files to update
html_files = [
    'about.html',
    'contact.html', 
    'people.html',
    'sponsorship.html',
    'submission.html',
    'festival-2026.html'
]

# The old navigation pattern
old_pattern = r'''                            <div class="nav-dropdown nested">
                                <a href="festival-2025\.html">2025 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="program-2025\.html">Program</a>
                                    <a href="schedule-2025\.html">Event Schedule</a>
                                    <a href="selections-2025\.html">Official Selections</a>
                                    <a href="mentions-2025\.html">Honorable Mentions</a>
                                    <a href="speakers-2025\.html">Speakers</a>
                                    <a href="honoree-2025\.html">Honoree</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="festival-2024\.html">2024 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="program-2024\.html">Program</a>
                                    <a href="schedule-2024\.html">Event Schedule</a>
                                    <a href="selections-2024\.html">Official Selections</a>
                                    <a href="mentions-2024\.html">Honorable Mentions</a>
                                    <a href="speakers-2024\.html">Speakers</a>
                                    <a href="honoree-2024\.html">Honoree</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="festival-2023\.html">2023 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="program-2023\.html">Program</a>
                                    <a href="schedule-2023\.html">Event Schedule</a>
                                    <a href="selections-2023\.html">Official Selections</a>
                                    <a href="mentions-2023\.html">Honorable Mentions</a>
                                    <a href="speakers-2023\.html">Speakers</a>
                                    <a href="honoree-2023\.html">Honoree</a>
                                </div>
                            </div>
                            <div class="nav-dropdown nested">
                                <a href="festival-2022\.html">2022 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="program-2022\.html">Program</a>
                                    <a href="schedule-2022\.html">Event Schedule</a>
                                    <a href="selections-2022\.html">Official Selections</a>
                                    <a href="mentions-2022\.html">Honorable Mentions</a>
                                    <a href="speakers-2022\.html">Speakers</a>
                                    <a href="honoree-2022\.html">Honoree</a>
                                </div>
                            </div>'''

# The new navigation replacement
new_navigation = '''                            <div class="nav-dropdown nested">
                                <a href="https://wp.nyu.edu/sff/2025-festival/" target="_blank">2025 <span class="dropdown-arrow">▶</span></a>
                                <div class="dropdown-content nested">
                                    <a href="https://wp.nyu.edu/sff/2025-program/" target="_blank">Program</a>
                                    <a href="https://wp.nyu.edu/sff/2025-event-schedule/" target="_blank">Event Schedule</a>
                                    <a href="https://wp.nyu.edu/sff/2025-official-selections/" target="_blank">Official Selections</a>
                                    <a href="https://wp.nyu.edu/sff/2025-honorable-mentions/" target="_blank">Honorable Mentions</a>
                                    <a href="https://wp.nyu.edu/sff/2025-speakers/" target="_blank">Speakers</a>
                                    <a href="https://wp.nyu.edu/sff/2025-honoree/" target="_blank">Honoree</a>
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
                                    <a href="https://wp.nyu.edu/sff/2022-program/" target="_blank">Program</a>
                                    <a href="https://wp.nyu.edu/sff/2022-event-schedule/" target="_blank">Event Schedule</a>
                                    <a href="https://wp.nyu.edu/sff/2022-official-selections/" target="_blank">Official Selections</a>
                                    <a href="https://wp.nyu.edu/sff/2022-honorable-mentions/" target="_blank">Honorable Mentions</a>
                                    <a href="https://wp.nyu.edu/sff/2022-speakers/" target="_blank">Speakers</a>
                                    <a href="https://wp.nyu.edu/sff/2022-honoree/" target="_blank">Honoree</a>
                                </div>
                            </div>'''

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the navigation section
        updated_content = re.sub(old_pattern, new_navigation, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Updated navigation in {filename}")

print("All navigation updates completed!")
