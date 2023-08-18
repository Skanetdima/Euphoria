rightArrow = document.querySelector('.first_arrow_right');
leftArrow = document.querySelector('.first_arrow_left');
rightBar = document.querySelector('.first_corousel_right_bar');
leftBar = document.querySelector('.first_corousel_left_bar');
rightArrow.addEventListener('click', ArrowHandler);
leftArrow.addEventListener('click', ArrowHandler);

function ArrowHandler(e){
    e.preventDefault();
    leftBar.classList.toggle("closed_bar");
    rightBar.classList.toggle("active_bar");
}

