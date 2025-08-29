
import os
import re

# The correct footer content from index.html
correct_footer = '''    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-content">
                <div class="footer-intro">
                    <h3 class="footer-title">THE PREMIER<br>INTERSECTION OF<br><span class="highlight">SPORTS X FILM</span><br>CULTURE</h3>
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
                            <li><a href="contact.html">Volunteer</a></li>
                            <li><a href="https://www.eventbrite.com/cc/5th-annual-nyu-sports-film-festival-4161713" target="_blank">Event RSVP</a></li>
                        </ul>
                    </div>

                    <div class="footer-section">
                        <h4>Connect</h4>
                        <ul>
                            <li><a href="https://www.instagram.com/nyusportsfilm/" target="_blank">Instagram</a></li>
                            <li><a href="https://www.linkedin.com/company/nyu-sports-film-festival/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3Bng8OALX4S%2Be9efKHAvWHZQ%3D%3D" target="_blank">LinkedIn</a></li>
                            <li><a href="https://mail.google.com/mail/?view=cm&fs=1&to=nyusportsfilmfestival@nyu.edu" target="_blank">Email</a></li>
                        </ul>
                    </div>

                    <div class="footer-section footer-logo-section">
                        <img src="assets/Player Logo NYUSFF.png" alt="NYUSFF Player Logo" class="player-logo">
                    </div>
                </div>
            </div>
            
            <div class="footer-legal-bar">
                <div class="footer-copyright">
                    © 2025 NYU Sports Film Festival
                </div>
                <div class="footer-legal">
                    <a href="https://www.nyu.edu/footer/copyright-and-fair-use/digital-privacy-statement.html" target="_blank">Privacy Policy</a>
                    <a href="https://www.nyu.edu/footer/accessibility.html" target="_blank">Accessibility Statement</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Get all HTML files in the current directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

def update_footer(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Multiple patterns to match different footer variations
        patterns = [
            r'    <!-- Footer -->.*?</html>',
            r'    <footer class="site-footer">.*?</html>',
            r'<footer class="site-footer">.*?</html>',
            r'<!-- Footer -->.*?</html>'
        ]
        
        updated = False
        for pattern in patterns:
            if re.search(pattern, content, re.DOTALL):
                updated_content = re.sub(pattern, correct_footer, content, flags=re.DOTALL)
                if updated_content != content:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"✓ Updated footer in {filename}")
                    updated = True
                    break
        
        if not updated:
            print(f"- No footer pattern found in {filename}")
        
        return updated
        
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")
        return False

def main():
    print("Updating all HTML files to use the same footer as index.html...")
    updated_count = 0
    
    # Skip index.html since it already has the correct footer
    files_to_update = [f for f in html_files if f != 'index.html']
    
    for filename in files_to_update:
        if update_footer(filename):
            updated_count += 1
    
    print(f"\nCompleted: Updated {updated_count} files with the standardized footer.")

if __name__ == "__main__":
    main()
