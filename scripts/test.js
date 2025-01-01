document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");
  
    
    const observerCallback = (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("active"); 
          entry.target.style.zIndex = [...sections].indexOf(entry.target) + 10; 
        } else {
          entry.target.classList.remove("active");
          entry.target.style.zIndex = 1; 
        }
      });
    };
  
    
    const observerOptions = {
      threshold: 0.5, 
    };
  
    const observer = new IntersectionObserver(observerCallback, observerOptions);
  
    
    sections.forEach((section) => observer.observe(section));
  });
  





// INTERSECTION API
// document.addEventListener("DOMContentLoaded", () => {
//     const sections = document.querySelectorAll(".section");

//     const observer = new IntersectionObserver(
//         (entries) => {
//             entries.forEach((entry) => {
//                 if (entry.isIntersecting) {
//                     entry.target.classList.add("visible");
//                 }
//             });
//         },
//         {
//             threshold: 0.5,
//         }
//     );

//     sections.forEach((section) => observer.observe(section));
// });

// document.addEventListener("scroll", () => {
//     const sections = document.querySelectorAll(".section");

//     sections.forEach((section, index) => {
//         const rect = section.getBoundingClientRect();

        
//         if (rect.top <= 0) {
//             section.style.zIndex = index + 10; 
//             section.classList.remove("dimmed");
//         } else {
            
//             section.classList.add("dimmed");
//         }
//     });
// });


// document.addEventListener("scroll", () => {
//     const sections = document.querySelectorAll(".section");
//     sections.forEach((section, index) => {
//         const rect = section.getBoundingClientRect();
//         if (rect.top <= 0) {
//             section.style.zIndex = index + 10;
//         }
//     });
// });
