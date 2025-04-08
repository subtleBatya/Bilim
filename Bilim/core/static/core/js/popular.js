var swiper = new Swiper('.swiper', {
  effect: 'coverflow',
  grabCursor: true,
  centeredSlides: true,
  initialSlide: 2,
  speed: 600,
  preventClicks: true,
  slidesPerView: 'auto',
  coverflowEffect: {
        rotate: 0,         // Set the rotation degree for coverflow effect
        stretch: 80,         // Set the stretch between the slides
        depth: 350,         // Set the depth effect for perspective
        modifier: 1,        // Set the modifier for scaling
        slideShadows: true, // Enable shadows on the slides
      },
      on: {
        click(event) {
          swiper.slideTo(this.clickedIndex);
        },
      },
      pagination: {
        el: '.swiper-pagination',
      },
})
  
  // BELOW ARE 18.02.2025 CHANGES

  // var swiper = new Swiper('.swiper-container', {
  //   effect: 'coverflow',  // Enable Coverflow effect
  //   grabCursor: true,     // Enable cursor grab effect
  //   centeredSlides: true, // Center the slides
  //   slidesPerView: 1,     // Default for small screens (only 1 image visible)
  //   spaceBetween: 10,     // Space between slides
  //   loop: true,           // Enable looping of slides
  //   coverflowEffect: {
  //     rotate: -20,         // Set the rotation degree for coverflow effect
  //     stretch: 0,         // Set the stretch between the slides
  //     depth: 100,         // Set the depth effect for perspective
  //     modifier: 1,        // Set the modifier for scaling
  //     slideShadows: true, // Enable shadows on the slides
  //   },
  //   navigation: {
  //     nextEl: '.swiper-button-next',
  //     prevEl: '.swiper-button-prev',
  //   },
  //   pagination: {
  //     el: '.swiper-pagination',
  //     clickable: true,
  //   },
  //   breakpoints: {
  //     // When window width is >= 768px (tablets)
  //     768: {
  //       slidesPerView: 2,  // Show 2 slides on medium screens
  //       spaceBetween: 20,
  //     },
  //     // When window width is >= 1024px (desktops)
  //     1024: {
  //       slidesPerView: 3,  // Show 3 slides on large screens
  //       spaceBetween: 30,
  //     },
  //   },
  // });


  // window.addEventListener('load', function() {
  //   document.body.style.overflowX = 'hidden'; // Disable horizontal scroll on page load
  
  //   // After a short delay, re-enable overflow if needed
  //   setTimeout(() => {
  //     document.body.style.overflowX = ''; // Reset overflow (if needed)
  //   }, 1000);
  // });


/*  BELOW IS THE UNMODIFIED VERSION BEFORE 17.02.2025 */

// const swiper = new Swiper(".swiper", {
//   slidesPerView: "auto", // Adjusts dynamically
//   spaceBetween: 10, // Adds spacing for better layout
//   centeredSlides: true,
//   loop: true,
//   simulateTouch: "ontouchstart" in window || navigator.maxTouchPoints > 0,
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
//   breakpoints: {
//     320: { slidesPerView: 1 }, // Mobile: 1 slide
//     480: { slidesPerView: 2 }, // Small screens: 2 slides
//     768: { slidesPerView: 3 }, // Tablets: 3 slides
//     1024: { slidesPerView: 4 }, // Desktops: 4 slides
//     1440: { slidesPerView: 5 }, // Large screens: 5 slides
//   },
// });

// const calculateHeight = () => {
//   const swiperSlideElements = document.querySelectorAll('.swiper .swiper-slide');
//   if (!swiperSlideElements.length) return;
//   const width = swiperSlideElements[0].getBoundingClientRect().width;
//   const height = Math.round(width / (16 / 9)); // Maintain aspect ratio
//   swiperSlideElements.forEach(element => element.style.height = `${height}px`);
// };

// document.addEventListener("DOMContentLoaded", calculateHeight);
// window.addEventListener("resize", calculateHeight);

/*  ABOVE IS THE UNMODIFIED VERSION BEFORE 17.02.2025 */

// const swiper = new Swiper(".swiper", {
//   slidesPerView: 5,
//   spaceBetween: 0,
//   centeredSlides: true,
//   loop: true,
//   simulateTouch: 'ontouchstart' in window || navigator.maxTouchPoints > 0,
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// })

// const calculateHeight = () => {
//   const swiperSlideElements = Array.from(document.querySelectorAll('.swiper .swiper-slide'))
//   if (!swiperSlideElements.length) return
//   const width = swiperSlideElements[0].getBoundingClientRect().width
//   const height = Math.round(width / (16 / 9))
//   swiperSlideElements.map(element => element.style.height = `${height}px`)
// }

// document.addEventListener("DOMContentLoaded", calculateHeight)
// addEventListener('resize', calculateHeight)

// const swiper = new Swiper(".swiper-container", {
//   effect: "coverflow",
//   grabCursor: true,
//   centeredSlides: true,
//   slidesPerView: "auto", // Change to "auto" to prevent extra width issues
//   coverflowEffect: {
//     rotate: 0, 
//     stretch: -20, // Reduce this value
//     depth: 150, 
//     modifier: 2, 
//     slideShadows: false,
//   },
//   loop: true,
//   breakpoints: {
//     0: {
//       slidesPerView: 1,
//       coverflowEffect: {
//         stretch: -10, 
//         depth: 120, 
//       },
//     },
//     768: {
//       slidesPerView: 2,
//       coverflowEffect: {
//         stretch: -15, 
//         depth: 140, 
//       },
//     },
//     1024: {
//       slidesPerView: 3,
//       coverflowEffect: {
//         stretch: -20, 
//         depth: 200, 
//       },
//     },
//   },
// });


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
  