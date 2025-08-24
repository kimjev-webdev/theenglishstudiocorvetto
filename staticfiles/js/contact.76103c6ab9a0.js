document.addEventListener("DOMContentLoaded", function () {
  const thankYouModal = document.getElementById("thankYouModal");

  if (thankYouModal && thankYouModal.dataset.show === "true") {
    const modal = new bootstrap.Modal(thankYouModal);
    modal.show();
  }
});
