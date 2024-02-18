let header = document.querySelector('header'); // Замените 'header' на селектор вашего хэдера
    
let menu = document.querySelector('.menu');
let logo = document.querySelector('.logo');
let phone = document.querySelector('.phone');

let imgList = [menu, logo, phone];


window.addEventListener('load', function() {
    if (window.pageYOffset > 0) {
      header.style.backgroundColor = 'white';
    } else {
      header.style.backgroundColor = 'transparent';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'invert(100%)';}
    }
});
  
  
document.addEventListener('scroll', function() {
    if (window.pageYOffset > 0) {
      header.style.backgroundColor = 'white';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'none';} // Замените цвет на нужный вам с прозрачностью
    } else {
      header.style.backgroundColor = 'transparent';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'invert(100%)';}
    }
});


function onmouse() {
  let header = document.querySelector('header');
  if (window.pageYOffset == 0) {
      header.style.backgroundColor = 'white';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'invert(0%)'};
}}


function outmouse() {
  let header = document.querySelector('header');
  if (window.pageYOffset == 0) {
      header.style.backgroundColor = 'transparent';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'invert(100%)'};
}}


const smoothLinks = document.querySelectorAll("a[href^='#']");
for (let smoothLink of smoothLinks) {
    smoothLink.addEventListener("click", function (e) {
        e.preventDefault();
        const id = smoothLink.getAttribute("href");

        document.querySelector(id).scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });
};