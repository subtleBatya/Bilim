// SU ASAKDAKY COMMENTLARY ELLEMAN! ELLEMELI DAL!


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



// // Wait for the DOM content to load
// document.addEventListener("DOMContentLoaded", () => {
//   const einsteinParentDiv = document.querySelector(".einstein_animes");
//   const einsteinDivs = einsteinParentDiv.querySelectorAll(".einstein_anime");
//   let currentIndex = 0;

//   // Function to update the active slide
//   function showNextSlide() {
//       // Remove the 'active' class from all slides
//       einsteinDivs.forEach((div) => div.classList.remove("active"));

//       // Add the 'active' class to the current slide
//       einsteinDivs[currentIndex].classList.add("active");

//       // Update the index for the next slide
//       currentIndex = (currentIndex + 1) % einsteinDivs.length; // Loop back to the first slide
//   }

//   // Show the first slide
//   showNextSlide();

//   // Set an interval to auto-slide every 4 seconds
//   const interval = setInterval(showNextSlide, 4000);

//   // Optional: Pause the slider on hover
//   einsteinParentDiv.addEventListener("mouseenter", () => clearInterval(interval));
//   einsteinParentDiv.addEventListener("mouseleave", () => setInterval(showNextSlide, 4000));
// });



