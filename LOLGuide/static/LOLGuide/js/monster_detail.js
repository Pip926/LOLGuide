document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.tab-btn');
    const articles = document.querySelectorAll('.monster-article');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');

            buttons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            articles.forEach(article => {
                article.style.display = 'none';
            });

            const activeArticle = document.getElementById('text-' + targetTab);
            if (activeArticle) {
                activeArticle.style.display = 'block';
            }
        });
    });
});