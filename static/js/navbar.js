"use strict";
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
const overlay = document.getElementById('overlay');
menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
    mobileMenu.classList.toggle('flex');
    overlay.classList.toggle('hidden');
    if (!mobileMenu.classList.contains('hidden')) {
        document.body.classList.add('overflow-hidden');
    }
    else {
        document.body.classList.remove('overflow-hidden');
    }
});
overlay.addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
    mobileMenu.classList.remove('flex');
    overlay.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
});
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
