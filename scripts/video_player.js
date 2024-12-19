// VIDEO player

document.addEventListener("contextmenu", (event) => {
  if (event.target.tagName === "VIDEO") {
    event.preventDefault();
  }
});


document.addEventListener("DOMContentLoaded", () => {
    const player = videojs('my-video', {
      autoplay: false, 
      controls: true, 
      responsive: true,
      fluid: true, 
      playbackRates: [0.5, 1, 1.5, 2],
    });
  
    
    player.on('play', () => {
      console.log('Video started playing!');
    });
  
    player.on('pause', () => {
      console.log('Video paused.');
    });
  
    player.on('ended', () => {
      console.log('Video ended.');
    });
  
    
    document.getElementById("change-video-btn").addEventListener("click", () => {
      player.src({
        src: "path-to-another-video.mp4",
        type: "video/mp4",
      });
      player.play();
    });
  });

  // LIKES COUNT

  document.addEventListener("DOMContentLoaded", () => {
    let likeCount = 0;
    let dislikeCount = 0;
  
    const likeBtn = document.getElementById("like-btn");
    const dislikeBtn = document.getElementById("dislike-btn");
    const likeCountSpan = document.getElementById("like-count");
    const dislikeCountSpan = document.getElementById("dislike-count");
  
    likeBtn.addEventListener("click", () => {
      likeCount++;
      likeCountSpan.textContent = likeCount;
    });
  
    dislikeBtn.addEventListener("click", () => {
      dislikeCount++;
      dislikeCountSpan.textContent = dislikeCount;
    });
  });
  

  //VIEW's COUNT