
// Film card flip functionality
function flipCard(filmCard) {
    const poster = filmCard.querySelector('.film-poster');
    poster.classList.toggle('flipped');
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
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
});
