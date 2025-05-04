//How to attach event handlers to elements in JavaScript
//There are three main ways to attach events to elements in JavaScript:

//1. Inline HTML Event Handlers
//Events are directly added to HTML elements using attributes.
<button onclick="alert('Button clicked!')">Click Me</button>

//2. DOM Property Method
//Assign a function to an element’s event property.
const button = document.getElementById('myButton');
button.onclick = function () {
  alert('Button clicked!');
};

//3. addEventListener Method(preferred method)
//This method separates JavaScript from HTML and allows multiple handlers for the same event.
const button = document.getElementById('myButton');
button.addEventListener('click', () => {
  alert('Button clicked!');
});


//Event Object
//The event object provides additional information about the event. For example:
document.addEventListener('click', (e) => {
  console.log(`Mouse clicked at: (${e.clientX}, ${e.clientY})`);
});

//Key Properties of event:

//type: The type of event (e.g., click).
//target: The element that triggered the event.
//preventDefault(): Prevents the default action (e.g., stopping form submission).
//stopPropagation(): Stops the event from bubbling up or capturing down the DOM tree.

//COMMON EVENT TYPES AND ATTRIBUTES
//1. The onclick Event 
//The onclick event is used to run code when an element is clicked.
//Example: Change Background Color on Click

/*
<button id="colorButton">Change Background</button>
<script>
  const button = document.getElementById("colorButton");
  button.onclick = function () {
    document.body.style.backgroundColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
  };
</script>
*/
//Explanation:
//The onclick property is assigned a function that changes the background color dynamically.


//The onmouseover Event 
//The onmouseover event is triggered when the mouse pointer moves over an element.
//Example: Highlight Text on Hover

/* <p id="hoverText">Hover over this text to highlight it!</p>
<script>
  const text = document.getElementById("hoverText");
  text.onmouseover = function () {
    text.style.color = "red";
    text.style.fontWeight = "bold";
  };
  text.onmouseout = function () {
    text.style.color = "black";
    text.style.fontWeight = "normal";
  };
</script>
*/


//The onchange Event 📝
//The onchange event occurs when the value of an input element is changed and the element loses focus.
//Example: Display Input Value on Change

/*
<input type="text" id="nameInput" placeholder="Enter your name">
<p id="nameDisplay"></p>
<script>
  const input = document.getElementById("nameInput");
  const display = document.getElementById("nameDisplay");

  input.onchange = function () {
    display.textContent = `Hello, ${input.value}!`;
  };
</script>
*/