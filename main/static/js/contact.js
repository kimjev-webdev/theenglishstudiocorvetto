/* jshint esversion: 6, node: true, devel: true, asi: true */
/* jshint -W030, -W033 */

document.addEventListener("DOMContentLoaded", function () {
  const thankYouModal = document.getElementById("thankYouModal");

  if (thankYouModal && thankYouModal.dataset.show === "true") {
    const modal = new bootstrap.Modal(thankYouModal);
    modal.show();
  }
});
