
const showTarea = document.getElementById('show-tarea');
const modalTarea = document.getElementById('modal-tarea');

showTarea.addEventListener('click', (e) => {
    e.preventDefault();
    modalTarea.classList.add('modal--show');
    showTarea.style.display = 'none';
    showProyecto.style.display = 'none';
    modalTarea.style.transition = '450ms';
});

modalTarea.addEventListener('click', (e) => {
    if (e.target.classList.contains('agregar-tarea-mobil')) 
        modalTarea.classList.remove('modal--show')
        showTarea.style.display = 'block';
        showProyecto.style.display = 'block';
        showTarea.style.transition = '450ms';
});

const showProyecto = document.getElementById('show-proyecto');
const modalProyecto = document.getElementById('modal-proyecto');

showProyecto.addEventListener('click', (e) => {
    e.preventDefault();
    modalProyecto.classList.add('modal--show');
    showProyecto.style.display = 'none';
    showTarea.style.display = 'none';
    modalProyecto.style.transition = '450ms';
});

modalProyecto.addEventListener('click', (e) => {
    if (e.target.classList.contains('agregar-proyecto-mobil')) 
        modalProyecto.classList.remove('modal--show')
        showProyecto.style.display = 'block';
        showTarea.style.display = 'block';
        showProyecto.style.transition = '450ms';
});