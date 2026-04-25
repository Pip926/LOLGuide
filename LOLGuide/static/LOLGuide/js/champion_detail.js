document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('[data-target]');
    const viewContents = document.querySelectorAll('.view-content');
    
    const abilityCaption = document.getElementById('ability-caption');
    const abilityBody = document.getElementById('ability-body');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const targetView = document.getElementById(`view-${targetId}`);

            buttons.forEach(b => b.classList.remove('active'));
            viewContents.forEach(v => {
                v.classList.remove('active');
                v.style.display = 'none';
            });

            if (targetId === 'ability') {
                abilityCaption.innerText = btn.getAttribute('data-name');
                abilityBody.innerText = btn.getAttribute('data-text');
            }

            btn.classList.add('active');
            if (targetView) {
                targetView.classList.add('active');
                targetView.style.display = 'block';
            }
        });
    });
});