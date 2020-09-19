function handleSuccess(stream) {
  const video = document.querySelector('#video');
  video.srcObject = stream;
  $("#submit-btn").attr("style", "visibility:visible");
}

async function init(e) {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: {
            facingMode: 'environment',
        },
    });
    handleSuccess(stream);
  } catch (e) {
    alert("카메라를 찾을 수 없습니다.");
  }
}

function capture() {
    width = 350;
    height = 260;
    const canvas = document.querySelector('#canvas');
    const video = document.querySelector('#video');
    console.log(video.width);
    console.log(video.height);
    canvas.width = width;
    canvas.height = height;
    canvas.getContext('2d').drawImage(video, 0, 0, width, height);
    $('#image').val(canvas.toDataURL());
}

document.querySelector('#showVideo').addEventListener('click', e => init(e));
document.querySelector('#submit-btn').addEventListener('click', capture);