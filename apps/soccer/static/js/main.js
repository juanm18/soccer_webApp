$(document).ready(function() {
  var  mn = $(".main-nav");
  mns = "main-nav-scrolled";
  $(window).scroll(function() {
    if( $(this).scrollTop() > 5 ) {
      mn.addClass(mns);
    }
    else {
      mn.removeClass(mns);
    }
  });
});
