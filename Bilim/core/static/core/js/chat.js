
const APP_ID = 'f761c240f7164bf293c1cb58eb3c5e8d'
const TOKEN = sessionStorage.getItem('token')
const CHANNEL = sessionStorage.getItem('room')
let UID = sessionStorage.getItem("UID")
let NAME = sessionStorage.getItem('username')

const client = AgoraRTC.createClient({mode:"rtc", codec:"vp8"})


let localTracks = []
let remoteUsers = {}


//  this function is for local stream user

let joinAndDisplayLocalStream = async () =>{

  client.on("user-published", handleUserJoin)

  client.on("user-left", handleUserLeft)
  
   UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
   
   localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

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
    player = ` <div class="main-video-container" id="user-container-${user.uid}">
      <center><h5 style="color:white">${user.uid}</h5></center>
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
joinAndDisplayLocalStream()


let leaveBtn = document.getElementById("leave-btn")
leaveBtn.addEventListener("click", leaveAndRemoveLocalStream)


let videoBtn = document.getElementById("video-btn")
videoBtn.addEventListener('click', toggleCamera)

let audioBtn = document.getElementById("mic-btn")
audioBtn.addEventListener("click", toggleMicrophone)