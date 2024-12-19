// VIDEO player
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