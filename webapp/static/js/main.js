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
    $(".dropdown-menu").hide();
    $(`[data-category='${listLinks}']`).show();
  });

  // Закрыть список ссылок при клике на Esc
  document.addEventListener("keyup", closeModal);
  function closeModal(event) {
    if (event.key === "Escape" || event.type === "click") {
      $(".dropdown-menu").hide();
    }
  }

  // Закрыть список ссылок при клике вне области ссылок
  $(document).mouseup(function (e) {
    var container = $(".dropdown-menu");
    if (container.has(e.target).length === 0) {
      container.hide();
    }
  });

  $('[data-btn="toTop"]').hide();

  // появление/затухание кнопки #back-top
  $(function () {
    $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {
        $('[data-btn="toTop"]').fadeIn();
      } else {
        $('[data-btn="toTop"]').fadeOut();
      }
    });

    // при клике на ссылку плавно поднимаемся вверх
    $('[data-btn="toTop"]').click(function () {
      $("body,html").animate(
        {
          scrollTop: 0,
        },
        1000
      );
      return false;
    });
  });
});
