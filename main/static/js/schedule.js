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

// Use window.urls injected via template
const urls = window.urls;

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
      const data = await res.json();

      if (id) {
        const row = document.querySelector(`tr[data-id='${id}']`);
        if (row) {
          row.dataset.classId = payload.class_id;
          row.dataset.date = payload.date;
          row.dataset.start = payload.start_time;
          row.dataset.end = payload.end_time;
          row.dataset.recurrence = payload.recurrence;
          row.dataset.days = payload.days_of_week;
          row.dataset.exceptions = payload.recurrence_exceptions;
        }
      } else {
        location.reload();
      }

      eventForm.reset();
      document.getElementById('event-id').value = '';
      bootstrap.Modal.getInstance(document.getElementById('eventModal'))?.hide();
    } else {
      alert('Failed to save event. Please check your inputs.');
    }
  } catch (err) {
    console.error('Error submitting form:', err);
    alert('Unexpected error. Please try again.');
  } finally {
    saveBtn.disabled = false;
  }
});

document.querySelector('#add-event-btn')?.addEventListener('click', () => {
  document.getElementById('event-id').value = '';
  eventForm.reset();
  const modal = new bootstrap.Modal(document.getElementById('eventModal'));
  modal.show();
  setTimeout(() => document.getElementById('event-class')?.focus(), 500);
});

window.editEvent = function (id) {
  // Select the specific row using data-id attribute
  const row = document.querySelector(`tr[data-id="${id}"]`);
  if (!row) return;

  // Populate modal fields from dataset
  document.getElementById('event-id').value = id;
  document.getElementById('event-class').value = row.dataset.classId;
  document.getElementById('event-date').value = row.dataset.date;
  document.getElementById('event-start').value = row.dataset.start;
  document.getElementById('event-end').value = row.dataset.end;
  document.getElementById('event-recurrence').value = row.dataset.recurrence || 'none';
  document.getElementById('event-days').value = row.dataset.days || '';
  document.getElementById('event-exceptions').value = row.dataset.exceptions || '';

  // Show modal
  new bootstrap.Modal(document.getElementById('eventModal')).show();
};

window.deleteEvent = async function(id) {
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
};

// CLASS HANDLERS
const classForm = document.getElementById('class-form');
classForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const saveBtn = classForm.querySelector('button[type="submit"]');
  saveBtn.disabled = true;

  const payload = {
    name_en: document.getElementById('class-name-en').value,
    name_it: document.getElementById('class-name-it').value,
    emoji: document.getElementById('class-emoji').value,
  };

  const id = document.getElementById('class-id').value;
  const url = id ? urls.updateClass(id) : urls.createClass;

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
      const data = await res.json();

      if (id) {
        const row = document.querySelector(`tr[data-id='${id}']`);
        if (row) {
          row.querySelector('td:nth-child(1)').textContent = data.emoji;
          row.querySelector('td:nth-child(2)').textContent = data.name_en;
          row.querySelector('td:nth-child(3)').textContent = data.name_it;
        }
      } else {
        location.reload();
      }

      classForm.reset();
      document.getElementById('class-id').value = '';
    } else {
      alert('Something went wrong while saving the class.');
    }
  } catch (err) {
    console.error('Error saving class:', err);
    alert('Unexpected error. Please try again.');
  } finally {
    saveBtn.disabled = false;
  }
});

window.editClass = function(id) {
  const row = document.querySelector(`tr[data-id='${id}']`);
  if (!row) return;
  const cells = row.querySelectorAll('td');
  document.getElementById('class-id').value = id;
  document.getElementById('class-name-en').value = cells[1].textContent.trim();
  document.getElementById('class-name-it').value = cells[2].textContent.trim();
  document.getElementById('class-emoji').value = cells[0].textContent.trim();
};

window.deleteClass = async function(id) {
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
};
