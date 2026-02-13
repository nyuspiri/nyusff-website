
// Film card flip functionality - only one card flipped at a time
function flipCard(filmCard) {
    const poster = filmCard.querySelector('.film-poster');
    const isCurrentlyFlipped = poster.classList.contains('flipped');
    
    // First, close all flipped cards
    const allFlippedCards = document.querySelectorAll('.film-poster.flipped');
    allFlippedCards.forEach(card => {
        card.classList.remove('flipped');
    });
    
    // If the clicked card wasn't already flipped, flip it
    if (!isCurrentlyFlipped) {
        poster.classList.add('flipped');
    }
}

// Close flipped cards when clicking outside
document.addEventListener('click', function(e) {
    if (!e.target.closest('.film-card')) {
        const flippedCards = document.querySelectorAll('.film-poster.flipped');
        flippedCards.forEach(card => {
            card.classList.remove('flipped');
        });
    }
});

// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    // Toggle main mobile menu
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            navMenu.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');
        });
    }
    
    // Handle dropdown toggles on mobile
    function handleMobileDropdowns() {
        const dropdowns = document.querySelectorAll('.nav-dropdown');
        
        dropdowns.forEach(dropdown => {
            const trigger = dropdown.querySelector(':scope > .nav-link, :scope > a');
            
            if (trigger) {
                // Clone the trigger to remove old event listeners
                const newTrigger = trigger.cloneNode(true);
                trigger.parentNode.replaceChild(newTrigger, trigger);
                
                newTrigger.addEventListener('click', function(e) {
                    // Only handle as dropdown on mobile (screen width <= 1024px)
                    if (window.innerWidth <= 1024) {
                        e.preventDefault();
                        e.stopPropagation();
                        
                        // Close other dropdowns at the same level
                        const siblings = dropdown.parentElement.querySelectorAll(':scope > .nav-dropdown');
                        siblings.forEach(sibling => {
                            if (sibling !== dropdown) {
                                sibling.classList.remove('mobile-open');
                            }
                        });
                        
                        // Toggle this dropdown
                        dropdown.classList.toggle('mobile-open');
                    }
                });
            }
        });
    }
    
    // Initialize mobile dropdown handlers
    handleMobileDropdowns();
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (navMenu && !navMenu.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                
                // Close all open dropdowns
                const openDropdowns = document.querySelectorAll('.nav-dropdown.mobile-open');
                openDropdowns.forEach(dropdown => {
                    dropdown.classList.remove('mobile-open');
                });
            }
        }
    });
    
    // Re-initialize dropdown handlers on window resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            // Close mobile menu and dropdowns if switching to desktop
            if (window.innerWidth > 1024) {
                if (navMenu) navMenu.classList.remove('active');
                if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
                
                const openDropdowns = document.querySelectorAll('.nav-dropdown.mobile-open');
                openDropdowns.forEach(dropdown => {
                    dropdown.classList.remove('mobile-open');
                });
            }
        }, 250);
    });

    // Substack RSS Feed Carousel
    var substackTrack = document.getElementById('substackTrack');
    var substackDots = document.getElementById('substackDots');

    if (substackTrack) {
        var SUBSTACK_FEED_URL = 'https://api.rss2json.com/v1/api.json?rss_url=https://nyusff.substack.com/feed';
        var substackIndex = 0;
        var substackPerView = 2.5;
        var substackTotal = 0;
        var substackGap = 16;

        function extractImageFromContent(content) {
            var div = document.createElement('div');
            div.innerHTML = content;
            var img = div.querySelector('img');
            return img ? img.src : null;
        }

        function formatDate(dateStr) {
            var date = new Date(dateStr);
            return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
        }

        function stripHtml(html) {
            var div = document.createElement('div');
            div.innerHTML = html;
            return div.textContent || div.innerText || '';
        }

        function sizeSubstackCards() {
            var viewport = substackTrack.parentElement;
            var viewportWidth = viewport.offsetWidth;
            var cardWidth = (viewportWidth - substackGap * (substackPerView - 1)) / substackPerView;
            var cards = substackTrack.querySelectorAll('.news-item');
            cards.forEach(function(card) {
                card.style.width = cardWidth + 'px';
                card.style.minWidth = cardWidth + 'px';
            });
            return cardWidth;
        }

        function updateSubstackCarousel() {
            var cardWidth = sizeSubstackCards();
            var offset = substackIndex * (cardWidth + substackGap);
            substackTrack.style.transform = 'translateX(-' + offset + 'px)';
            updateSubstackDots();
        }

        function updateSubstackDots() {
            if (!substackDots) return;
            substackDots.innerHTML = '';
            for (var i = 0; i < substackTotal; i++) {
                var dot = document.createElement('button');
                var startVisible = substackIndex;
                var endVisible = substackIndex + substackPerView - 1;
                var isActive = (i >= startVisible && i <= endVisible);
                dot.className = 'substack-dot' + (isActive ? ' active' : '');
                dot.setAttribute('aria-label', 'Go to post ' + (i + 1));
                (function(idx) {
                    dot.addEventListener('click', function() {
                        substackIndex = idx;
                        var maxIndex = Math.max(0, substackTotal - substackPerView);
                        if (substackIndex > maxIndex) substackIndex = maxIndex;
                        updateSubstackCarousel();
                    });
                })(i);
                substackDots.appendChild(dot);
            }
        }

        fetch(SUBSTACK_FEED_URL)
            .then(function(res) { return res.json(); })
            .then(function(data) {
                if (data.status !== 'ok' || !data.items || data.items.length === 0) {
                    substackTrack.innerHTML = '<div class="substack-loading">No posts found.</div>';
                    return;
                }

                var posts = data.items.slice(0, 10);
                substackTotal = posts.length;
                substackTrack.innerHTML = '';

                posts.forEach(function(post) {
                    var imgSrc = post.thumbnail || extractImageFromContent(post.content);
                    var excerpt = stripHtml(post.description).substring(0, 150);
                    if (stripHtml(post.description).length > 150) excerpt += '...';

                    var article = document.createElement('article');
                    article.className = 'news-item';

                    var imageHtml = '';
                    if (imgSrc) {
                        imageHtml = '<div class="news-image"><img src="' + imgSrc + '" alt="' + post.title.replace(/"/g, '&quot;') + '" class="substack-post-thumbnail"></div>';
                    } else {
                        imageHtml = '<div class="news-image"><div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg, var(--color-nyu-purple), var(--color-nyu-violet));color:white;font-family:var(--font-header);font-size:1.2rem;padding:20px;text-align:center;">' + post.title + '</div></div>';
                    }

                    article.innerHTML = '<a href="' + post.link + '" target="_blank" class="news-item-link">' +
                        imageHtml +
                        '<div class="news-content">' +
                        '<h3 class="news-title">' + post.title + '</h3>' +
                        '<p class="news-date">' + formatDate(post.pubDate) + '</p>' +
                        '<p class="news-excerpt">' + excerpt + '</p>' +
                        '</div></a>';

                    substackTrack.appendChild(article);
                });

                updateSubstackCarousel();
            })
            .catch(function(err) {
                console.error('Error loading Substack feed:', err);
                substackTrack.innerHTML = '<div class="substack-loading">Unable to load posts. Visit <a href="https://nyusff.substack.com/" target="_blank">our Substack</a> directly.</div>';
            });

        var leftArrow = document.querySelector('.substack-arrow-left');
        var rightArrow = document.querySelector('.substack-arrow-right');

        if (leftArrow) {
            leftArrow.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                substackIndex--;
                if (substackIndex < 0) substackIndex = Math.max(0, substackTotal - substackPerView);
                updateSubstackCarousel();
            });
        }

        if (rightArrow) {
            rightArrow.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                substackIndex++;
                if (substackIndex > substackTotal - substackPerView) substackIndex = 0;
                updateSubstackCarousel();
            });
        }

        var substackResizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(substackResizeTimer);
            substackResizeTimer = setTimeout(function() {
                updateSubstackCarousel();
            }, 200);
        });
    }
});
