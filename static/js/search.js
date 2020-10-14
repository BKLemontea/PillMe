var overlay = document.querySelector('.modal-search-overlay');
overlay.addEventListener('click', toggleModal_search);
    
var closemodal = document.querySelectorAll('.modal-search-close');
for (var i = 0; i < closemodal.length; i++) {
  closemodal[i].addEventListener('click', toggleModal_search);
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

function toggleModal_search () {
  const modal = document.querySelector('.modal-search');
  modal.classList.toggle('opacity-0');
  modal.classList.toggle('pointer-events-none');
}

var openmodal = document.querySelectorAll('#showSearch');
for (var i = 0; i < openmodal.length; i++) {
  openmodal[i].addEventListener('click', toggleModal_search);
}

function check(){
  var name = document.getElementById("name");
  var mark = document.getElementById("mark");
  var shape = document.getElementById("shape");
  var color = document.getElementById("color");
  if(!name.value && !mark.value && !shape.value && !color.value){
    alert("하나 이상의 정보를 입력해주세요.");
    name.focus();
  }else{
    $("#btn").click();
  }
}
document.querySelector('#submit').addEventListener('click', check);