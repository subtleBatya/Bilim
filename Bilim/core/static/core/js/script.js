// Функция для button в Оплате 
const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');
const content = document.getElementById('content');
const registration = document.getElementById('registration');

// Ensure all necessary elements exist before proceeding
if ( !content || !registration) {
    console.error("Error: One or more required elements are missing from the DOM.");
} else {
    // Show content and set initial active button
    content.classList.remove('d-none');
    button1.classList.add('active');

    button1.addEventListener('click', () => {
        content.classList.remove('d-none');
        registration.classList.add('d-none');
        button1.classList.add('active');
        button2.classList.remove('active');
    });

    button2.addEventListener('click', () => {
        content.classList.add('d-none');
        registration.classList.remove('d-none');
        button2.classList.add('active');
        button1.classList.remove('active');

        // Scroll after layout update
        setTimeout(() => {
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        }, 50);
    });
}










// Функция для button в Оплате
// const button1 = document.getElementById('button1');
// const button2 = document.getElementById('button2');
// const content = document.getElementById('content');
// const registration = document.getElementById('registration');
// if(content && button1 && button2) {
//   content.classList.remove('d-none');
//   button1.classList.add('active');


//   button1.addEventListener('click', () => {
//     content.classList.remove('d-none');
//     registration.classList.add('d-none');
//     button1.classList.add('active');
//     button2.classList.remove('active');
//   });
  
//   button2.addEventListener('click', () => {
//     content.classList.add('d-none');
//     registration.classList.remove('d-none');
//     button2.classList.add('active');
//     button1.classList.remove('active');
//     window.scrollTo(0, document.body.scrollHeight);
//   });
// }





