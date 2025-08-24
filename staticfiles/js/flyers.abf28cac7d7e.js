// main/static/js/flyers.js
document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".my-flyer-carousel");
  if (!container) return;

  if (typeof Swiper === "undefined") {
    console.warn("[flyers] Swiper library not found on page.");
    return;
  }

  const slideCount = container.querySelectorAll(".swiper-slide").length;
  // Only run the carousel for 3+ slides. (1–2 are rendered statically.)
  if (slideCount < 3) return;

  const swiper = new Swiper(container, {
    effect: "coverflow",
    loop: true,
    centeredSlides: true,
    centeredSlidesBounds: true,
    slidesPerView: "auto",
    spaceBetween: 24,
    grabCursor: true,
    slideToClickedSlide: true,
    watchSlidesProgress: true,
    normalizeSlideIndex: true,
    coverflowEffect: {
      rotate: 0,
      stretch: -60,      // slight overlap for "stacked" look
      depth: 220,
      modifier: 1.05,
      slideShadows: false,
    },
    autoplay: { delay: 4000, disableOnInteraction: false },

    // IMPORTANT: bind nav/pagination *from this container* so they’re scoped.
    navigation: {
      nextEl: container.querySelector(".swiper-button-next"),
      prevEl: container.querySelector(".swiper-button-prev"),
    },
    pagination: {
      el: container.querySelector(".swiper-pagination"),
      clickable: true,
    },

    // Do not reference the outer `swiper` during construction.
    on: {
      afterInit(sw) {
        // Mark as ready (useful for debugging/styles if needed)
        container.classList.add("swiper-ready");
      },
      // If you still want hard looping behaviour, use the instance param:
      // reachEnd(sw) { sw.slideNext(); }
    },
  });

  // Recalculate once images finish loading (prevents odd initial offsets).
  container.querySelectorAll("img").forEach((img) => {
    if (img.complete) return;
    img.addEventListener("load", () => swiper.update());
  });
});
