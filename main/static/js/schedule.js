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

// EVENT HANDLERS
const eventForm = document.getElementById('event-form');
eventForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const saveBtn = eventForm.querySelector('button[type="submit"]');
  saveBtn.disabled = true;

  const payload = {
    class_id: document.getElementById('event-class').value,
    date: document.getElementById('event-date').value,
    start_time: document.getElementById('event-start').value,
    end_time: document.getElementById('event-end').value,
    recurrence: document.getElementById('event-recurrence').value,
    days_of_week: document.getElementById('event-days').value,
    recurrence_exceptions: document.getElementById('event-exceptions').value,
  };

  const id = document.getElementById('event-id').value;
  const url = id ? urls.updateEvent(id) : urls.createEvent;

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      location.reload();
    } else {
      alert('Failed to save event. Please check your inputs.');
      saveBtn.disabled = false;
    }
  } catch (err) {
    console.error('Error submitting form:', err);
    alert('Unexpected error. Please try again.');
    saveBtn.disabled = false;
  }
});

// Open empty modal with autofocus
document.querySelector('#add-event-btn')?.addEventListener('click', () => {
  document.getElementById('event-id').value = '';
  eventForm.reset();
  const modal = new bootstrap.Modal(document.getElementById('eventModal'));
  modal.show();
  setTimeout(() => document.getElementById('event-class')?.focus(), 500);
});

function editEvent(id) {
  const row = document.querySelector(`tr[data-id='${id}']`);
  if (!row) return;
  document.getElementById('event-id').value = id;
  document.getElementById('event-class').value = row.dataset.classId || '';
  document.getElementById('event-date').value = row.dataset.date || '';
  document.getElementById('event-start').value = row.dataset.start || '';
  document.getElementById('event-end').value = row.dataset.end || '';
  document.getElementById('event-recurrence').value = row.dataset.recurrence || '';
  document.getElementById('event-days').value = row.dataset.days || '';
  document.getElementById('event-exceptions').value = row.dataset.exceptions || '';
  new bootstrap.Modal(document.getElementById('eventModal')).show();
}

async function deleteEvent(id) {
  if (!confirm('Delete this event?')) return;
  const res = await fetch(urls.deleteEvent(id), {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  });
  if (res.ok) {
    document.querySelector(`tr[data-id='${id}']`)?.remove();
  }
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
  const url = id ? urls.updateClass(id) : urls.createClass;
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(payload)
  });
  if (res.ok) {
    location.reload();
  }
});

function editClass(id) {
  const row = document.querySelector(`tr[data-id='${id}']`);
  if (!row) return;
  const cells = row.querySelectorAll('td');
  document.getElementById('class-id').value = id;
  document.getElementById('class-name-en').value = cells[1].textContent.trim();
  document.getElementById('class-name-it').value = cells[2].textContent.trim();
  document.getElementById('class-emoji').value = cells[0].textContent.trim();
}

async function deleteClass(id) {
  if (!confirm('Delete this class?')) return;
  const res = await fetch(urls.deleteClass(id), {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  });
  if (res.ok) {
    document.querySelector(`tr[data-id='${id}']`)?.remove();
  }
}