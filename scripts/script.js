

const einParentDiv = document.querySelector('.einstein_animes'); 
const einDivs = einParentDiv.querySelectorAll('.einstein_anime'); 

let currentIndex = 0;


function showNextRow() {
  einDivs.forEach((e) => {
    e.style.display = 'none';
  });

  einDivs[currentIndex].style.display = 'flex';

  currentIndex = (currentIndex + 1) % einDivs.length;
}

showNextRow();

setInterval(showNextRow, 4000);





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
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
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



