document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.champions-container');
    const upBtn = document.getElementById('scrollUp');
    const downBtn = document.getElementById('scrollDown');

    const scrollStep = 400; 

    downBtn.addEventListener('click', () => {
        container.scrollBy({
            top: scrollStep,
            behavior: 'smooth'
        });
    });

    upBtn.addEventListener('click', () => {
        container.scrollBy({
            top: -scrollStep,
            behavior: 'smooth'
        });
    });
});