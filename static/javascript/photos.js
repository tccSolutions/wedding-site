//------------------------------Image Handler----------------------------------------------------//

let images = document.getElementsByClassName("photo")
let overlay = document.getElementsByClassName("photo_overlay")[0]
let carItems = document.getElementsByClassName("carousel-item")

Array.from(images).forEach(function(element){
    element.onclick = function (event){
      Array.from(carItems).forEach(function(carItem){
        if (carItem.childNodes[1].src === event.target.childNodes[1].src) {
          carItem.classList.add('active')
        }
      })
      overlay.style.visibility = "visible"
    }
  }
)

document.getElementById("photo_exit_btn").onclick=function (){
      Array.from(carItems).forEach(function(carItem){
        carItem.classList.remove("active")
      })
      overlay.style.visibility = "hidden"
    }
