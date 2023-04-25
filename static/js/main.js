document.addEventListener('DOMContentLoaded', () => { 
    const onScrollHeader = () => { 
      const header = document.querySelector('.header')
      let prevScroll = window.pageYOffset
      let currentScroll
      window.addEventListener('scroll', () => { 
        currentScroll = window.pageYOffset
        const headerHidden = () => header.classList.contains('header_hidden')
        if (currentScroll > prevScroll && !headerHidden()) { 
          header.classList.add('header_hidden')
        }
        if (currentScroll < prevScroll && headerHidden()) {
          header.classList.remove('header_hidden')
        }
        prevScroll = currentScroll
      })
    }
    onScrollHeader()
  });   

var autoSwiper = new Swiper(".promoSwiper", {
    spaceBetween: 30,
    keyboard: true,
    loop: true,
    autoplay: {
        delay: 4000,
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
    mousewheel: true,
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
    var element = document.querySelector('#c1');
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
    var element = document.querySelector('#a1');
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