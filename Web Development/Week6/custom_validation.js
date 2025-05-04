//Custom Validation
//Use setCustomValidity() for custom error messages.

//Example: Validate Username Length

/*
<label for="username">Username:</label>
<input type="text" id="username">
<p id="validationMessage"></p>
<script>
  const username = document.getElementById("username");

  username.oninput = function () {
    if (username.value.length < 5) {
      username.setCustomValidity("Username must be at least 5 characters.");
    } else {
      username.setCustomValidity("");
    }
  };
</script>
*/