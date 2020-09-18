var sel_file;

$(document).ready(function() {
    $("#camera").on("change", handleImgFileSelect);
});

function handleImgFileSelect(e){
    var files = e.target.files;
    var filesArr = Array.prototype.slice.call(files);

    filesArr.forEach(function(f) {
        if(!f.type.match("image.*")) {
            alert("이미지 파일만 가능합니다.");
            return;
        }

        sel_file = f;

        var reader = new FileReader();
        reader.onload = function(e) {
            $("#img").attr("src", e.target.result);
            $("#img").attr("class", "duration-300 rounded-lg w-56 h-56 md:w-64 md:h-64 border-2");
        }
        reader.readAsDataURL(f);
    });
}