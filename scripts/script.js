


const data = [
  {
    image: './images/Tesla.webp',
    title: 'Nikola Tesla',
    text: '"Geljegiň güýji elektromagnetizmde ýatyr."'
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


let currentIndex = 1;


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
    
    imageElement.classList.remove('fade-out');
    titleElement.classList.remove('fade-out');
    textElement.classList.remove('fade-out');

    imageElement.classList.remove('fade-in');
    titleElement.classList.remove('fade-in');
    textElement.classList.remove('fade-in');

    
    currentIndex = (currentIndex + 1) % data.length;
  }, 500); 
}


setInterval(updateContent, 5000);
