
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
});
