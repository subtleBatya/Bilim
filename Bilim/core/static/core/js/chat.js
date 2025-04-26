
const APP_ID = 'f761c240f7164bf293c1cb58eb3c5e8d'
const TOKEN = sessionStorage.getItem('token')
const CHANNEL = sessionStorage.getItem('room')
let UID = sessionStorage.getItem("UID")
let NAME = sessionStorage.getItem('username')

const client = AgoraRTC.createClient({mode:"rtc", codec:"vp8"})


let localTracks = []
let remoteUsers = {}
let screenTrack = null
let isScreenSharing = false

//  this function is for local stream user

let joinAndDisplayLocalStream = async () =>{

  client.on("user-published", handleUserJoin)

  client.on("user-left", handleUserLeft)
  
   UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
   
   localTracks = await AgoraRTC.createMicrophoneAndCameraTracks({
    microphoneId: null,
    cameraId: null,
    encoderConfig: "720p_1",
    audioConfig: {
      AEC: true,  // Acoustic Echo Cancellation
      AGC: true,  // Automatic Gain Control
      ANS: true   // Automatic Noise Suppression
    }
  });
  

   let player = ` <div class="main-video-container" id="user-container-${UID}">
      <center><h5 style="color:white">${NAME}</h5></center>
      <div class="main-video" id="main-video-${UID}">
      </div>`


    document.getElementById("video-sections").insertAdjacentHTML("beforeend", player)
    localTracks[1].play(`main-video-${UID}`)
   
    
    
    await client.publish([localTracks[0], localTracks[1]])
}




let handleUserJoin = async (user, mediaType) => {
  remoteUsers[user.uid] = user

  await client.subscribe(user, mediaType)
  if(mediaType == 'video'){
    let player  = document.getElementById(`user-container-${user.uid}`)

    if(player != null){
      player.remove()
    }

    let response = await fetch(`/chat/get_username_by_uid/?uid=${user.uid}`);
    let data = await response.json();
    let username = data.username || user.uid;
    player = ` <div class="main-video-container" id="user-container-${user.uid}">
      <center><h5 style="color:white">${username}</h5></center>
      <div class="main-video" id="main-video-${user.uid}">
      </div>
      `
      document.getElementById("video-sections").insertAdjacentHTML("beforeend", player)
      
      user.videoTrack.play(`main-video-${user.uid}`)

  }

  if (mediaType == 'audio') {
    user.audioTrack.play()
  }
}



let handleUserLeft = async (user) => {

  let delete_user = await fetch(`/chat/quit_user/?room_name=${CHANNEL}?uid=${user.uid}`)
  let data = await delete_user.json()
  console.log(data.result)
  delete remoteUsers[user.uid]
  document.getElementById(`user-container-${user.uid}`).remove()

}



let leaveAndRemoveLocalStream = async () =>{
  for (let i=0; localTracks.length > i; i++){
    localTracks[i].stop()
    localTracks[i].close()
  }

  await client.leave()

  window.open("/", "_self")
}


let toggleCamera = async (e) =>{
  if (localTracks[1].muted){
    await localTracks[1].setMuted(false)
    e.target.style.backgroundColor = "#fff"
    e.target.style.color = "#000"
  }
  else {
    await localTracks[1].setMuted(true)
    e.target.style.backgroundColor = "red"
    e.target.style.color = "#fff"
  }
}


let toggleMicrophone = async (e) =>{
  if (localTracks[0].muted){
    await localTracks[0].setMuted(false)
    e.target.style.backgroundColor = "#fff"
    e.target.style.color = "#000"
  }
  else {
    await localTracks[0].setMuted(true)
    e.target.style.backgroundColor = "red"
    e.target.style.color = "#fff"
  }
}


let toggleScreenShare = async (e) => {
  if (!isScreenSharing) {
    // Stop camera video
    await localTracks[1].stop()
    await localTracks[1].close()

    // Start screen sharing
    screenTrack = await AgoraRTC.createScreenVideoTrack()

    // Replace camera with screen
    await client.unpublish([localTracks[1]])
    await client.publish([screenTrack])

    screenTrack.play(`main-video-${UID}`)

    isScreenSharing = true

    e.target.style.backgroundColor = "red"
  } else {
    // Stop screen share
    await screenTrack.stop()
    await screenTrack.close()

    // Restart camera video
    localTracks[1] = await AgoraRTC.createCameraVideoTrack()
    await client.unpublish([screenTrack])
    await client.publish([localTracks[1]])

    localTracks[1].play(`main-video-${UID}`)

    isScreenSharing = false

    e.target.style.backgroundColor = "#fff"
  }
}

joinAndDisplayLocalStream()


let leaveBtn = document.getElementById("leave-btn")
leaveBtn.addEventListener("click", leaveAndRemoveLocalStream)


let videoBtn = document.getElementById("video-btn")
videoBtn.addEventListener('click', toggleCamera)

let audioBtn = document.getElementById("mic-btn")
audioBtn.addEventListener("click", toggleMicrophone)

let displayScreenVideo = document.getElementById("display-btn");
displayScreenVideo.addEventListener("click", toggleScreenShare);
