// Example usage of the globals defined above

function getCSRFToken() {
  return window.csrfToken;
}

function createClass(data) {
  return fetch(window.urls.createClass, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCSRFToken(),
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
}

// same idea for updateClass, deleteClass, createEvent, etc.
