

const data = [
  {
    image: './images/Tesla.webp',
    title: 'Nikola Tesla',
    text: '"Geljegiň güýji Elektromagnetizmde ýatyr"'
  },
  {
    image: './images/Newton.webp',
    title: 'Isaac Newton',
    text: '"Men uzak serhetleri görüp bilýän bolsam, onda men ullakan eňňitleriň üstünde duranlygym üçin"'
  },
  {
    image: './images/MarieCurie.webp',
    title: 'Marie Curie',
    text: '"Ylmyň çäksiz güýji bar"'
  }
];


let currentIndex = 0;


function removeAnimationClasses(element, animationClass) {
  element.addEventListener("animationend", () => {
    element.classList.remove(animationClass);
  }, { once: true });
}

function updateContent() {
  const imageElement = document.getElementById('changing-image');
  const titleElement = document.getElementById('changing-title');
  const textElement = document.getElementById('changing-text');

  imageElement.classList.add('fade-out');
  titleElement.classList.add('fade-out');
  textElement.classList.add('fade-out');

  setTimeout(() => {
    imageElement.src = data[currentIndex].image;
    titleElement.textContent = data[currentIndex].title;
    textElement.textContent = data[currentIndex].text;

    imageElement.classList.add('fade-in');
    titleElement.classList.add('fade-in');
    textElement.classList.add('fade-in');

    removeAnimationClasses(imageElement, 'fade-in');
    removeAnimationClasses(titleElement, 'fade-in');
    removeAnimationClasses(textElement, 'fade-in');

    removeAnimationClasses(imageElement, 'fade-out');
    removeAnimationClasses(titleElement, 'fade-out');
    removeAnimationClasses(textElement, 'fade-out');

    currentIndex = (currentIndex + 1) % data.length;
  }, 500);
}

updateContent();

setInterval(updateContent, 5000);
