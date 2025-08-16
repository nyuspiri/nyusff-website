import os
import re

# The correct footer content
correct_footer = '''    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-content">
                <div class="footer-intro">
                    <h3 class="footer-title">THE PREMIER INTERSECTION OF SPORTS X FILM CULTURE</h3>
                </div>
                
                <div class="footer-links">
                    <div class="footer-section">
                        <h4>About</h4>
                        <ul>
                            <li><a href="about.html">History of NYUSFF</a></li>
                            <li><a href="people.html">People</a></li>
                            <li><a href="contact.html">Contact</a></li>
                        </ul>
                    </div>

                    <div class="footer-section">
                        <h4>Join & Support</h4>
                        <ul>
                            <li><a href="sponsorship.html">Become a Sponsor</a></li>
                            <li><a href="#">Volunteer</a></li>
                            <li><a href="https://www.eventbrite.com/cc/5th-annual-nyu-sports-film-festival-4161713" target="_blank">Event RSVP</a></li>
                        </ul>
                    </div>

                    <div class="footer-section">
                        <h4>Connect</h4>
                        <ul>
                            <li><a href="https://www.instagram.com/nyusportsfilm/" target="_blank">Instagram</a></li>
                            <li><a href="https://www.linkedin.com/company/nyu-sports-film-festival/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3Bng8OALX4S%2Be9efKHAvWHZQ%3D%3D" target="_blank">LinkedIn</a></li>
                            <li><a href="mailto:nyusportsfilmfestival@nyu.edu">Email</a></li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <div class="footer-legal">
                    <a href="https://www.nyu.edu/footer/copyright-and-fair-use/digital-privacy-statement.html" target="_blank">Privacy Policy</a>
                    <a href="https://www.nyu.edu/footer/accessibility.html" target="_blank">Accessibility Statement</a>
                </div>

                <div class="footer-sponsors">
                    <div class="sponsor-logos">
                        <img src="./THE NYU Sports Film Festival – Co-Produced by the NYU Production Lab and NYU Athletics_files/Production-1024x1024.png" alt="NYU Production Lab">
                        <img src="./THE NYU Sports Film Festival – Co-Produced by the NYU Production Lab and NYU Athletics_files/Athletics-1024x1024.png" alt="NYU Athletics">
                        <img src="./THE NYU Sports Film Festival – Co-Produced by the NYU Production Lab and NYU Athletics_files/SNY-1024x1024.png" alt="SNY">
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Files that need footer updates
files_to_update = [
    'honoree-2022.html',
    'honoree-2023.html', 
    'honoree-2024.html',
    'honoree-2025.html',
    'mentions-2022.html',
    'mentions-2023.html',
    'mentions-2024.html', 
    'mentions-2025.html',
    'people.html',
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
    'speakers-2025.html',
    'submission.html'
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace footer content
        # Look for the footer section and replace everything from <!-- Footer --> to </html>
        footer_pattern = r'    <!-- Footer -->.*?</html>'
        
        if re.search(footer_pattern, content, re.DOTALL):
            # Replace existing footer
            updated_content = re.sub(footer_pattern, correct_footer, content, flags=re.DOTALL)
        else:
            # Look for just the footer tag and replace from there
            footer_pattern2 = r'    <footer class="site-footer">.*?</html>'
            if re.search(footer_pattern2, content, re.DOTALL):
                updated_content = re.sub(footer_pattern2, correct_footer, content, flags=re.DOTALL)
            else:
                print(f"Could not find footer pattern in {filename}")
                continue
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Updated footer in {filename}")

print("All footer updates completed!")
