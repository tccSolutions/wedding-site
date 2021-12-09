





mobile_nav_icon = document.getElementsByClassName('mobile-nav-icon')[0]
registry_field =document.getElementsByClassName("registry")[0]
mobile_dropdown = document.getElementsByClassName("mobile-dropdown")[0]
mobile_nav_icon.onclick = function (){
 if(mobile_dropdown.style.visibility === "visible") {
  mobile_dropdown.style.visibility = "hidden";
 }else{
  mobile_dropdown.style.visibility = "visible";
 }
}