$(document).ready(function () {
  // Кнопка в шапке
  var menuButton = document.querySelector(".menu-button");
  menuButton.addEventListener("click", function () {
    document
      .querySelector(".nav--mobile--hidden")
      .classList.toggle("nav--mobile--visible");
    // document.querySelector("body").classList.toggle("body-overflow-hidden");
  });

  // Тень для header при скролле
  $(window).scroll(function () {
    $("header").toggleClass("scroll", $(this).scrollTop() > 100);
  });

  // Скрывать/показывать список ссылок при клике на заголовок
  $(".nav__link").on("click", function () {
    var listLinks = $(this).data("category");
    $(".nav__link__list").hide();
    $(`[data-category='${listLinks}']`).show();
  });

  // Закрыть список ссылок при клике на Esc
  document.addEventListener("keyup", closeModal);
  function closeModal(event) {
    if (event.key === "Escape" || event.type === "click") {
      $(".nav__link__list").hide();
    }
  }

  // Закрыть список ссылок при клике вне области ссылок
  $(document).mouseup(function (e) {
    var container = $(".nav__link__list");
    if (container.has(e.target).length === 0) {
      container.hide();
    }
  });
});
