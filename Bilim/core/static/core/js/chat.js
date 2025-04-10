
// for chatting 
function sendMessage(e) {
    e.preventDefault();
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    if (message !== '') {
      const messagesContainer = document.getElementById('messages');

      const msgDiv = document.createElement('div');
      msgDiv.classList.add('message');

      const avatar = document.createElement('img');
      avatar.src = 'image.png';

      const content = document.createElement('div');
      content.classList.add('message-content');

      const name = document.createElement('strong');
      name.textContent = 'Пользователь';

      const text = document.createElement('span');
      text.textContent = message;

      content.appendChild(name);
      content.appendChild(text);

      msgDiv.appendChild(avatar);
      msgDiv.appendChild(content);

      messagesContainer.appendChild(msgDiv);

      input.value = '';
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
  }



//   for video



const APP_ID = 'f761c240f7164bf293c1cb58eb3c5e8d'
const TOKEN = sessionStorage.getItem('token')
const CHANNEL = sessionStorage.getItem('room')
let UID = sessionStorage.getItem("UID")
let NAME = sessionStorage.getItem('username')



const client = AgoraRTC.createClient({mode:"rtc", codec:"vp8"})


let localTracks = []
let remoteUsers = {}


let joinAndDisplayLocalStream = async () =>{
   UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
   
   localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

   let player = ` <<div class="main-video-container" id="user-container-${UID}">
      <video class="main-video-${UID}" autoplay muted loop>
        <source src="main-video.mp4" type="video/mp4">
        Ваш браузер не поддерживает видео.
      </video>
      <div class="video-controls">
        <button onclick="alert('Микрофон отключен')">🎙️ Микрофон</button>
        <button onclick="alert('Звук отключен')">🔈 Звук</button>
        <button onclick="alert('Видео отключено')">📷 Видео</button>
        <button onclick="alert('Выбор экрана')">🖥️ Поделиться</button>
      </div>`


    document.getElementById("video-section").insertAdjacentHTML("beforeend", player)

    localTracks[1].play(`main-video-${UID}`)
    
    await client.publish([localTracks[0], localTracks[1]])
}


joinAndDisplayLocalStream()