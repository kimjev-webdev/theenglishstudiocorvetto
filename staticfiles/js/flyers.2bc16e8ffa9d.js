// main/static/js/flyers.js
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    const root = document.querySelector(".flyer-cf");
    if (!root) return;

    const track = root.querySelector(".flyer-cf-track");
    const slides = Array.from(track.querySelectorAll(".flyer-cf-slide"));
    const n = slides.length;

    // Only enable the coverflow for 3+ slides. 1–2 stay static in the template.
    if (n < 3) return;

    const prevBtn = root.querySelector(".cf-prev");
    const nextBtn = root.querySelector(".cf-next");
    const autoplayDelay =
      parseInt(root.getAttribute("data-autoplay") || "4000", 10) || 4000;

    let i = 0;      // current center index
    let timer = null;

    function cls(el, ...names) {
      el.className = "flyer-cf-slide " + names.join(" ");
    }

    function render() {
      const L1 = (i - 1 + n) % n;
      const R1 = (i + 1) % n;
      slides.forEach((el, idx) => {
        if (idx === i) {
          cls(el, "cf-center");
        } else if (idx === L1) {
          cls(el, "cf-left");
        } else if (idx === R1) {
          cls(el, "cf-right");
        } else {
          // put everything else outside, left or right
          // decide side by shortest direction
          const distR = (idx - i + n) % n;
          const distL = (i - idx + n) % n;
          if (distL < distR) {
            cls(el, "cf-out-left");
          } else {
            cls(el, "cf-out-right");
          }
        }
      });
    }

    function go(delta) {
      i = (i + delta + n) % n;
      render();
    }

    function startAuto() {
      stopAuto();
      timer = setInterval(() => go(1), autoplayDelay);
    }
    function stopAuto() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    }

    // Nav
    nextBtn.addEventListener("click", () => go(1));
    prevBtn.addEventListener("click", () => go(-1));

    // Click a side slide → bring to front (don’t open modal yet)
    slides.forEach((el, idx) => {
      el.addEventListener("click", (e) => {
        if (idx !== i) {
          e.preventDefault(); // stops "#" link / modal on side slides
          i = idx;
          render();
        }
        // if idx === i the inner <a> will trigger the Bootstrap modal as usual
      });
    });

    // Pause on hover / resume on leave
    root.addEventListener("pointerenter", stopAuto);
    root.addEventListener("pointerleave", startAuto);

    // Also pause when any flyer modal is open
    document.addEventListener("shown.bs.modal", stopAuto);
    document.addEventListener("hidden.bs.modal", startAuto);

    // Reflow when images load so initial layout is perfect
    slides.forEach((el) => {
      const img = el.querySelector("img");
      if (img && !img.complete) {
        img.addEventListener("load", render, { once: true });
      }
    });

    // Kickoff
    render();
    startAuto();
  });
})();
