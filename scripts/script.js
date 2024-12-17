

const data = [
  {
    image: './images/Tesla.webp',
    title: 'Nikola Tesla',
    text: '"Geljegiň güýji Elektromagnetizmde ýatyr"'
  },
  {
    image: './images/Newton.webp',
    title: 'Isaac Newton',
    text: '"Men uzak serhetleri görüp bilýän bolsam, onda men ullakan eňňitleriň üstünde duranlygym üçin"'
  },
  {
    image: './images/MarieCurie.webp',
    title: 'Marie Curie',
    text: '"Ylmyň çäksiz güýji bar"'
  }
];


let currentIndex = 0;


function removeAnimationClasses(element, animationClass) {
  element.addEventListener("animationend", () => {
    element.classList.remove(animationClass);
  }, { once: true });
}

function updateContent() {
  const imageElement = document.getElementById('changing-image');
  const titleElement = document.getElementById('changing-title');
  const textElement = document.getElementById('changing-text');

  imageElement.classList.add('fade-out');
  titleElement.classList.add('fade-out');
  textElement.classList.add('fade-out');

  setTimeout(() => {
    imageElement.src = data[currentIndex].image;
    titleElement.textContent = data[currentIndex].title;
    textElement.textContent = data[currentIndex].text;

    imageElement.classList.add('fade-in');
    titleElement.classList.add('fade-in');
    textElement.classList.add('fade-in');

    removeAnimationClasses(imageElement, 'fade-in');
    removeAnimationClasses(titleElement, 'fade-in');
    removeAnimationClasses(textElement, 'fade-in');

    removeAnimationClasses(imageElement, 'fade-out');
    removeAnimationClasses(titleElement, 'fade-out');
    removeAnimationClasses(textElement, 'fade-out');

    currentIndex = (currentIndex + 1) % data.length;
  }, 500);
}

updateContent();

setInterval(updateContent, 5000);

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



