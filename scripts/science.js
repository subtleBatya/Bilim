// FOR SCIENTISTS ANIMATION IN THE MAIN FILE



function initializeWebsiteLogic() {
  console.log("All content has been fully loaded. Initializing logic...");

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
}


window.addEventListener("load", initializeWebsiteLogic);



