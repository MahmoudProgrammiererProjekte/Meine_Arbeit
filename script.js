document.addEventListener("DOMContentLoaded", function() {
    // Dynamische Begrüßung basierend auf der Tageszeit
    const greeting = document.getElementById("greeting");
    const hour = new Date().getHours();
    if (hour < 12) {
      greeting.innerText = "Guten Morgen! Ich bin Mahmoud";
    } else if (hour < 18) {
      greeting.innerText = "Guten Tag! Ich bin Mahmoud";
    } else {
      greeting.innerText = "Guten Abend! Ich bin Mahmoud";
    }
  
    // Interaktive Elemente: Skills & Tools klickbar machen
    document.querySelectorAll(".clickable").forEach(element => {
      element.addEventListener("click", () => {
        element.classList.toggle("highlight");
      });
    });
  
    // Dark Mode Toggle
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    darkModeToggle.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode");
      // Speichern der Einstellung im Local Storage
      if(document.body.classList.contains("dark-mode")){
        localStorage.setItem("theme", "dark");
        darkModeToggle.innerText = "Light Mode";
      } else {
        localStorage.setItem("theme", "light");
        darkModeToggle.innerText = "Dark Mode";
      }
    });
  
    // Prüfe gespeicherten Modus
    const savedTheme = localStorage.getItem("theme");
    if(savedTheme === "dark"){
      document.body.classList.add("dark-mode");
      darkModeToggle.innerText = "Light Mode";
    }
  
    // Intersection Observer für sanfte Scroll-Animationen
    const sections = document.querySelectorAll("section");
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if(entry.isIntersecting){
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.3 });
    sections.forEach(section => observer.observe(section));
  });
  