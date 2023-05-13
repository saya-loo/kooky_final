document.addEventListener('DOMContentLoaded', function() {
  var paymentButton = document.getElementById('payment-button');
  var paymentForm = document.getElementById('payment-form');

  paymentButton.addEventListener('click', function() {
    paymentForm.style.display = 'block';
  });
});

  
var deadline = new Date("may 27, 2023 00:00:00").getTime();
var x = setInterval(function() {
var now = new Date().getTime();
var t = deadline - now;
var days = Math.floor(t / (1000 * 60 * 60 * 24)); /*since in milliseconds all time measuremenents are divided by 1000*/
var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((t % (1000 * 60)) / 1000);
document.getElementById("day").innerHTML =days ;
document.getElementById("hour").innerHTML =hours;
document.getElementById("minute").innerHTML = minutes; 
document.getElementById("second").innerHTML =seconds; 
}, 0); /*delay for 0 millisec*/


function changeLocation(){
this.window.location = "C:\\Users\\User\\OneDrive\\Desktop\\frontEnd\\Final\\Final\\form\\index.html";
}