

let gen_btn = document.getElementById("gen_btn");
let exam_btn = document.getElementById("exam_btn");
let class_btn = document.getElementById("class_btn");

let gen_block = document.getElementById("general_block");
let exam_block = document.getElementById("exams_block");
let class_block = document.getElementById("class_block");



exam_btn.addEventListener( "click", () => {
    exam_btn.classList.add('border-bottom', 'border-2', 'border-primary');
    exam_block.classList.remove('d-none');
    
    if(exam_btn.classList.contains('border-bottom', 'border-2', 'border-primary')) {
        gen_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        class_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        gen_block.classList.add('d-none');
        class_block.classList.add('d-none');
    }
});


gen_btn.addEventListener( "click", () => {
    gen_btn.classList.add('border-bottom', 'border-2', 'border-primary');
    gen_block.classList.remove('d-none');
    
    if(gen_btn.classList.contains('border-bottom', 'border-2', 'border-primary')){
        exam_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        class_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        exam_block.classList.add('d-none');
        class_block.classList.add('d-none');
    }
});

class_btn.addEventListener("click", () => {
    class_btn.classList.add('border-bottom', 'border-2', 'border-primary');
    class_block.classList.remove('d-none');

    if(class_btn.classList.contains('border-bottom', 'border-2', 'border-primary')){
        exam_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        gen_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        exam_block.classList.add('d-none');
        gen_block.classList.add('d-none');
    }
})