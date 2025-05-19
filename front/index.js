const track = document.querySelector('.carousel-track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.carousel-button.next');
const prevButton = document.querySelector('.carousel-button.prev');
const modal = document.getElementById('myModal');
const modalImg = document.getElementById('img01');
const modalTitle = document.getElementById('modal-title');
const modalDesc = document.getElementById('modal-description');
const modalClose = document.querySelector('.close');
const playLink = modal.querySelector('.play');
const descargaLink = modal.querySelector('.descarga');

let currentIndex = 0;

function updateCarousel() {
  const slideWidth = slides[0].getBoundingClientRect().width;
  track.style.transform = `translateX(-${currentIndex * (slideWidth + 20)}px)`;
}

nextButton.addEventListener('click', () => {
  if (currentIndex < slides.length - 1) {
    currentIndex++;
    updateCarousel();
  }
});

prevButton.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    updateCarousel();
  }
});

let startX;

track.addEventListener('mousedown', (e) => {
  startX = e.clientX;
  track.style.cursor = 'grabbing';
});

track.addEventListener('mouseup', (e) => {
  const endX = e.clientX;
  const delta = endX - startX;

  if (delta > 50 && currentIndex > 0) {
    currentIndex--;
  } else if (delta < -50 && currentIndex < slides.length - 1) {
    currentIndex++;
  }
  updateCarousel();
  track.style.cursor = 'grab';
});

// Modal interactions
slides.forEach((slide) => {
  slide.addEventListener('click', () => {
    const img = slide.querySelector('img');
    if (img) {
      modal.style.display = 'block';
      modalImg.src = img.src;
      modalTitle.textContent = slide.dataset.title;
      modalDesc.textContent = slide.dataset.content;

      // Set modal links
      playLink.href = slide.dataset.url || '#';
      descargaLink.href = slide.dataset.descarga || '#';
    }
  });
});

modalClose.onclick = () => {
  modal.style.display = 'none';
};

window.onclick = (event) => {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
};
