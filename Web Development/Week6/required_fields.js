//Required Fields
//Check if required fields are filled out before submission.

//Example: Basic Required Validation

/*
<form id="myForm">
  <label for="email">Email:</label>
  <input type="email" id="email" required>
  <button type="submit">Submit</button>
  <p id="errorMessage" style="color: red;"></p>
</form>
<script>
  const form = document.getElementById("myForm");
  const email = document.getElementById("email");
  const errorMessage = document.getElementById("errorMessage");

  form.onsubmit = function (e) {
    if (!email.value) {
      e.preventDefault(); // Prevent form submission
      errorMessage.textContent = "Email is required!";
    }
  };
</script>
*/