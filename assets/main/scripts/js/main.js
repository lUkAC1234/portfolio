document.addEventListener('DOMContentLoaded', function () {
    // Toggle Menu
    let menuIcon = document.querySelector("#menu-icon");
    let menu = document.querySelector(".header-links-container");
    
    menuIcon.addEventListener('click', () => {
        menu.classList.toggle('active');
    });

    // Scroll-triggered Header Activation
    var scrollTrigger = 60;
    window.onscroll = function() {
        document.getElementById("header").classList.toggle('active', window.scrollY >= scrollTrigger);
    };
});
