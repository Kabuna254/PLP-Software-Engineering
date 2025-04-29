// Function to change the text of the paragraph
function changeText() {
    document.getElementById("message").textContent = "The text has been changed!";
  }
  
  // Function to change the color of the heading
  function changeColor() {
    if (document.getElementById("title").style.color === "yellow") {
      document.getElementById("title").style.color = "red"; // Change to red if it's yellow
    }
    else {
      document.getElementById("title").style.color = "yellow"; // Change to yellow if it's red
    }
  }
  
  // Function to add a new paragraph inside the container
  function addItem() {
    const newItem = document.createElement("p"); // Create a new paragraph element
    newItem.textContent = "New item has been added!";     // Set its text
    newItem.id = "newItem";                      // Assign it an ID
    document.getElementById("container").appendChild(newItem); // Add it to the page
  }
  
  // Function to remove the added paragraph if it exists
  function removeItem() {
    const item = document.getElementById("newItem"); // Find the item by ID
    if (item) {
      item.remove(); // Remove it from the page
    }
  }
  