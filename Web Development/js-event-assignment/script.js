document.addEventListener("DOMContentLoaded", () => {
    // 1. Event Handling
    // Button click: Change text and background color on click
    const changeButton = document.getElementById("changeButton");
    changeButton.addEventListener("click", () => {
      changeButton.innerText = "You clicked me!";
      changeButton.style.backgroundColor = "#4CAF50";
    });
  
    // Hover effect: Change background color when hovering over the logo
    const logo = document.querySelector(".logo");
    logo.addEventListener("mouseover", () => {
      logo.style.color = "#FF6347"; // Tomato color
    });
    logo.addEventListener("mouseout", () => {
      logo.style.color = "#FFD700"; // Gold color
    });
  
    // Keypress detection: Detect when 'Enter' key is pressed
    document.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        alert("You pressed the Enter key!");
      }
    });
  
    // Bonus: Secret action for double-click or long press
    let timer;
    logo.addEventListener("dblclick", () => {
      alert("Double-click detected!");
    });
    logo.addEventListener("mousedown", () => {
      timer = setTimeout(() => {
        alert("Long press detected!");
      }, 1000); // Trigger long press after 1 second
    });
    logo.addEventListener("mouseup", () => {
      clearTimeout(timer);
    });
  
    // 2. Interactive Elements
  
    // Image gallery slideshow: Change image on button click
    const images = [
      "wallhaven-nk91o7.png", 
      "Images/wallhaven-jxz7ww.png", 
      "Images/wallhaven-vq6vyp.png"
    ];
    let currentImage = 0;
    const imageElement = document.querySelector(".image-gallery");
  
    const nextButton = document.getElementById("nextImage");
    nextButton.addEventListener("click", () => {
      currentImage = (currentImage + 1) % images.length;
      imageElement.src = images[currentImage];
    });
  
    // 3. Form Validation   
    const form = document.getElementById("form");
    const emailField = document.getElementById("email");
    const passwordField = document.getElementById("password");
    const submitButton = document.getElementById("submit");
  
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      let isValid = true;
  
      // Email format validation
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!emailRegex.test(emailField.value)) {
        isValid = false;
        alert("Please enter a valid email address.");
      }
  
      // Password rules (min 8 characters)
      if (passwordField.value.length < 8) {
        isValid = false;
        alert("Password must be at least 8 characters long.");
      }
  
      if (isValid) {
        alert("Form submitted successfully!");
      }
    });
  
    // Bonus: Real-time feedback while typing
    emailField.addEventListener("input", () => {
      const emailFeedback = document.getElementById("emailFeedback");
      emailFeedback.innerText = emailField.value.includes("@") ? "Valid email" : "Invalid email";
    });
  
    passwordField.addEventListener("input", () => {
      const passwordFeedback = document.getElementById("passwordFeedback");
      passwordFeedback.innerText = passwordField.value.length >= 8 ? "Valid password" : "Password too short";
    });
  });
  