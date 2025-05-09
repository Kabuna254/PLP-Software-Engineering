// Store and retrieve user preferences using localStorage
function savePreference(key, value) {
    localStorage.setItem(key, value);
}

function getPreference(key) {
    return localStorage.getItem(key);
}

// Apply saved preferences on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = getPreference('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
});

// Toggle theme and save preference
const themeToggleButton = document.getElementById('theme-toggle');
themeToggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    const newTheme = document.body.classList.contains('dark-theme') ? 'dark' : 'light';
    savePreference('theme', newTheme);
});

// Trigger animation on button click
const animateButton = document.getElementById('animate-button');
animateButton.addEventListener('click', () => {
    const box = document.querySelector('.box');
    box.classList.add('animate');

    // Remove the animation class after it completes
    setTimeout(() => {
        box.classList.remove('animate');
    }, 1000); // Match the duration of the animation
});

// Trigger bounce animation dynamically
const bounceButton = document.getElementById('bounce-button');
bounceButton.addEventListener('click', () => {
    const box = document.querySelector('.box');
    box.classList.add('bounce');

    // Remove the bounce class after it completes
    setTimeout(() => {
        box.classList.remove('bounce');
    }, 1000); // Match the duration of the animation
});

// Trigger bounce animation for the image
const imageBounceButton = document.getElementById('image-bounce-button');
imageBounceButton.addEventListener('click', () => {
    const image = document.getElementById('animated-image');
    image.classList.add('bounce-image');

    // Remove the animation class after it completes
    setTimeout(() => {
        image.classList.remove('bounce-image');
    }, 1000); // Match the duration of the animation
});