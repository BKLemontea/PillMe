var overlay = document.querySelector('.modal-overlay');
overlay.addEventListener('click', toggleModal);
    
var closemodal = document.querySelectorAll('.modal-close');
for (var i = 0; i < closemodal.length; i++) {
  closemodal[i].addEventListener('click', toggleModal);
}
    
document.onkeydown = function(evt) {
  evt = evt || window.event;
  var isEscape = false;
  if ("key" in evt) {
    isEscape = (evt.key === "Escape" || evt.key === "Esc");
  } else {
    isEscape = (evt.keyCode === 27);
  }
  if (isEscape && document.body.classList.contains('modal-active')) {
    toggleModal();
  }
};
    
function toggleModal (stream_a) {
  const video = document.querySelector('#video');
  const stream = video.srcObject;
  if(stream){
    const tracks = stream.getTracks();
    tracks.forEach(function(track) {
      track.stop();
    });
    video.srcObject = null;
  } else{
    const video = document.querySelector('#video');
    video.srcObject = stream_a;
  }
  
  const modal = document.querySelector('.modal');
  modal.classList.toggle('opacity-0');
  modal.classList.toggle('pointer-events-none');
}

async function init(e) {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: {
            facingMode: 'environment',
        },
    });
    toggleModal(stream)
  } catch (e) {
    alert("카메라를 찾을 수 없습니다.");
  }
}

function capture() {
    width = 350;
    height = 260;
    if ($( window ).width() < $( window ).height()){
      width = 260;
      height = 350;
    }
    const canvas = document.querySelector('#canvas');
    const video = document.querySelector('#video');
    canvas.width = width;
    canvas.height = height;
    canvas.getContext('2d').drawImage(video, 0, 0, width, height);
    $('#image').val(canvas.toDataURL());
}

document.querySelector('#showVideo').addEventListener('click', e => init(e));
document.querySelector('#submit-btn').addEventListener('click', capture);