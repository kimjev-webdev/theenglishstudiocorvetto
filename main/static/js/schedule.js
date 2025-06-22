// CSRF helper
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Toggle event form
function toggleEventForm() {
  document.getElementById('event-form').classList.toggle('d-none');
}

// EVENT HANDLERS
const eventForm = document.getElementById('event-form');
eventForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    class_id: document.getElementById('event-class').value,
    date: document.getElementById('event-date').value,
    start_time: document.getElementById('event-start').value,
    end_time: document.getElementById('event-end').value,
    recurrence: document.getElementById('event-recurrence').value,
    days_of_week: document.getElementById('event-days').value,
  };
  const id = document.getElementById('event-id').value;
  const url = id ? `/events/${id}/edit/` : '/events/create/';
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(payload)
  });
  if (res.ok) location.reload();
});

function editEvent(id) {
  const row = document.querySelector(`tr[data-id='${id}']`);
  const cells = row.querySelectorAll('td');
  document.getElementById('event-id').value = id;
  document.getElementById('event-class').value = cells[0].dataset.classId || '';
  document.getElementById('event-date').value = cells[1].textContent.trim();
  document.getElementById('event-start').value = cells[2].textContent.trim();
  document.getElementById('event-end').value = cells[3].textContent.trim();
  document.getElementById('event-recurrence').value = cells[4].textContent.trim();
  toggleEventForm();
}

async function deleteEvent(id) {
  if (!confirm('Delete this event?')) return;
  const res = await fetch(`/events/${id}/delete/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  });
  if (res.ok) location.reload();
}

// CLASS HANDLERS
const classForm = document.getElementById('class-form');
classForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    name_en: document.getElementById('class-name-en').value,
    name_it: document.getElementById('class-name-it').value,
    emoji: document.getElementById('class-emoji').value,
  };
  const id = document.getElementById('class-id').value;
  const url = id ? `/classes/${id}/edit/` : '/classes/create/';
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(payload)
  });
  if (res.ok) location.reload();
});

function editClass(id) {
  const row = document.querySelector(`tr[data-id='${id}']`);
  const cells = row.querySelectorAll('td');
  document.getElementById('class-id').value = id;
  document.getElementById('class-name-en').value = cells[1].textContent.trim();
  document.getElementById('class-name-it').value = cells[2].textContent.trim();
  document.getElementById('class-emoji').value = cells[0].textContent.trim();
}

async function deleteClass(id) {
  if (!confirm('Delete this class?')) return;
  const res = await fetch(`/classes/${id}/delete/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  });
  if (res.ok) location.reload();
}