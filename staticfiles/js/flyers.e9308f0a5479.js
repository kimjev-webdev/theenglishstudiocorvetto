// main/static/js/flyers.js
document.addEventListener('DOMContentLoaded', function () {
  const container = document.querySelector('.my-flyer-carousel');
  if (!container) return;

  if (typeof Swiper === 'undefined') {
    console.warn('[flyers] Swiper library not found on page.');
    return;
  }

  const slideEls = container.querySelectorAll('.swiper-slide');
  const slideCount = slideEls.length;
  if (slideCount < 3) return; // we only init Swiper for 3+ slides

  const swiper = new Swiper(container, {
    effect: 'coverflow',
    loop: true,                         // infinite
    loopedSlides: slideCount,           // duplicate all for safety
    loopAdditionalSlides: 3,            // extra duplicates avoid gaps
    centeredSlides: true,
    centeredSlidesBounds: true,
    slidesPerView: 'auto',
    spaceBetween: 24,
    grabCursor: true,
    slideToClickedSlide: true,
    watchSlidesProgress: true,
    normalizeSlideIndex: true,
    coverflowEffect: {
      rotate: 0,
      stretch: -60,                     // slight overlap
      depth: 220,
      modifier: 1.05,
      slideShadows: false
    },
    autoplay: { delay: 4000, disableOnInteraction: false },
    navigation: {
      // bind to elements *inside* this container
      nextEl: container.querySelector('.swiper-button-next'),
      prevEl: container.querySelector('.swiper-button-prev'),
    },
    pagination: {
      el: container.querySelector('.swiper-pagination'),
      clickable: true
    }
  });

  // Optional sanity log; remove later.
  console.debug('[flyers] Swiper ready with', slideCount, 'slides', swiper);
});
