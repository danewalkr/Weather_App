document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("weather-form");
  const loader = document.getElementById("loader");

  form.addEventListener("submit", function () {
    loader.style.display = "block";
  });

  // Optional: Focus input on load
  document.getElementById("city-input").focus();
  
  console.log("🌦️ Weather app loaded.");
});
