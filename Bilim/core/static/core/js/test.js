document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");
    let currentSection = null;

    const observerCallback = (entries) => {
        entries.forEach((entry) => {
            const index = [...sections].indexOf(entry.target);
            console.log(`Section ${index + 1}: isIntersecting=${entry.isIntersecting}`);

            if (entry.isIntersecting) {
                if (currentSection !== entry.target) {

                    entry.target.classList.remove("past");

                    if (currentSection) {

                        currentSection.classList.add("past");
                        currentSection.classList.remove("active");
                        currentSection.style.zIndex = index;
                    }


                    entry.target.classList.add("active");
                    entry.target.style.zIndex = index + 10;
                    currentSection = entry.target;
                }
            } else {

                entry.target.classList.remove("active");
                entry.target.style.zIndex = index;


                if (currentSection && [...sections].indexOf(currentSection) > index) {
                    entry.target.classList.remove("past");
                }
            }
        });
    };

    const observerOptions = {
        // threshold: 0.2,
        // rootMargin: "0px 0px -50% 0px",
        // threshold: [0.1, 0.5, 0.9],
        threshold: [0.9, 0.3, 0.5],

    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);

    sections.forEach((section) => observer.observe(section));
});
