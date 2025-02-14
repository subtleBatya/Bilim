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



document.addEventListener("DOMContentLoaded", () => {
    let tel_field = document.getElementById("tel_number");
    let old_value = tel_field.value;

    tel_field.addEventListener("focus", () => {
        if (!tel_field.value.startsWith("+993")) {
            old_value = tel_field.value; // Save old value
            tel_field.value = "+993"; // Pre-fill the field with +993
        }
    });

    tel_field.addEventListener("blur", () => {
        if (tel_field.value === "+993") {
            tel_field.value = old_value; // Restore old value if only "+993" is entered
        }
    });
});



