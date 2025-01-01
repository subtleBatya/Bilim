document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");


    let currentSection = null;

    const observerCallback = (entries) => {
        entries.forEach((entry) => {
            const index = [...sections].indexOf(entry.target);
            console.log(`Section ${index + 1}: isIntersecting=${entry.isIntersecting}`);

            if (entry.isIntersecting) {
                if (currentSection !== entry.target) {

                    if (currentSection) {
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
            }
        });
    };

    const observerOptions = {
        threshold: 0.1,
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);

    sections.forEach((section) => observer.observe(section));
});
