const openModal = document.querySelector('.nuevo-proyecto');
const modal = document.querySelector('.modal');

openModal.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.add('modal--show');
});
modal.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) modal.classList.remove('modal--show')
});