
// FOR SCIENTISTS ANIMATION IN THE MAIN FILE

  document.addEventListener("DOMContentLoaded", () =>{

    // Get button elements
    const gen_btn = document.getElementById("gen_btn");
    const exam_btn = document.getElementById("exam_btn");
    const class_btn = document.getElementById("class_btn");
    const subs_btn = document.getElementById("subs_btn");
  
    // Get block elements
  
    const gen_block = document.getElementById("general_block");
    const exam_block = document.getElementById("exams_block");
    const class_block = document.getElementById("class_block");
    const subs_block = document.getElementById("subs_block");
  
 
  
    // Exam button logic
    exam_btn.addEventListener("click", () => {
      exam_btn.classList.add('border-bottom', 'border-2', 'border-primary');
      exam_block.classList.remove('d-none');
  
      if (exam_btn.classList.contains('border-bottom', 'border-2', 'border-primary')) {
        gen_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        class_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        subs_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        gen_block.classList.add('d-none');
        class_block.classList.add('d-none');
        subs_block.classList.add('d-none');
      }
    });
  
    // General button logic
    gen_btn.addEventListener("click", () => {
      gen_btn.classList.add('border-bottom', 'border-2', 'border-primary');
      gen_block.classList.remove('d-none');
  
      if (gen_btn.classList.contains('border-bottom', 'border-2', 'border-primary')) {
        exam_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        class_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        subs_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        exam_block.classList.add('d-none');
        class_block.classList.add('d-none');
        subs_block.classList.add('d-none');
      }
    });
  
    // Class button logic
    class_btn.addEventListener("click", () => {
      class_btn.classList.add('border-bottom', 'border-2', 'border-primary');
      class_block.classList.remove('d-none');
  
      if (class_btn.classList.contains('border-bottom', 'border-2', 'border-primary')) {
        exam_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        gen_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        subs_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        exam_block.classList.add('d-none');
        gen_block.classList.add('d-none');
        subs_block.classList.add('d-none');
      }
    });
  
    // Subs button logic
    subs_btn.addEventListener("click", () => {
      subs_btn.classList.add('border-bottom', 'border-2', 'border-primary');
      subs_block.classList.remove('d-none');
  
      if (subs_btn.classList.contains('border-bottom', 'border-2', 'border-primary')) {
        gen_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        class_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        exam_btn.classList.remove('border-bottom', 'border-2', 'border-primary');
        gen_block.classList.add('d-none');
        class_block.classList.add('d-none');
        exam_block.classList.add('d-none');
      }
    });

  
  // Attach the async initialize function to the load event
  window.addEventListener('load', async () => {
    await initializeTabLogic();
  });
  

  })
  
  
  
  


