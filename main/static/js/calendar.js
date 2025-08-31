document.addEventListener('DOMContentLoaded', function () {
  tippy('.day[data-tippy-content]', {
    placement: 'top',
    animation: 'fade',
    arrow: false,
    delay: [100, 100],
    allowHTML: true,
    maxWidth: 240,
    appendTo: () => document.body,
    theme: 'custom',
    interactive: true,
    zIndex: 9999,
  });
});
