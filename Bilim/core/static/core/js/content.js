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

function handleFileUpload(input) {
    const files = Array.from(input.files); // Get all selected files
    const fileInfoContainer = document.getElementById("fileInfoContainer");
    const maxDuration = 20 * 60; // 20 minutes in seconds

    // Clear any existing file information to ensure only one file is processed
    fileInfoContainer.innerHTML = "";

    if (files.length > 1) {
        alert("You can only upload one file at a time.");
        input.value = ""; // Clear the input to prevent uploading multiple files
        return;
    }

    const file = files[0]; // Get the first (and only) file
    const video = document.createElement("video");
    video.preload = "metadata";
    const fileName = file.name; // Store filename before clearing input

    video.onloadedmetadata = function () {
        window.URL.revokeObjectURL(video.src); // Clean up the object URL

        if (video.duration > maxDuration) {
            alert(`The video "${fileName}" exceeds the maximum allowed duration of 20 minutes.`);
            input.value = ""; // Clear the input to prevent uploading
            return;
        }

        // If valid, create a container for the file
        const fileContainer = document.createElement("div");
        fileContainer.className = "mb-3";

        // Create file name display
        const fileNameDisplay = document.createElement("p");
        fileNameDisplay.textContent = `Selected File: ${fileName}`;
        fileNameDisplay.className = "fw-bold text-dark mb-1";

        // Create progress bar
        const progressBarContainer = document.createElement("div");
        progressBarContainer.className = "progress mb-2";
        const progressBar = document.createElement("div");
        progressBar.className = "progress-bar";
        progressBar.style.width = "0%";
        progressBar.textContent = "0%";
        progressBarContainer.appendChild(progressBar);

        // Create Remove button
        const removeButton = document.createElement("button");
        removeButton.className = "btn btn-danger btn-sm";
        removeButton.textContent = "Remove";
        removeButton.onclick = () => removeFile(fileContainer, input);

        // Append file name, progress bar, and remove button to the file container
        fileContainer.appendChild(fileNameDisplay);
        fileContainer.appendChild(progressBarContainer);
        fileContainer.appendChild(removeButton);
        fileInfoContainer.appendChild(fileContainer);

        // Simulate progress (for demonstration purposes)
        let progress = 0;
        const interval = setInterval(() => {
            progress += 10;
            if (progress <= 100) {
                progressBar.style.width = `${progress}%`;
                progressBar.textContent = `${progress}%`;
            } else {
                clearInterval(interval);
            }
        }, 300);
    };

    video.src = URL.createObjectURL(file); // Load the video to check its duration
}

function removeFile(fileContainer, input) {
    if (fileContainer) {
        fileContainer.remove(); // Remove the file container
    }
    input.value = ""; // Clear the file input field
}



















// const editBtn = document.getElementById("cnt_edit_btn");
// const trashIcons = document.querySelectorAll(".trash_icon");


// if (editBtn) {
//     editBtn.addEventListener("click", () => {
//         const isEditing = editBtn.textContent === "Edit";
//         editBtn.textContent = isEditing ? "Unedit" : "Edit";

//         trashIcons.forEach((icon) => {
//             icon.style.display = isEditing ? "block" : "none";
//         });
//     });
// }

    

// function handleFileUpload(input) {
//   const files = Array.from(input.files); // Get all selected files
//   const fileInfoContainer = document.getElementById('fileInfoContainer');
//   const maxDuration = 20 * 60; // 20 minutes in seconds

//   // Clear any existing file information to ensure only one file is processed
//   fileInfoContainer.innerHTML = ""; 

//   if (files.length > 1) {
//       alert("You can only upload one file at a time.");
//       input.value = ""; // Clear the input to prevent uploading multiple files
//       return;
//   }

//   const file = files[0]; // Get the first (and only) file
//   const video = document.createElement('video');
//   video.preload = 'metadata';
//   const fileName = file.name; // Store filename before clearing input

//   video.onloadedmetadata = function () {
//       window.URL.revokeObjectURL(video.src); // Clean up the object URL

//       if (video.duration > maxDuration) {
//           alert(`The video "${file.name}" exceeds the maximum allowed duration of 20 minutes.`);
//           input.value = ""; // Clear the input to prevent uploading
//           return;
//       } else {
//           // If valid, create a container for the file
//           const fileContainer = document.createElement('div');
//           fileContainer.className = 'mb-3';
//           fileContainer.id = 'file-container'; // Unique ID for the file container

//           // Create file name display
//           const fileName = document.createElement('p');
//           fileName.textContent = `Selected File: ${file.name}`;
//           fileName.className = 'fw-bold text-dark mb-1';

//           // Create progress bar
//           const progressBarContainer = document.createElement('div');
//           progressBarContainer.className = 'progress mb-2';
//           const progressBar = document.createElement('div');
//           progressBar.className = 'progress-bar';
//           progressBar.style.width = '0%';
//           progressBar.textContent = '0%';
//           progressBarContainer.appendChild(progressBar);

//           // Create Remove button
//           const removeButton = document.createElement('button');
//           removeButton.className = 'btn btn-danger btn-sm';
//           removeButton.textContent = 'Remove';
//           removeButton.onclick = () => removeFile(fileContainer.id, input);

//           // Append file name, progress bar, and remove button to the file container
//           fileContainer.appendChild(fileName);
//           fileContainer.appendChild(progressBarContainer);
//           fileContainer.appendChild(removeButton);
//           fileInfoContainer.appendChild(fileContainer);

//           // Simulate progress (for demonstration purposes)
//           let progress = 0;
//           const interval = setInterval(() => {
//               progress += 10;
//               if (progress <= 100) {
//                   progressBar.style.width = `${progress}%`;
//                   progressBar.textContent = `${progress}%`;
//               } else {
//                   clearInterval(interval);
//               }
//           }, 300);
//       }
//   };

//   video.src = URL.createObjectURL(file); // Load the video to check its duration
// }

// function removeFile(containerId, input) {
//   const fileContainer = document.getElementById(containerId);
//   if (fileContainer) {
//       fileContainer.remove(); // Remove the file container
//   }
//   input.value = ""; // Clear the file input field
// }




    // function handleFileUpload(input) {
    //     const files = Array.from(input.files); // Get all selected files
    //     const fileInfoContainer = document.getElementById('fileInfoContainer');
    //     const maxDuration = 20 * 60; // 20 minutes in seconds
      
    //     files.forEach((file, index) => {
    //       const video = document.createElement('video');
    //       video.preload = 'metadata';
      
    //       video.onloadedmetadata = function () {
    //         window.URL.revokeObjectURL(video.src); // Clean up the object URL
      
    //         if (video.duration > maxDuration) {
    //           alert(`The video "${file.name}" exceeds the maximum allowed duration of 20 minutes.`);
    //           input.value = ""; // Clear the input to prevent uploading
    //           return; // Skip adding this file to the UI
    //         } else {
    //          // If valid, create a container for the file
    //           const fileContainer = document.createElement('div');
    //           fileContainer.className = 'mb-3';
    //           fileContainer.id = `file-${index}`; // Unique ID for each file container
      
    //           // Create file name display
    //           const fileName = document.createElement('p');
    //           fileName.textContent = `Selected File: ${file.name}`;
    //           fileName.className = 'fw-bold text-dark mb-1';
      
    //           // Create progress bar
    //           const progressBarContainer = document.createElement('div');
    //           progressBarContainer.className = 'progress mb-2';
    //           const progressBar = document.createElement('div');
    //           progressBar.className = 'progress-bar';
    //           progressBar.style.width = '0%';
    //           progressBar.textContent = '0%';
    //           progressBarContainer.appendChild(progressBar);
      
    //           // Create Remove button
    //           const removeButton = document.createElement('button');
    //           removeButton.className = 'btn btn-danger btn-sm';
    //           removeButton.textContent = 'Remove';
    //           removeButton.onclick = () => removeFile(fileContainer.id);
      
    //           // Append file name, progress bar, and remove button to the file container
    //           fileContainer.appendChild(fileName);
    //           fileContainer.appendChild(progressBarContainer);
    //           fileContainer.appendChild(removeButton);
    //           fileInfoContainer.appendChild(fileContainer);
      
    //           // Simulate progress (for demonstration purposes)
    //           let progress = 0;
    //           const interval = setInterval(() => {
    //             progress += 10;
    //             if (progress <= 100) {
    //               progressBar.style.width = `${progress}%`;
    //               progressBar.textContent = `${progress}%`;
    //             } else {
    //               clearInterval(interval);
    //             }
    //           }, 300);
    //         }
    //       };
      
    //       video.src = URL.createObjectURL(file); // Load the video to check its duration
    //     });
    //   }
      
    //   function removeFile(containerId) {
    //     const fileContainer = document.getElementById(containerId);
    //     if (fileContainer) {
    //       fileContainer.remove(); // Remove the file container
    //     }
    //   }
      
    
