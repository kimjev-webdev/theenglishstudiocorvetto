// main/static/js/flyers.js
(function () {
  function initCoverflow(root) {
    const track  = root.querySelector('.flyer-cf-track');
    const slides = Array.from(root.querySelectorAll('.flyer-cf-slide'));
    const prev   = root.querySelector('.cf-prev');
    const next   = root.querySelector('.cf-next');
    if (!track || slides.length < 3) return;

    let idx = 0;
    let timer = null;
    const gapFactor = 0.58;   // how much the side slides overlap (smaller = more overlap)
    const scaleStep = 0.08;   // scale drop per step away from center
    const maxSteps  = Math.floor(slides.length / 2);

    // Ensure the track reserves enough height
    const setHeight = () => {
      const h = Math.max(...slides.map(li => li.offsetHeight));
      track.style.height = h + 'px';
    };

    const layout = () => {
      const center = slides[idx];
      const slideW = center.offsetWidth || 400;
      const stepX  = slideW * gapFactor;

      slides.forEach((li, i) => {
        // compute shortest signed distance from current index (circular)
        let d = i - idx;
        if (d > slides.length / 2) d -= slides.length;
        if (d < -slides.length / 2) d += slides.length;

        const z = 100 - Math.abs(d);
        const s = Math.max(1 - Math.abs(d) * scaleStep, 0.7);
        const x = d * stepX;

        li.style.transform  = `translateX(${x}px) scale(${s})`;
        li.style.zIndex     = z;
        li.style.opacity    = Math.abs(d) > maxSteps ? 0 : 1;
        li.style.pointerEvents = (Math.abs(d) <= 1) ? 'auto' : 'none';
      });
    };

    const go = (delta) => {
      idx = (idx + delta + slides.length) % slides.length;
      layout();
    };

    // Nav
    prev && prev.addEventListener('click', e => { e.preventDefault(); stop(); go(-1); start(); });
    next && next.addEventListener('click', e => { e.preventDefault(); stop(); go(+1); start(); });

    // Click a side slide to focus it
    slides.forEach((li, i) => {
      li.addEventListener('click', (e) => {
        if (i === idx) return; // center slide -> let link open the modal
        e.preventDefault();
        stop();
        idx = i;
        layout();
        start();
      });
    });

    // Autoplay
    const delay = parseInt(root.getAttribute('data-autoplay') || '0', 10);
    const start = () => {
      if (!delay) return;
      stop();
      timer = setInterval(() => go(+1), delay);
    };
    const stop  = () => { if (timer) { clearInterval(timer); timer = null; } };
    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', start);

    // kick it off
    setHeight();
    layout();
    start();

    // Re-measure on resize
    window.addEventListener('resize', () => { setHeight(); layout(); });
  }

  // init every coverflow on page (desktop area)
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.flyer-cf').forEach(initCoverflow);
  });
})();
