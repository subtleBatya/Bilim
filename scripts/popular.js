


console.log(typeof Swiper); // Should return "function"

document.addEventListener('DOMContentLoaded', () => {
const swiper = new Swiper('.swiper-container', {
    slidesPerView: 3,
    spaceBetween: -10,
    centeredSlides: true,
    loop: true, // Enables infinite scrolling
    grabCursor: true, // Changes the cursor to a grab icon
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });
  
  swiper.on('slideChange', () => {
    document.querySelectorAll('.swiper-slide').forEach((slide, index) => {
      if (index === swiper.activeIndex) {
        slide.querySelector('img').style.transform = 'scale(1.2) translateX(0)';
      } else {
        slide.querySelector('img').style.transform = 'scale(0.9) translateX(10px)';
      }
    });
  });
  
});





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
  