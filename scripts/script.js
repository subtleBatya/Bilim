/*

async function initializeWebsiteLogic() {
  console.log("Initializing website logic...");

  // Меняет цвет при скролле
  const header = document.querySelector('#navbar');

  function changeHeaderColor() {
    const scrollPosition = window.scrollY;
    const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollThreshold = windowHeight * 0.1;

    if (scrollPosition > scrollThreshold) {
      header.classList.remove('bg-transparent');
      header.style.backgroundColor = 'rgba(178, 235, 242, 1)';
    } else {
      header.classList.add('bg-transparent');
    }
  }

  window.addEventListener('scroll', changeHeaderColor);

  // Функция для стрелок меню
  document.addEventListener('DOMContentLoaded', () => {
    const profileDropdown = document.getElementById('profileDropdown');
    const profileMenu = document.getElementById('profileMenu');
    const coursesDropdown = document.getElementById('coursesDropdown');
    const coursesMenu = document.getElementById('coursesMenu');

    function toggleMenu(dropdown, menu) {
      const arrow = dropdown.querySelector('.arrow');
      const isVisible = menu.classList.contains('show');

      closeAllMenus();

      if (!isVisible) {
        menu.classList.add('show');
        arrow.textContent = '▲';
        arrow.style.color = '#FFA000';
      } else {
        arrow.textContent = '▼';
        arrow.style.color = 'black';
      }
    }

    function closeAllMenus() {
      document.querySelectorAll('.dropdown-menu1').forEach(menu => {
        menu.classList.remove('show');
      });
      document.querySelectorAll('.arrow').forEach(arrow => {
        arrow.textContent = '▼';
        arrow.style.color = 'black';
      });
    }

    profileDropdown.addEventListener('click', e => {
      e.preventDefault();
      toggleMenu(profileDropdown, profileMenu);
    });

    coursesDropdown.addEventListener('click', e => {
      e.preventDefault();
      toggleMenu(coursesDropdown, coursesMenu);
    });

    document.addEventListener('click', e => {
      if (!e.target.closest('.nav-item')) {
        closeAllMenus();
      }
    });
  });

  // Функция для смены языка
  function changeLanguage() {
    let languageName = document.getElementById('languageName');
    let languageImage = document.getElementById("languageImage");
    console.log("Function is working");
    let imageSrc = languageImage.src;
    if (imageSrc.endsWith('russian-flag.png')) {
      imageSrc = './images/turkmen-flag.png';
      languageName.textContent = "TM";
      console.log("Russian");
    } else {
      imageSrc = './images/russian-flag.png';
      languageName.textContent = "RU";
      console.log("TM");
    }

    languageImage.src = imageSrc;
    console.log("Language path is set to:", imageSrc);
  }

  // Функция для button в Оплате
  const button1 = document.getElementById('button1');
  const button2 = document.getElementById('button2');
  const content = document.getElementById('content');
  const registration = document.getElementById('registration');

  content.classList.remove('d-none');
  button1.classList.add('active');

  button1.addEventListener('click', () => {
    content.classList.remove('d-none');
    registration.classList.add('d-none');
    button1.classList.add('active');
    button2.classList.remove('active');
  });

  button2.addEventListener('click', () => {
    content.classList.add('d-none');
    registration.classList.remove('d-none');
    button2.classList.add('active');
    button1.classList.remove('active');
  });
}

// Attach the async initialize function to the load event
window.addEventListener('load', async () => {
  await initializeWebsiteLogic();
});
*/


/*asdasd */













async function initializeWebsiteLogic() {
  console.log("All content has been fully loaded. Initializing logic...");

  try {
    // Simulate a heavy or asynchronous task
    await performHeavyInitialization();






    // Меняет цвет при скролле
    const header = document.querySelector('#navbar');

    function changeHeaderColor() {
      const scrollPosition = window.scrollY;
      const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollThreshold = windowHeight * 0.1;

      if (scrollPosition > scrollThreshold) {
        header.classList.remove('bg-transparent');
        header.style.backgroundColor = 'rgba(178, 235, 242, 1)';
      } else {
        header.classList.add('bg-transparent');
      }
    }
    window.addEventListener('scroll', changeHeaderColor);


    // Функция для стрелок меню
    document.addEventListener('DOMContentLoaded', () => {
      const profileDropdown = document.getElementById('profileDropdown')
      const profileMenu = document.getElementById('profileMenu')
      const coursesDropdown = document.getElementById('coursesDropdown')
      const coursesMenu = document.getElementById('coursesMenu')

      function toggleMenu(dropdown, menu) {
        const arrow = dropdown.querySelector('.arrow')
        const isVisible = menu.classList.contains('show')

        closeAllMenus()

        if (!isVisible) {
          menu.classList.add('show')
          arrow.textContent = '▲'
          arrow.style.color = '#FFA000'
        } else {
          arrow.textContent = '▼'
          arrow.style.color = 'black'
        }
      }

      function closeAllMenus() {
        document.querySelectorAll('.dropdown-menu1').forEach(menu => {
          menu.classList.remove('show')
        })
        document.querySelectorAll('.arrow').forEach(arrow => {
          arrow.textContent = '▼'
          arrow.style.color = 'black'
        })
      }

      profileDropdown.addEventListener('click', e => {
        e.preventDefault()
        toggleMenu(profileDropdown, profileMenu)
      })

      coursesDropdown.addEventListener('click', e => {
        e.preventDefault()
        toggleMenu(coursesDropdown, coursesMenu)
      })

      document.addEventListener('click', e => {
        if (!e.target.closest('.nav-item')) {
          closeAllMenus()
        }
      })
    })

    function changeLanguage() {

      let languageName = document.getElementById('languageName');
      let languageImage = document.getElementById("languageImage");
      console.log("Function is working");
      let imageSrc = languageImage.src;
      if (imageSrc.endsWith('russian-flag.png')) {
        imageSrc = './images/turkmen-flag.png';
        languageName.textContent = "TM";
        console.log("Russian");
      }
      else {
        imageSrc = './images/russian-flag.png';
        languageName.textContent = "RU";
        console.log("TM");
      }

      languageImage.src = imageSrc;
      console.log("Language path is set to:", imageSrc);
    }

    //Функция для button в Оплате
    const button1 = document.getElementById('button1')
    const button2 = document.getElementById('button2')
    const content = document.getElementById('content')
    const registration = document.getElementById('registration')

    content.classList.remove('d-none')
    button1.classList.add('active')

    button1.addEventListener('click', () => {
      content.classList.remove('d-none')
      registration.classList.add('d-none')
      button1.classList.add('active')
      button2.classList.remove('active')
    })

    button2.addEventListener('click', () => {
      content.classList.add('d-none')
      registration.classList.remove('d-none')
      button2.classList.add('active')
      button1.classList.remove('active')
    })

    console.log("Initialization complete.");
  } catch (error) {
    console.error("Error during initialization:", error);
  }
}


async function performHeavyInitialization() {
  console.log("Starting heavy initialization...");

  // Simulating a delay, e.g., loading data or preparing resources
  return new Promise((resolve) => setTimeout(resolve, 2000)); // 2-second delay
}


window.addEventListener("load", async () => {
  await initializeWebsiteLogic();
});




