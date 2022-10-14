window.onload = function () {
  document.getElementById("detect").onclick = function () {
    myFunction();
  };
};

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}


function myFunction() {
  $.ajax({
    url: "/detect",
    type: "POST",
    contentType: "application/json",
    success: function (response) {
      if (response.redirect) {
        window.location.href = response.redirect;
      }
    },
  });
}

$(function () {
  var twoToneButton = document.querySelector(".twoToneButton");

  twoToneButton.addEventListener(
    "click",
    function () {
      twoToneButton.innerHTML = "Processing";
      twoToneButton.classList.add("spinning");
    },
    false
  );
});

$(document).on("change", ".file-input", function () {
  var fileName = $(this).val().split("\\").pop();
  document.getElementById("file_name").innerHTML = fileName;
});

$(function () {
  $("#upload-file-btn").click(function () {
    var form_data = new FormData($("#upload-file")[0]);
    $.ajax({
      type: "POST",
      url: "/upload",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      success: function (data) {
        document.getElementById("detect").style.visibility = "visible";
        document.getElementById("file_name").innerHTML = "";
        const video = document.createElement("video");
        video.src = "../static/input.mp4";
        video.type = "video/mp4";
        video.autoplay = false;
        video.controls = true;
        video.muted = true;
        video.height = 240;
        video.width = 320;
        const box = document.getElementById("preview");
        box.appendChild(video);
      },
    });
  });
});
