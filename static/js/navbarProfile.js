"use strict";
const profileBtn = document.getElementById("profileBtn");
const dropdown = document.getElementById("profileDropdown");
profileBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.classList.toggle("hidden");
});
document.addEventListener("click", () => {
    if (!dropdown.classList.contains("hidden")) {
        dropdown.classList.add("hidden");
    }
});
