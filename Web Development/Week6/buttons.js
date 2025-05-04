//Buttons
//Buttons are the backbone of interactivity. Here's how you can make them dynamic:

//Example: Toggle Visibility

/*
<button id="toggleButton">Hide Text</button>
<p id="toggleText">This text will be hidden or shown when you click the button.</p>
<script>
  const button = document.getElementById("toggleButton");
  const text = document.getElementById("toggleText");

  button.onclick = function () {
    if (text.style.display === "none") {
      text.style.display = "block";
      button.textContent = "Hide Text";
    } else {
      text.style.display = "none";
      button.textContent = "Show Text";
    }
  };
</script>
*/