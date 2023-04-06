var autoSwiper = new Swiper(".autoSwiper", {
    spaceBetween: 30,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination1",
    },
    mousewheel: true,
    keyboard: true,
});

var infoSwiper = new Swiper(".infoSwiper", {
    spaceBetween: 30,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination2",
    },
    mousewheel: true,
    keyboard: true,
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
    mousewheel: true,
    keyboard: true,
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('.models');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 2;

    if (position < screenPosition) {
        element.classList.add('visible');
    }
});

window.addEventListener('scroll', function() {
    var element = document.querySelector('.carshipment');
    var position = element.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 2;

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