<script>
import js2py;
window.alert('you have register successfully');
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName('mySlides');
  
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
 
  slides[slideIndex-1].style.display = 'block';  
  
  setTimeout(showSlides, 4000); 
}

function openForm() {
  document.getElementById('myForm').style.display = 'block';
  document.getElementById('mySlides fade').style.filter='blur(8px)';
  
}
function closeForm() {
  document.getElementById('myForm').style.display = 'none';
}


var modal = document.getElementById('id01');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}


</script>