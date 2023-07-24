window.addEventListener('load', function() {
    let header = document.querySelector('header');

    let menu = document.querySelector('.menu');
    let logo = document.querySelector('.logo');
    let phone = document.querySelector('.phone');

    let imgList = [menu, logo, phone];
  
    if (window.pageYOffset > 0) {
      header.style.backgroundColor = 'white';
    } else {
      header.style.backgroundColor = 'transparent';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'invert(100%)';}
    }
});
  
  
document.addEventListener('scroll', function() {
    let header = document.querySelector('header'); // Замените 'header' на селектор вашего хэдера
    
    let menu = document.querySelector('.menu');
    let logo = document.querySelector('.logo');
    let phone = document.querySelector('.phone');

    let imgList = [menu, logo, phone];

    if (window.pageYOffset > 0) {
      header.style.backgroundColor = 'white';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'none';} // Замените цвет на нужный вам с прозрачностью
    } else {
      header.style.backgroundColor = 'transparent';
      for (let i = 0; i < 3; i++) {imgList[i].querySelector('img').style.filter = 'invert(100%)';}
    }
});