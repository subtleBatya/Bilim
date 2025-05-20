// FOR INDEX PAGE OF THE CONTENT PROFILE

const editBtn = document.getElementById("cnt_edit_btn");
const trashIcons = document.querySelectorAll(".trash_icon"); // Changed from ID to class for multiple elements

if (editBtn) {
    editBtn.addEventListener("click", () => {
        const isEditing = editBtn.textContent === "Edit";
        editBtn.textContent = isEditing ? "Unedit" : "Edit";

        trashIcons.forEach((icon) => {
            icon.style.display = isEditing ? "block" : "none";
        });
    });
}
