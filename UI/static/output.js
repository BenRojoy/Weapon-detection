var severity=0;
var Color =["#FFFFFF","#FFA500","#FF0000"];

window.onload = loadSeverity;

function loadSeverity() {
    $.ajax({
        type: "GET",
        url: "/severity",
        success: function (data) {
          severity=parseInt(data);
          for(i=0;i<severity;i++)
          {
            const star = document.createElement("span");
            star.classList.add('fa','fa-star','checked');
            document.getElementById("severityRating").appendChild(star);
          }
          for(j=i;j<2;j++)
          {
            const star = document.createElement("span");
            star.classList.add('fa','fa-star','unchecked');
            document.getElementById("severityRating").appendChild(star);
          }
          document.getElementById("home2").style.borderColor=Color[severity];
          var p1 =document.getElementById("p1").value;
          var p2 =document.getElementById("p2").value;
          var p3 =document.getElementById("p3").value;
          var p4 =document.getElementById("p4").value;
          if(p1<60)
          {
            document.getElementById("p1").style.color="#1B1C25";
          }
          if(p2<60)
          {
            document.getElementById("p2").style.color="#1B1C25";
          }
          if(p3<60)
          {
            document.getElementById("p3").style.color="#1B1C25";
          }
          if(p4<60)
          {
            document.getElementById("p4").style.color="#1B1C25";
          }
        },
      });
}


function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more <span><i class='fas fa-angle-down'></i></span>"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less <span><i class='fas fa-angle-up'></i></span>"; 
    moreText.style.display = "inline";
  }
}

function onClick(element) {
  
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
}