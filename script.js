// NYUSFF site scripts: navigation, film card flips, Substack feed.

const MOBILE_NAV = window.matchMedia('(max-width: 1024px)');

/* ---------- Navigation ---------- */

function setExpanded(button, open) {
    button.setAttribute('aria-expanded', String(open));
    button.closest('.nav-dropdown').classList.toggle('open', open);
}

function closeDropdowns(except) {
    document.querySelectorAll('.dropdown-toggle[aria-expanded="true"], .submenu-toggle[aria-expanded="true"]')
        .forEach(btn => {
            if (except && btn.closest('.nav-dropdown').contains(except)) return;
            setExpanded(btn, false);
        });
}

function initNavigation() {
    const header = document.querySelector('.site-header');
    const toggle = document.querySelector('.mobile-menu-toggle');
    const menu = document.getElementById('site-menu');
    if (!header || !toggle || !menu) return;

    function setMenu(open) {
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        menu.classList.toggle('open', open);
        document.body.classList.toggle('menu-open', open);
        if (!open) closeDropdowns();
    }

    toggle.addEventListener('click', () => {
        setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });

    // Top-level dropdowns (About, Events, TV Specials) and nested year submenus
    header.querySelectorAll('.dropdown-toggle, .submenu-toggle').forEach(btn => {
        btn.addEventListener('click', event => {
            event.stopPropagation();
            // On desktop the menu is already open from hovering, so a click keeps it open
            const hovered = !MOBILE_NAV.matches && btn.closest('.nav-dropdown').matches(':hover');
            const open = hovered || btn.getAttribute('aria-expanded') !== 'true';
            closeDropdowns(btn);
            setExpanded(btn, open);
        });
    });

    // Desktop: open on hover too, so the menus feel the same as before
    header.querySelectorAll('.nav-dropdown').forEach(dropdown => {
        const btn = dropdown.querySelector(':scope > .dropdown-toggle, :scope > .nested-row > .submenu-toggle');
        if (!btn) return;
        dropdown.addEventListener('mouseenter', () => { if (!MOBILE_NAV.matches) setExpanded(btn, true); });
        dropdown.addEventListener('mouseleave', () => { if (!MOBILE_NAV.matches) setExpanded(btn, false); });
    });

    document.addEventListener('click', event => {
        if (!header.contains(event.target)) {
            closeDropdowns();
            setMenu(false);
        }
    });

    document.addEventListener('keydown', event => {
        if (event.key !== 'Escape') return;
        const wasOpen = toggle.getAttribute('aria-expanded') === 'true';
        closeDropdowns();
        setMenu(false);
        if (wasOpen) toggle.focus();
    });

    // Leaving the mobile layout resets everything
    MOBILE_NAV.addEventListener('change', () => setMenu(false));

    // Header shadow once the page scrolls
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 4);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
}

/* ---------- Film cards (homepage) ---------- */

function flipCard(filmCard) {
    const poster = filmCard.querySelector('.film-poster');
    const wasFlipped = poster.classList.contains('flipped');
    document.querySelectorAll('.film-poster.flipped').forEach(p => p.classList.remove('flipped'));
    if (!wasFlipped) poster.classList.add('flipped');
}

function initFilmCards() {
    document.querySelectorAll('.film-poster').forEach(poster => {
        poster.setAttribute('role', 'button');
        poster.setAttribute('tabindex', '0');
        const title = poster.parentElement.querySelector('.film-title');
        if (title) poster.setAttribute('aria-label', `Show logline for ${title.textContent.trim()}`);
        poster.addEventListener('click', () => flipCard(poster.parentElement));
        poster.addEventListener('keydown', event => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                flipCard(poster.parentElement);
            }
        });
    });

    document.addEventListener('click', event => {
        if (!event.target.closest('.film-card')) {
            document.querySelectorAll('.film-poster.flipped').forEach(p => p.classList.remove('flipped'));
        }
    });
}

/* ---------- Substack feed (homepage) ---------- */

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function stripHtml(html) {
    return new DOMParser().parseFromString(html, 'text/html').body.textContent || '';
}

function firstImage(html) {
    const img = new DOMParser().parseFromString(html, 'text/html').querySelector('img');
    return img ? img.getAttribute('src') : null;
}

function initSubstackFeed() {
    const track = document.getElementById('substackTrack');
    if (!track) return;

    const FEED_URL = 'https://api.rss2json.com/v1/api.json?rss_url=https://nyusff.substack.com/feed';

    fetch(FEED_URL)
        .then(res => res.json())
        .then(data => {
            if (data.status !== 'ok' || !data.items || data.items.length === 0) {
                track.innerHTML = '<div class="substack-loading">No posts found.</div>';
                return;
            }

            track.innerHTML = data.items.slice(0, 10).map(post => {
                const title = escapeHtml(post.title);
                const imgSrc = post.thumbnail || firstImage(post.content);
                const text = stripHtml(post.description);
                const excerpt = escapeHtml(text.length > 150 ? text.slice(0, 150).trim() + '…' : text);
                const date = new Date(post.pubDate).toLocaleDateString('en-US', {
                    year: 'numeric', month: 'long', day: 'numeric'
                });
                const image = imgSrc
                    ? `<img src="${escapeHtml(imgSrc)}" alt="" class="substack-post-thumbnail" loading="lazy">`
                    : `<div class="news-image-fallback">${title}</div>`;

                return `<article class="news-item">
                    <a href="${escapeHtml(post.link)}" target="_blank" rel="noopener" class="news-item-link">
                        <div class="news-image">${image}</div>
                        <div class="news-content">
                            <h3 class="news-title">${title}</h3>
                            <p class="news-date">${date}</p>
                            <p class="news-excerpt">${excerpt}</p>
                        </div>
                    </a>
                </article>`;
            }).join('');
        })
        .catch(err => {
            console.error('Error loading Substack feed:', err);
            track.innerHTML = '<div class="substack-loading">Unable to load posts. Visit <a href="https://nyusff.substack.com/" target="_blank" rel="noopener">our Substack</a> directly.</div>';
        });
}

initNavigation();
initFilmCards();
initSubstackFeed();
