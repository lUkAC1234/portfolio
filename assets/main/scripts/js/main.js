document.addEventListener('DOMContentLoaded', function () {
    var audioPlayer = document.getElementById('audioPlayer');
    var audioPlayButton = document.getElementById('audioPlay');

    updateVisualState();

    audioPlayer.addEventListener('playing', updateVisualState);
    audioPlayer.addEventListener('pause', updateVisualState);

    function updateVisualState() {
        if (audioPlayer.paused) {
            audioPlayButton.classList.remove('active');
        } else {
            audioPlayButton.classList.add('active');
        }
    }

    function toggleAudio() {
        if (audioPlayer.paused) {
            audioPlayer.play();
        } else {
            audioPlayer.pause();
        }
    }

    audioPlayButton.addEventListener('click', toggleAudio);
});

let menuIcon = document.querySelector("#menu-icon");
let menu = document.querySelector(".header-links-container")
menuIcon.addEventListener('click', () => {
    if (menu.classList.contains('active')) {
        menu.classList.remove('active');
    } else {
        menu.classList.add('active');
    }
})

// HEADER
var scrollTrigger = 60;
window.onscroll = function() {
    if (window.scrollY >= scrollTrigger) {
        document.getElementById("header").classList.add('active');
    } else {
        document.getElementById("header").classList.remove('active');
    }
};