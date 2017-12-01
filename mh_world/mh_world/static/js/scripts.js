// Global JS and jquery

// MHWord Launch Countdown

// Set the date we're counting down to
var countDownDate = new Date("Jan 26, 2018 00:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now an the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("countdown-timer").innerHTML = days + "d " + hours +
  "h " + minutes + "m " + seconds + "s ";
  document.getElementById("countdown-text").innerHTML = "Until Monster Hunter World's Console Release!"

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown-timer").innerHTML = "RELEASED!";
  }
}, 1000);


// Auto-sticky navbar
$(document).ready(function () {

    var menu = $('.menu');
    var origOffsetY = menu.offset().top;

    function scroll() {
        if ($(window).scrollTop() >= origOffsetY) {
            $('.menu').addClass('navbar-fixed-top');
            $('.content').addClass('menu-padding');
        } else {
            $('.menu').removeClass('navbar-fixed-top');
            $('.content').removeClass('menu-padding');
        }
    }
    // Function call on scroll event
    document.onscroll = scroll;
});

//-----------------------



//-----------------------

// Main page accordion navigation
// Cycles between 'plus' and 'minus' glyphicons
$(document).ready(function(){
    // Add minus icon for collapse element which is open by default
    $(".collapse.in").each(function(){
      $(this).siblings(".panel-heading").find(".glyphicon").addClass("glyphicon-minus").removeClass("glyphicon-plus");
    });

    // Toggle plus minus icon on show hide of collapse element
    // and toggles the :hover styling at the same time.
    $(".collapse").on('show.bs.collapse', function(){
      $(this).parent().find(".glyphicon").removeClass("glyphicon-plus").addClass("glyphicon-minus");
      $(this).parent().find(".panel-heading").addClass("clicked")
    }).on('hide.bs.collapse', function(){
      $(this).parent().find(".glyphicon").removeClass("glyphicon-minus").addClass("glyphicon-plus");
      $(this).parent().find(".panel-heading").removeClass("clicked")
    });
});
