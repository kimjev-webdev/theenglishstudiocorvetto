// main/static/js/flyers.js
document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".my-flyer-carousel");
  if (!container) return;

  if (typeof Swiper === "undefined") {
    console.warn("[flyers] Swiper library not found on page.");
    return;
  }

  // Avoid double-init on hot reloads / Turbolinks, etc.
  if (container.dataset.swiperInit === "1") return;
  container.dataset.swiperInit = "1";

  const slides = container.querySelectorAll(".swiper-slide");
  const slideCount = slides.length;

  // Only init Swiper when we actually render 3+ slides (1–2 are static)
  if (slideCount < 3) return;

  const nextBtn = container.querySelector(".swiper-button-next");
  const prevBtn = container.querySelector(".swiper-button-prev");
  const dots    = container.querySelector(".swiper-pagination");

  const swiper = new Swiper(container, {
    // Layout
    effect: "coverflow",
    slidesPerView: "auto",
    centeredSlides: true,
    spaceBetween: 24,

    // Make looping robust with auto-width slides
    loop: true,
    loopPreventsSliding: false,   // never block a slide because of loop math
    normalizeSlideIndex: true,
    watchSlidesProgress: true,
    // (deliberately NOT setting loopedSlides/loopAdditionalSlides)

    // Feel
    grabCursor: true,
    slideToClickedSlide: true,
    allowTouchMove: true,
    resistanceRatio: 0,

    // Coverflow look
    coverflowEffect: {
      rotate: 0,
      stretch: -60,   // slight overlap
      depth: 220,
      modifier: 1.05,
      slideShadows: false,
    },

    // Auto advance
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },

    // UI bits (use elements inside this container)
    navigation: {
      nextEl: nextBtn,
      prevEl: prevBtn,
    },
    pagination: {
      el: dots,
      clickable: true,
    },

    // Safety: if Swiper thinks it reached an end (shouldn't with loop),
    // force jump to the correct looped index.
    on: {
      reachEnd() {
        swiper.slideToLoop(0, 600);
      },
      reachBeginning() {
        swiper.slideToLoop(slideCount - 1, 600);
      },
    },
  });

  // Belt-and-braces: also wire the buttons manually in case nav module misses
  if (nextBtn) {
    nextBtn.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      swiper.slideNext();
    });
  }
  if (prevBtn) {
    prevBtn.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      swiper.slidePrev();
    });
  }

  console.debug("[flyers] Swiper ready:", {
    slideCount,
    hasNext: !!nextBtn,
    hasPrev: !!prevBtn,
  });
});
