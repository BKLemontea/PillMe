function handleSuccess(stream) {
  const video = document.querySelector('#video');
  $('#video').attr("class", "duration-300 rounded-lg w-56 h-56 md:w-64 md:h-64");
  video.srcObject = stream;
}

async function init(e) {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: {
            width: { min: 720, ideal: 720, max: 720 },
            height: { min: 720, ideal: 720, max: 720 },
            facingMode: 'environment',
        },
    });
    handleSuccess(stream);
  } catch (e) {
    alert("카메라를 찾을 수 없습니다.");
  }
}

function capture() {
    const canvas = document.querySelector('#canvas');
    const video = document.querySelector('#video');
    canvas.getContext('2d').drawImage(video, 0, 0);
}

document.querySelector('#showVideo').addEventListener('click', e => init(e));
document.querySelector('#submit-btn').addEventListener('click', capture);