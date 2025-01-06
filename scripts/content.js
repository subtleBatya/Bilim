let editBtn = document.getElementById("cnt_edit_btn");
let trashIcon = document.getElementById("trash_icon");

editBtn.addEventListener("click", () => {
    trashIcon.classList.add('d-none');
})
