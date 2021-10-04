$(document).ready(function () {
  // Кнопка в шапке
  var menuButton = document.querySelector(".menu-button");
  menuButton.addEventListener("click", function () {
    document
      .querySelector(".nav--mobile--hidden")
      .classList.toggle("nav--mobile--visible");
    // document.querySelector("body").classList.toggle("body-overflow-hidden");
  });

  $(window).scroll(function () {
    $("header").toggleClass("scroll", $(this).scrollTop() > 100);
  });
});
