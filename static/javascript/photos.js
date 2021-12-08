//------------------------------Image Handler----------------------------------------------------//
function setOnclick(){
    images = document.getElementsByClassName("photo");
  Array.from(images).forEach(image=>{
    image.onclick = clickPhoto 
  })}
    
  setOnclick(clickPhoto)
  
    function clickPhoto(event){
      image = event.target;
      overlay = document.getElementsByClassName("photo_overlay")[0]
      console.log(overlay)
      overlay.style.visibility = "visible"
      overlay.getElementsByTagName("img")[0].src = image.src
      overlay.onclick = () =>{overlay.style.visibility = "hidden"}   
    } 
  