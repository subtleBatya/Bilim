const swiper = new Swiper(".swiper-container", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto", // Change to "auto" to prevent extra width issues
  coverflowEffect: {
    rotate: 0, 
    stretch: -20, // Reduce this value
    depth: 150, 
    modifier: 2, 
    slideShadows: false,
  },
  loop: true,
  breakpoints: {
    0: {
      slidesPerView: 1,
      coverflowEffect: {
        stretch: -10, 
        depth: 120, 
      },
    },
    768: {
      slidesPerView: 2,
      coverflowEffect: {
        stretch: -15, 
        depth: 140, 
      },
    },
    1024: {
      slidesPerView: 3,
      coverflowEffect: {
        stretch: -20, 
        depth: 200, 
      },
    },
  },
});


// const swiper = new Swiper(".swiper-container", {
//   effect: "coverflow",
//   grabCursor: true,
//   centeredSlides: true,
//   slidesPerView: 3, // Default for larger screens
//   coverflowEffect: {
//     rotate: 0, 
//     stretch: -40, 
//     depth: 200, 
//     modifier: 2, 
//     slideShadows: false,
//   },
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
//   loop: true,
//   breakpoints: {
//     // Small devices (mobile)
//     0: {
//       slidesPerView: 1,
//       coverflowEffect: {
//         stretch: -30, 
//         depth: 180, 
//       },
//     },
//     // Medium devices (tablets)
//     768: {
//       slidesPerView: 2,
//       coverflowEffect: {
//         stretch: -30, 
//         depth: 150, 
//       },
//     },
//     // Large devices (desktops)
//     1024: {
//       slidesPerView: 3,
//       coverflowEffect: {
//         stretch: -40, 
//         depth: 300, 
//       },
//     },
//   },
// });





// const swiper = new Swiper(".swiper-container", {
//     effect: "coverflow",
//     grabCursor: true,
//     centeredSlides: true,
//     slidesPerView: "3",
//     coverflowEffect: {
//       rotate: 0, // No rotation for slides
//       stretch: -40, // Pulls the side images inward
//       depth: 200, // Adds a 3D perspective effect
//       modifier: 2, // Multiplier for scaling and depth
//       slideShadows: false, // Disables shadow for cleaner design
//     },
//     navigation: {
//       nextEl: ".swiper-button-next",
//       prevEl: ".swiper-button-prev",
//     },
//     loop: true, // Enable infinite scrolling
//   });

// console.log(typeof Swiper); // Should return "function"

// document.addEventListener('DOMContentLoaded', () => {
// const swiper = new Swiper('.swiper-container', {
//     effect: 'coverflow',
//     slidesPerView: 2,
//     centeredSlides: true,
//     loop: true, // Enables infinite scrolling
//     grabCursor: true, // Changes the cursor to a grab icon
//     coverflowEffect: {
//         rotate: 0, // Angle of rotation for inactive slides
//         stretch: 150, // Spacing between slides
//         depth: 150, // Perspective depth
//          // Multiplier for scale and rotation
//         // Enable shadows on slides
//       },
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },
//     pagination: {
//       el: '.swiper-pagination',
//       clickable: true,
//     },
//   });
  
//   swiper.on('slideChange', () => {
//     document.querySelectorAll('.swiper-slide').forEach((slide, index) => {
//       if (index === swiper.activeIndex) {
//         slide.querySelector('img').style.transform = 'scale(1.2) translateX(0)';
//       } else {
//         slide.querySelector('img').style.transform = 'scale(0.9) translateX(10px)';
//       }
//     });
//   });
  
// });





// document.addEventListener("DOMContentLoaded", () => {
//     const images = document.querySelectorAll(".slider-image");
//     const prevBtn = document.querySelector(".slider-btn.prev");
//     const nextBtn = document.querySelector(".slider-btn.next");
  
//     let currentIndex = 0;
  
//     const updateSlider = () => {
//       images.forEach((img, index) => {
//         img.classList.remove("active", "left", "right");
  
//         if (index === currentIndex) {
//           img.classList.add("active");
//         } else if (index === (currentIndex - 1 + images.length) % images.length) {
//           img.classList.add("left");
//         } else if (index === (currentIndex + 1) % images.length) {
//           img.classList.add("right");
//         }
//       });
//     };
  
//     prevBtn.addEventListener("click", () => {
//       currentIndex = (currentIndex - 1 + images.length) % images.length;
//       updateSlider();
//     });
  
//     nextBtn.addEventListener("click", () => {
//       currentIndex = (currentIndex + 1) % images.length;
//       updateSlider();
//     });
  
//     updateSlider(); 
//   });
  