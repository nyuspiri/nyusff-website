# NYU Sports Film Festival Website

## Overview

The NYU Sports Film Festival website is a static, multi-page informational site showcasing an annual film festival co-produced by NYU Production Lab and NYU Athletics. The website features festival information across multiple years (2022-2026), film submissions, event programs, speaker information, and organizational details. Built with vanilla HTML, CSS, and JavaScript, it provides a clean, modern interface with dropdown navigation and interactive film card displays.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Static Multi-Page Application**
- **Technology Stack**: Vanilla HTML5, CSS3, and JavaScript
- **Rationale**: Chosen for simplicity, fast loading times, and ease of deployment without requiring a backend server or build process
- **Structure**: Template-based HTML pages with shared navigation and styling across 40+ pages
- **Styling Approach**: Single centralized stylesheet (`style.css`) with Google Fonts (Inter family) for typography
- **Responsive Design**: Mobile-first approach with viewport meta tags and CSS media queries

**Navigation System**
- **Multi-Level Dropdown Menus**: Nested dropdowns for organizing festival years and event categories
- **Mobile-Responsive Toggle**: JavaScript-powered mobile menu with hamburger toggle
- **Consistent Header**: Shared navigation component across all pages linking to home, submissions, about sections, and yearly events

**Interactive Components**
- **Film Card Flip Functionality**: JavaScript-driven card flip animation for film poster displays
- **Single-Card Focus Pattern**: Only one card can be flipped at a time, improving user experience
- **Click-Outside Detection**: Auto-closes flipped cards when clicking outside the film card area

### Content Organization Pattern

**Year-Based Event Pages**
- **Structure**: Separate pages for each festival year (2022-2026) with sub-pages for:
  - Program details
  - Event schedules
  - Official selections
  - Honorable mentions
  - Speakers
  - Honorees
- **Hybrid Approach**: 2026 content hosted locally; 2025 and earlier years link to external WordPress site
- **Rationale**: Allows preservation of historical content while migrating to new static architecture

**Asset Management**
- **Centralized Assets Folder**: Images, logos, and favicons stored in `/assets` directory
- **Favicon Implementation**: 32x32 PNG favicon consistently applied across all pages
- **Logo Strategy**: Transparent PNG main logo for flexible placement on various backgrounds

### Code Maintenance Tools

**Python Utility Scripts**
- **`add_favicon_to_all.py`**: Automated script to inject favicon links into all HTML pages
- **`fix_email_links.py`**: Converts mailto links to Gmail compose URLs with target="_blank"
- **`fix_navigation_links.py`**: Updates navigation links across multiple pages, particularly for external WordPress links
- **Rationale**: Automation reduces manual errors when making site-wide changes across 40+ pages

**Pattern**: Regular expression-based HTML manipulation for bulk updates while preserving file encoding (UTF-8)

### Design Patterns

**Templating Approach**
- **Copy-Paste Template Pattern**: Pages share identical header/navigation structure
- **Pros**: Simple to understand, no build tools required, easy to debug
- **Cons**: Manual updates required across multiple files for navigation changes (mitigated by Python scripts)

**CSS Architecture**
- **Single Stylesheet Strategy**: One `style.css` file for entire site
- **Font Weights**: Multiple Inter font weights (300-800) loaded for typographic flexibility
- **Naming Convention**: Class-based styling with semantic names (e.g., `.nav-dropdown`, `.film-card`)

**JavaScript Organization**
- **Single Script File**: `script.js` contains all interactive functionality
- **Event Delegation**: Uses document-level event listeners for efficiency
- **DOMContentLoaded Pattern**: Ensures DOM is ready before attaching event handlers

## External Dependencies

**Typography Service**
- **Google Fonts API**: Hosts Inter font family
- **Weights Used**: 300, 400, 500, 600, 700, 800
- **Format**: WOFF2 for optimal web performance
- **Loading Strategy**: CSS link in document head with `display=swap` parameter

**External Content Integration**
- **NYU WordPress Site**: `https://wp.nyu.edu/sff/`
- **Purpose**: Hosts historical festival content (2025 and earlier years)
- **Integration Method**: External links with `target="_blank"` for seamless user experience
- **Rationale**: Maintains access to existing content infrastructure while transitioning to static site

**Image Assets**
- **Local Storage**: All images stored in `/assets` directory
- **Formats**: PNG for logos and favicons
- **No CDN**: Direct file serving for simplicity

**Email Communication**
- **Gmail Compose Integration**: Email links redirect to Gmail compose window
- **Address**: nyusportsfilmfestival@nyu.edu
- **Pattern**: `https://mail.google.com/mail/?view=cm&fs=1&to=EMAIL`
- **Rationale**: Reduces spam and provides consistent email experience

**No Build Process**
- **Direct Deployment**: Files can be served as-is by any static web server
- **No Package Manager**: No npm, webpack, or other build tools required
- **Maintenance Scripts**: Python scripts run manually when batch updates needed