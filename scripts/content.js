const editBtn = document.getElementById("cnt_edit_btn");
const trashIcons = document.querySelectorAll("#trash_icon");


editBtn.addEventListener("click", () => {
    const isEditing = editBtn.textContent === "Edit";

    editBtn.textContent = isEditing ? "Unedit" : "Edit";

    trashIcons.forEach((icon) => {
        icon.style.display = isEditing ? "block" : "none";
    })


})