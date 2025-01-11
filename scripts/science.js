// FOR SCIENTISTS ANIMATION IN THE MAIN FILE

// Wrap the logic inside an async function
async function initializeWebsiteLogic() {
  console.log("All content has been fully loaded. Initializing logic...");

  try {
    // Simulate a heavy or asynchronous task
    await performHeavyInitialization();

    // Your website's logic here
   
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



    console.log("Initialization complete.");
  } catch (error) {
    console.error("Error during initialization:", error);
  }
}

// A mock function to simulate a heavy initialization task
async function performHeavyInitialization() {
  console.log("Starting heavy initialization...");

  // Simulating a delay, e.g., loading data or preparing resources
  return new Promise((resolve) => setTimeout(resolve, 2000)); // 2-second delay
}

// Attach the initialize function to the window load event
window.addEventListener("load", async () => {
  await initializeWebsiteLogic();
});





