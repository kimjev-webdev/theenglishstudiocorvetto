// main/static/js/flyers.js
document.addEventListener('DOMContentLoaded', () => {
  const wrap  = document.querySelector('.flyer-cf');
  if (!wrap) return;

  const track = wrap.querySelector('.flyer-cf-track');
  const slides = Array.from(wrap.querySelectorAll('.flyer-cf-slide'));
  const prev  = wrap.querySelector('.cf-prev');
  const next  = wrap.querySelector('.cf-next');

  let index = 0;
  let timer = null;
  const autoplayMs = parseInt(wrap.getAttribute('data-autoplay') || '0', 10) || 0;

  // distance between centres of slides (responsive)
  function spacing() {
    const w = track.clientWidth;
    return Math.min(Math.max(w * 0.32, 180), 360); // 180..360px
  }

  function render() {
    const s = spacing();
    slides.forEach((el, i) => {
      const d = i - index;                 // relative offset from active
      const x = d * s;                      // horizontal push
      const a = Math.min(Math.abs(d), 3);   // clamp off-screen slides
      const scale = 1 - a * 0.12;           // step down 12% each side
      const opacity = 1 - Math.min(Math.abs(d) * 0.18, 0.6);
      const z = 100 - Math.abs(d);          // keep centre above arrows? we'll set arrows higher via CSS

      el.style.zIndex = z;
      el.style.opacity = String(opacity);
      // left:50% in CSS + translateX(-50%) keeps the centre slide truly centred
      el.style.transform = `translateX(${x}px) translateX(-50%) scale(${scale})`;
    });
  }

  function step(dir) {
    index = (index + dir + slides.length) % slides.length;
    render();
  }

  function start() {
    if (!autoplayMs) return;
    timer = setInterval(() => step(1), autoplayMs);
  }

  function stop() {
    if (timer) clearInterval(timer);
    timer = null;
  }

  prev?.addEventListener('click', () => { stop(); step(-1); start(); });
  next?.addEventListener('click', () => { stop(); step(1);  start(); });

  window.addEventListener('resize', render);

  // init
  render();
  start();
});
