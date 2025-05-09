// Button Click Feedback
const sendBtn = document.querySelector("form button");
sendBtn.addEventListener("click", () => {
    sendBtn.textContent = "Sent!";
    sendBtn.style.backgroundColor = "#4CAF50";
    alert("Message Sent Successfully!");
});

// Hover Effect for Navigation Links
document.querySelectorAll("nav ul li a").forEach(link => {
    link.addEventListener("mouseover", () => {
        link.classList.add("hovered-link");
    });
    link.addEventListener("mouseout", () => {
        link.classList.remove("hovered-link");
    });
});

// Keypress Detection
document.addEventListener("keydown", (e) => {
    console.log(`Key Pressed: ${e.key}`); // Logs to the console
    const keyDisplay = document.getElementById('key-display');
    if (keyDisplay) {
        keyDisplay.textContent = `Key Pressed: ${e.key}`; // Display on the webpage
    }
});

// Double-Click Easter Egg
document.querySelector("h1").addEventListener("dblclick", () => {
    alert("Secret unlocked! You double-clicked the header!");
});

// Simple Slideshow
const galleryImages = ["Images/pic1.jpg", "Images/pic2.jpg", "Images/pic3.jpg"];
let slideIndex = 0;
const galleryImg = document.querySelector(".gallery-img");

if (galleryImg) {
    setInterval(() => {
        slideIndex = (slideIndex + 1) % galleryImages.length;
        galleryImg.src = galleryImages[slideIndex];
    }, 3000);
}

// Real-time Email Validation
const emailField = document.querySelector('input[type="email"]');
if (emailField) {
    emailField.addEventListener("input", () => {
        emailField.style.borderColor = emailField.validity.valid ? "green" : "red";
    });
}

// Real-time feedback for the "Your Name" field
const nameInput = document.getElementById('name-input');
nameInput.addEventListener('input', () => {
    if (nameInput.value.trim().length < 3) {
        nameInput.style.borderColor = 'red';
        nameInput.setCustomValidity('Name must be at least 3 characters long.');
    } else {
        nameInput.style.borderColor = 'green';
        nameInput.setCustomValidity('');
    }
});

// Real-time feedback for the "Your Email" field
const emailInput = document.getElementById('email-input');
emailInput.addEventListener('input', () => {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]*$/; // Regex for partial email validation
    if (emailPattern.test(emailInput.value)) {
        emailInput.style.borderColor = 'green'; // Valid format so far
        emailInput.setCustomValidity('');
    } else {
        emailInput.style.borderColor = 'red'; // Invalid format
        emailInput.setCustomValidity('Please enter a valid email address.');
    }
});

// Real-time feedback for the "Your Message" field
const messageInput = document.getElementById('message-input');
messageInput.addEventListener('input', () => {
    if (messageInput.value.trim().length < 10) {
        messageInput.style.borderColor = 'red';
        messageInput.setCustomValidity('Message must be at least 10 characters long.');
    } else {
        messageInput.style.borderColor = 'green';
        messageInput.setCustomValidity('');
    }
});

// Example: Change text on clicking the About section
document.getElementById('about-text').addEventListener('click', () => {
    alert('You clicked on the About Me section!');
});

// Example: Highlight the resume download link on hover
document.getElementById('download-resume').addEventListener('mouseover', () => {
    document.getElementById('download-resume').style.color = 'red';
});
document.getElementById('download-resume').addEventListener('mouseout', () => {
    document.getElementById('download-resume').style.color = '';
});

// Prevent form submission from reloading the page
const contactForm = document.getElementById('contact-form');
contactForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent page reload
    const nameInput = document.getElementById('name-input');
    const emailInput = document.getElementById('email-input');
    const messageInput = document.getElementById('message-input');
    const sendBtn = document.getElementById('submit-button'); // Target the submit button

    // Update the button text to "Sent!"
    sendBtn.textContent = "Sent!";
    sendBtn.style.backgroundColor = "#4CAF50"; // Change button color to green
    sendBtn.disabled = true; // Disable the button to prevent multiple submissions

    // Clear the form fields
    nameInput.value = '';
    emailInput.value = '';
    messageInput.value = '';

    // Reset the textboxes' border colors
    nameInput.style.borderColor = '';
    emailInput.style.borderColor = '';
    messageInput.style.borderColor = '';

    // Optionally, reset the button after a delay
    setTimeout(() => {
        sendBtn.textContent = "Send Message";
        sendBtn.style.backgroundColor = ""; // Reset to default color
        sendBtn.disabled = false; // Re-enable the button
    }, 3000); // Reset after 3 seconds
});

// Tabs Functionality
document.querySelectorAll('.tab-button').forEach(button => {
    button.addEventListener('click', () => {
        const tabId = button.getAttribute('data-tab');

        // Remove active class from all buttons and panels
        document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));

        // Add active class to the clicked button and corresponding panel
        button.classList.add('active');
        document.getElementById(tabId).classList.add('active');
    });
});
