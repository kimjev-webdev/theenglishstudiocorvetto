/* jshint esversion: 6, node: true, devel: true, asi: true */
/* jshint -W030, -W033 */

(function () {
  function shouldShowModal(el) {
    if (!el) return false;
    // Accept both dataset.show and data-show, normalize and compare
    const raw =
      (el.dataset && el.dataset.show) ||
      el.getAttribute('data-show') ||
      '';
    return String(raw).toLowerCase() === 'true';
  }

  function tryShowThankYou() {
    const el = document.getElementById('thankYouModal');
    if (!shouldShowModal(el)) return;

    // Only proceed if Bootstrap Modal is available
    if (window.bootstrap && window.bootstrap.Modal) {
      new bootstrap.Modal(el).show();
    } else {
      // Bootstrap not ready yet; try again at window.load
      window.addEventListener('load', () => {
        if (window.bootstrap && window.bootstrap.Modal) {
          new bootstrap.Modal(el).show();
        }
      }, { once: true });
    }
  }

  // Try early (DOM ready) in case Bootstrap is already loaded
  document.addEventListener('DOMContentLoaded', tryShowThankYou);

  // Also try on full load as a fallback (mirrors your bullet-proof version)
  window.addEventListener('load', tryShowThankYou);
})();
