// main/static/js/flyers.js
document.addEventListener('DOMContentLoaded', () => {
  const root = document.querySelector('.flyer-cf');
  if (!root) return;

  const track  = root.querySelector('.flyer-cf-track');
  const slides = Array.from(track.querySelectorAll('.flyer-cf-slide'));
  const prevBtn = root.querySelector('.cf-prev');
  const nextBtn = root.querySelector('.cf-next');

  const N = slides.length;
  if (N < 3) return; // desktop carousel only runs with 3+

  // ---- Tunables ---------------------------------------------------
  const VISIBLE_PER_SIDE = Math.min(2, Math.floor((N - 1) / 2)); // neighbors each side
  const BASE_OFFSET = 260;     // px shift for the first neighbor
  const GAP_SHRINK  = 0.86;    // spacing reduces as you go outward
  const SCALE_STEP  = 0.88;    // scale for each step away from center
  const OPACITY_BASE = 0.95;   // center neighbors start near-opaque
  const OPACITY_STEP = 0.15;   // fade as you go outward
  // -----------------------------------------------------------------

  let idx = 0; // active (center) slide index
  let timer = null;
  const delay = parseInt(root.dataset.autoplay || '0', 10) || 0;

  function offsetForStep(k) {
    // sum a geometric series to get nice even spacing
    let x = 0;
    for (let j = 1; j <= k; j++) x += BASE_OFFSET * Math.pow(GAP_SHRINK, j - 1);
    return x;
  }

  function place(el, x, scale, opacity, z, interactive) {
    // Anchor by center, then push left/right, then scale
    el.style.transform = `translateX(-50%) translateX(${x}px) scale(${scale})`;
    el.style.zIndex = String(z);
    el.style.opacity = String(opacity);
    el.style.pointerEvents = interactive ? 'auto' : 'none';
  }

  function layout() {
    const ZCENTER = 1000;
    slides.forEach((el, i) => {
      const rel = ((i - idx) % N + N) % N; // 0..N-1 relative to center
      if (rel === 0) {
        // Center
        place(el, 0, 1, 1, ZCENTER, true);
        return;
      }

      // Right side neighbors: 1..VISIBLE_PER_SIDE
      if (rel <= VISIBLE_PER_SIDE) {
        const k = rel;
        const x = offsetForStep(k);
        const s = Math.pow(SCALE_STEP, k);
        const o = Math.max(0, OPACITY_BASE - OPACITY_STEP * (k - 1));
        place(el, +x, s, o, ZCENTER - k, true);
        return;
      }

      // Left side neighbors: N-1 .. N-VISIBLE_PER_SIDE
      if (rel >= N - VISIBLE_PER_SIDE) {
        const k = N - rel;
        const x = offsetForStep(k);
        const s = Math.pow(SCALE_STEP, k);
        const o = Math.max(0, OPACITY_BASE - OPACITY_STEP * (k - 1));
        place(el, -x, s, o, ZCENTER - k, true);
        return;
      }

      // Everything else: hide (still in DOM to keep loop smooth)
      place(el, 0, 0.6, 0, 0, false);
    });
  }

  function next() { idx = (idx + 1) % N; layout(); }
  function prev() { idx = (idx - 1 + N) % N; layout(); }

  // Controls
  nextBtn?.addEventListener('click', next);
  prevBtn?.addEventListener('click', prev);

  // Click a non-center slide -> bring to front
  slides.forEach((el, i) => {
    el.addEventListener('click', () => {
      if (i === idx) return;
      // find shortest direction
      const rightSteps = ((i - idx) % N + N) % N;
      const leftSteps  = N - rightSteps;
      if (rightSteps <= leftSteps) {
        idx = (idx + rightSteps) % N;
      } else {
        idx = (idx - leftSteps + N) % N;
      }
      layout();
    });
  });

  // Autoplay (pause on hover)
  function start() { if (delay > 0 && !timer) timer = setInterval(next, delay); }
  function stop()  { if (timer) clearInterval(timer), (timer = null); }
  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);

  // Keyboard (desktop)
  root.setAttribute('tabindex', '0');
  root.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') prev();
    if (e.key === 'ArrowRight') next();
  });

  // Init
  layout();
  start();
});
