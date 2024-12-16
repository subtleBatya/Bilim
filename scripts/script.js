// script.js

// Define an array of images and corresponding text
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

// Current index for tracking content
let currentIndex = 0;

// Function to update content with animations
function updateContent() {
  const imageElement = document.getElementById('changing-image');
  const titleElement = document.getElementById('changing-title');
  const textElement = document.getElementById('changing-text');

  // Add fade-out animation
  imageElement.classList.add('fade-out');
  titleElement.classList.add('fade-out');
  textElement.classList.add('fade-out');

  // Wait for fade-out animation to complete before updating content
  setTimeout(() => {
    // Update content
    imageElement.src = data[currentIndex].image;
    titleElement.textContent = data[currentIndex].title;
    textElement.textContent = data[currentIndex].text;

    // Reset fade-out, add fade-in
    

    imageElement.classList.add('fade-in');
    titleElement.classList.add('fade-in');
    textElement.classList.add('fade-in');
    
    imageElement.classList.remove('fade-out');
    titleElement.classList.remove('fade-out');
    textElement.classList.remove('fade-out');

    imageElement.classList.remove('fade-in');
    titleElement.classList.remove('fade-in');
    textElement.classList.remove('fade-in');

    // Move to the next index, loop back if needed
    currentIndex = (currentIndex + 1) % data.length;
  }, 500); // Duration matches fade-out animation
}

// Change content every 5 seconds
setInterval(updateContent, 5000);
