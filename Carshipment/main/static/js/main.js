  var autoSwiper = new Swiper(".promoSwiper", {
    spaceBetween: 30,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination3",
        clickable: true,
    },
    keyboard: true,
    loop: true,
    autoplay: {
        delay: 10000,
        pauseOnMouseEnter: true,
    },
});

var newsSwiper = new Swiper(".newsSwiper", {
    spaceBetween: 30,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination3",
        clickable: true,
    },
    mousewheel: false,
    keyboard: true,
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('h1');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 2;

    if (position < screenPosition) {
        element.classList.add('visible');
    }
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('.car-img');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 2;

    if (position < screenPosition) {
        element.classList.add('visible');
    }
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('.about');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 2;

    if (position < screenPosition) {
        element.classList.add('visible');
    }
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('.all_models');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 1.5;

    if (position < screenPosition) {
        element.classList.add('visible');
    }
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('.press_realises');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 2;

    if (position < screenPosition) {
        element.classList.add('visible');
    }
});

function copyLink() {
  let link = document.getElementById("share-link");
  link.select();
  document.execCommand("copy");
  alert("Ссылка скопирована!");
}