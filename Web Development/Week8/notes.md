
# Combining CSS and JavaScript Animations

Combining CSS animations with JavaScript creates powerful, dynamic, and interactive user experiences. While CSS handles the visual effects, JavaScript provides control, logic, and interactivity. Let’s explore how to seamlessly blend the two.

---

## 1. Why Combine CSS and JavaScript for Animations? 🤔

- **Dynamic Control:** JavaScript allows you to start, stop, or modify CSS animations based on user interactions.  
- **Enhanced Interactivity:** Create effects triggered by events like clicks, hovers, and scrolling.  
- **Flexibility:** Change animation properties dynamically without rewriting CSS.

---

## 2. CSS Animation Basics Refresher 🎥

### Key Properties of CSS Animations

```css
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

### Animation Properties

- `animation-name`: The name of the `@keyframes`.
- `animation-duration`: How long the animation lasts.
- `animation-timing-function`: The animation's pacing.
- `animation-delay`: When the animation should start.
- `animation-iteration-count`: How many times it runs.

---

## 3. Adding Interactivity with JavaScript 🖱️

### Example: Button Click to Trigger Animation

#### HTML

```html
<button id="animateBtn">Animate Box</button>
<div id="box" class="box"></div>
```

#### CSS

```css
.box {
  width: 100px;
  height: 100px;
  background-color: #3498db;
  opacity: 0;
  transition: opacity 0.3s;
}

.box.animate {
  opacity: 1;
  animation: moveRight 2s ease-in-out forwards;
}

@keyframes moveRight {
  0% { transform: translateX(0); }
  100% { transform: translateX(200px); }
}
```

#### JavaScript

```javascript
document.getElementById("animateBtn").addEventListener("click", function () {
  const box = document.getElementById("box");
  box.classList.toggle("animate");
});
```

**How It Works:**

- Clicking the button toggles the `animate` class on the box element.
- CSS animations are triggered when the class is added.

---

### Example: Dynamic Animation Duration

#### HTML

```html
<button id="startAnimation">Start Animation</button>
<div id="circle"></div>
```

#### CSS

```css
#circle {
  width: 50px;
  height: 50px;
  background-color: #e74c3c;
  border-radius: 50%;
  position: relative;
}
```

#### JavaScript

```javascript
document.getElementById("startAnimation").addEventListener("click", function () {
  const circle = document.getElementById("circle");
  circle.style.animation = "expand 3s ease-in-out forwards";
});

const styleSheet = document.styleSheets[0];
styleSheet.insertRule(\`
  @keyframes expand {
    0% { transform: scale(1); }
    100% { transform: scale(2); }
  }
\`, styleSheet.cssRules.length);
```

**How It Works:**

- JavaScript applies the animation as an inline style to the circle.
- The `expand` keyframe is dynamically added to the stylesheet.

---

## 4. Advanced: Controlling Animations with Events 🚀

### Example: Pause and Resume Animation

#### HTML

```html
<button id="pause">Pause</button>
<button id="resume">Resume</button>
<div id="movingBox"></div>
```

#### CSS

```css
#movingBox {
  width: 100px;
  height: 100px;
  background-color: #8e44ad;
  animation: slide 5s linear infinite;
}

@keyframes slide {
  0% { transform: translateX(0); }
  100% { transform: translateX(300px); }
}
```

#### JavaScript

```javascript
const box = document.getElementById("movingBox");
const pauseButton = document.getElementById("pause");
const resumeButton = document.getElementById("resume");

pauseButton.addEventListener("click", () => {
  box.style.animationPlayState = "paused";
});

resumeButton.addEventListener("click", () => {
  box.style.animationPlayState = "running";
});
```

**How It Works:**

- The `animationPlayState` property toggles between `paused` and `running`.

---

## 5. Example: Interactive Modal with Animation

#### HTML

```html
<button id="openModal">Open Modal</button>
<div id="modal" class="modal">
  <div class="modal-content">
    <span id="closeModal" class="close">&times;</span>
    <p>Modal Content Here!</p>
  </div>
</div>
```

#### CSS

```css
.modal {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  animation: scaleUp 0.5s ease forwards;
}

@keyframes scaleUp {
  0% { transform: scale(0); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}

.modal.show {
  display: flex;
}
```

#### JavaScript

```javascript
const modal = document.getElementById("modal");
const openModalButton = document.getElementById("openModal");
const closeModalButton = document.getElementById("closeModal");

openModalButton.addEventListener("click", () => {
  modal.classList.add("show");
});

closeModalButton.addEventListener("click", () => {
  modal.classList.remove("show");
});
```

**How It Works:**

- Clicking "Open Modal" adds the `show` class, making the modal visible and triggering the animation.
- Clicking "Close" removes the class, hiding the modal.

---

## 6. Tools and Tips for Combining CSS and JavaScript Animations

### Tools to Enhance Animations

- **GSAP (GreenSock):** A powerful library for complex animations.
- **Lottie:** For JSON-based animations.

### Best Practices

- Use **CSS** for simple animations and transitions (e.g., hover effects).
- Use **JavaScript** for logic-heavy animations (e.g., conditional triggers).
- Optimize performance by using `transform` and `opacity` over properties like `width` or `height`.

---

By combining CSS animations and JavaScript, you can craft visually appealing, interactive websites that captivate users.  
**Experiment and let your creativity flow!** 🚀✨
