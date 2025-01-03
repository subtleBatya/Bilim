document.addEventListener("DOMContentLoaded", () => {
    const images = document.querySelectorAll(".slider-image");
    const prevBtn = document.querySelector(".slider-btn.prev");
    const nextBtn = document.querySelector(".slider-btn.next");
  
    let currentIndex = 0;
  
    const updateSlider = () => {
      images.forEach((img, index) => {
        img.classList.remove("active", "left", "right");
  
        if (index === currentIndex) {
          img.classList.add("active");
        } else if (index === (currentIndex - 1 + images.length) % images.length) {
          img.classList.add("left");
        } else if (index === (currentIndex + 1) % images.length) {
          img.classList.add("right");
        }
      });
    };
  
    prevBtn.addEventListener("click", () => {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      updateSlider();
    });
  
    nextBtn.addEventListener("click", () => {
      currentIndex = (currentIndex + 1) % images.length;
      updateSlider();
    });
  
    updateSlider(); 
  });
  