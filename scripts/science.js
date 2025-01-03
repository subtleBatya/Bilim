// FOR SCIENTISTS ANIMATION IN THE MAIN FILE

const einParentDiv = document.querySelector('.einstein_animes'); 
const einDivs = einParentDiv.querySelectorAll('.einstein_anime'); 

let currentIndex = 0;


function showNextRow() {
  einDivs.forEach((e) => {
    e.style.display = 'none';
  });

  einDivs[currentIndex].style.display = 'flex';

  currentIndex = (currentIndex + 1) % einDivs.length;
}

showNextRow();

setInterval(showNextRow, 4000);