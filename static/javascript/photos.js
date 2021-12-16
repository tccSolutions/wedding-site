//------------------------------Image Handler----------------------------------------------------//

images = document.getElementsByClassName("photo")
car_items = document.getElementsByClassName("carousel-item")
console.log(images)
Array.from(images).forEach(function(element){
  element.onclick = function (event){
    console.log(event.target)
    overlay = document.getElementsByClassName("photo_overlay")[0]
    overlay.style.visibility = "visible"
    car_items[0].classList.add("active")
    document.getElementById("photo_exit_btn").onclick=function (){
      overlay.style.visibility = "hidden"
    }
  }
})

