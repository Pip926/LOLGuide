const track = document.querySelector('.carousel-track');
const cards = Array.from(track.children);
const prevButton = document.getElementById('prevBtn');
const nextButton = document.getElementById('nextBtn');

let rotationIndex = 0;

function updateCarousel() {
    const totalCards = cards.length;

    cards.forEach((card, i) => {
        let position = (i + rotationIndex) % totalCards;
        if (position < 0) position += totalCards;

        card.classList.remove('pos-0', 'pos-1', 'pos-2', 'pos-3', 'is_active');

        card.classList.add(`pos-${position}`);

        if (position === 0) {
            card.classList.add('is-active');
        }
    });
}

nextButton.addEventListener('click', () => {
    rotationIndex--; 
    updateCarousel();
});

prevButton.addEventListener('click', () => {
    rotationIndex++; 
    updateCarousel();
});

updateCarousel();