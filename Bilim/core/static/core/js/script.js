// Функция для button в Оплате
const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');
const content = document.getElementById('content');
const registration = document.getElementById('registration');

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
});

function initializeWebsiteLogic() {
  console.log("All content has been fully loaded. Initializing logic...");

    //Функция для button в Оплате
    const button1 = document.getElementById('button1')
    const button2 = document.getElementById('button2')
    const content = document.getElementById('content')
    const registration = document.getElementById('registration')

    content.classList.remove('d-none')
    button1.classList.add('active')

    button1.addEventListener('click', () => {
      content.classList.remove('d-none')
      registration.classList.add('d-none')
      button1.classList.add('active')
      button2.classList.remove('active')
    })

    button2.addEventListener('click', () => {
      content.classList.add('d-none')
      registration.classList.remove('d-none')
      button2.classList.add('active')
      button1.classList.remove('active')
    })

    console.log("Initialization complete.");
  } 







