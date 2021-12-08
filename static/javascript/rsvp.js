document.body.style.backgroundImage = "url(../static/images/us.png)";
document.body.style.backgroundRepeat= "no-repeat"
document.body.style.backgroundSize= "cover";
document.body.style.backgroundPosition = "center"
document.body.style.backgroundAttachment = "fixed"


let rsvp_link = document.getElementById("rsvp_maker")
let rsvp_form = document.getElementsByClassName("rsvp_container_form")
let rsvp_exit_btn = document.getElementById("rsvp_exit_btn")

rsvp_link.onclick = function(){
    rsvp_form[0].classList.add("rsvp_container_form_click")
}



rsvp_exit_btn.onclick = function(){
    rsvp_form[0].classList.remove("rsvp_container_form_click")
}