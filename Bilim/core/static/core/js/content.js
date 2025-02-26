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
        progressBarContainer.className = "progress mb-2 h-100";
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

        // Debugging: Check if progressBar exists
        console.log("Progress Bar:", progressBar);

        // Ensure Progress Bar is in DOM before updating
        setTimeout(() => {
            let progress = 0;
            function updateProgress() {
                if (progress >= 100) {
                    
                    progressBar.textContent = "100%";
                    progressBar.style.backgroundColor = "#28a745";
                    console.log("Progress complete!");
                    return;
                }
                progress += 10;
                progressBar.style.setProperty("width", progress + "%", "important");
                progressBar.textContent = `${progress}%`;   
                console.log(`Progress updated: ${progress}%`);

                // Use requestAnimationFrame for smoother updates
                setTimeout(updateProgress, 300);
            }

            updateProgress();
        }, 200);
    };

    video.src = URL.createObjectURL(file); // Load the video to check its duration
}

function removeFile(fileContainer, input) {
    if (fileContainer) {
        fileContainer.remove(); // Remove the file container
    }
    input.value = ""; // Clear the file input field
}

