document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        },
        {
            threshold: 0.5,
        }
    );

    sections.forEach((section) => observer.observe(section));
});

document.addEventListener("scroll", () => {
    const sections = document.querySelectorAll(".section");
    sections.forEach((section, index) => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 0) {
            section.style.zIndex = index + 10;
        }
    });
});
