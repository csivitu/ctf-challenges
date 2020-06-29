$(document).ready(function() {
	// Closes the sidebar menu
  $(".menu-toggle").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
    $(".menu-toggle > .fa-bars, .menu-toggle > .fa-times").toggleClass("fa-bars fa-times");
    $(this).toggleClass("active");
  });
  // Smoothscroll script
  $(".smooth-scroll").click(function(e) {
    e.preventDefault();
    var dis = $(this),
      target = dis.attr("href"),
      offset = parseInt($(target).offset().top),
      header = $(".sidebar-nav");
    dis.addClass("active").parent().siblings().find(".smooth-scroll").removeClass("active");
    $('html,body').stop().animate({ scrollTop: offset }, 200);
  });
  // Closes responsive menu when a scroll trigger link is clicked
  $('#sidebar-wrapper').click(function() {
    $("#sidebar-wrapper").removeClass("active");
    $(".menu-toggle").removeClass("active");
    $(".menu-toggle > .fa-bars, .menu-toggle > .fa-times").toggleClass("fa-bars fa-times");
  });
  if ($(window).width() > 991) {
    $(window).on("load", function (e) {
      $("body").addClass("active");
    })
  }
});

