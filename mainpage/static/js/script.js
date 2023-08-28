rightArrow = document.querySelector('.first_arrow_right');
leftArrow = document.querySelector('.first_arrow_left');
rightBar = document.querySelector('.first_corousel_right_bar');
leftBar = document.querySelector('.first_corousel_left_bar');
rightArrow.addEventListener('click', ArrowHandler);
leftArrow.addEventListener('click', ArrowHandler);

activeSpan = document.querySelector('.tenth_active_window span:first-child');
activeSpan.addEventListener('click', spanHandler);
notActiveSpan = document.querySelector('.not_active_span')
notActiveSpan.addEventListener('click', spanHandler);


function ArrowHandler(e){
    e.preventDefault();
    leftBar.classList.toggle("closed_bar");
    rightBar.classList.toggle("active_bar");
}

function spanHandler(e){
    e.preventDefault();
    activeSpan.classList.toggle("not_active_span");
    notActiveSpan.classList.toggle("active_span");
}

