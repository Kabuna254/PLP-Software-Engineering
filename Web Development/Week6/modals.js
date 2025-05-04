//Modals
//Modals are popup elements that grab the user’s attention.

//Example: Create a Simple Modal

/*
<button id="openModal">Open Modal</button>
<div id="modal" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); padding:20px; background:white; box-shadow:0 0 10px rgba(0,0,0,0.5);">
  <p>This is a modal!</p>
  <button id="closeModal">Close</button>
</div>
<script>
  const modal = document.getElementById("modal");
  const openModal = document.getElementById("openModal");
  const closeModal = document.getElementById("closeModal");

  openModal.onclick = function () {
    modal.style.display = "block";
  };
  closeModal.onclick = function () {
    modal.style.display = "none";
  };
</script>
*/