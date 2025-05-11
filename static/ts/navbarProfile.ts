const profileBtn = document.getElementById("profileBtn") as HTMLButtonElement;
const dropdown = document.getElementById("profileDropdown") as HTMLDivElement;

profileBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.classList.toggle("hidden");
});

document.addEventListener("click", () => {
    if (!dropdown.classList.contains("hidden")) {
        dropdown.classList.add("hidden");
    }
});