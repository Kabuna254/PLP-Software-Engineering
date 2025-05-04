//Sliders
//Sliders are great for adjusting values dynamically, such as volume or brightness.

//Example: Adjust Font Size with a Slider

/*
<input type="range" id="fontSlider" min="10" max="50" value="20">
<p id="sliderText" style="font-size: 20px;">Adjust my size!</p>
<script>
  const slider = document.getElementById("fontSlider");
  const text = document.getElementById("sliderText");

  slider.oninput = function () {
    text.style.fontSize = `${slider.value}px`;
  };
</script>
*/