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
const urls = window.urls;

// EVENT HANDLERS
const eventForm = document.getElementById('event-form');
eventForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const saveBtn = eventForm.querySelector('button[type="submit"]');
  saveBtn.disabled = true;

  const classId = document.getElementById('event-class').value;
  const startDate = new Date(document.getElementById('event-date').value);
  const startTime = document.getElementById('event-start').value;
  const endTime = document.getElementById('event-end').value;
  const recurrence = document.getElementById('event-recurrence').value;
  const daysOfWeekRaw = document.getElementById('event-days').value;
  const exceptions = document.getElementById('event-exceptions').value;
  const repeatUntilStr = document.getElementById('event-repeat-until').value;
  const repeatUntil = repeatUntilStr ? new Date(repeatUntilStr).toISOString().split('T')[0] : null;
  const eventId = document.getElementById('event-id').value;
  const url = eventId ? urls.updateEvent(eventId) : urls.createEvent;

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({
        class_id: classId,
        date: startDate.toISOString().split('T')[0],
        start_time: startTime,
        end_time: endTime,
        recurrence: recurrence,
        days_of_week: daysOfWeekRaw,
        recurrence_exceptions: exceptions,
        repeat_until: repeatUntil,
      })
    });

    if (res.ok) {
      eventForm.reset();
      document.getElementById('event-id').value = '';
      bootstrap.Modal.getInstance(document.getElementById('eventModal'))?.hide();
      location.reload();
    } else {
      alert('Error saving event.');
    }
  } catch (err) {
    console.error('Error submitting form:', err);
    alert('Unexpected error. Please try again.');
  } finally {
    saveBtn.disabled = false;
  }
});

// Modal open, edit, delete handlers
document.querySelector('#add-event-btn')?.addEventListener('click', () => {
  document.getElementById('event-id').value = '';
  eventForm.reset();
  new bootstrap.Modal(document.getElementById('eventModal')).show();
  setTimeout(() => document.getElementById('event-class')?.focus(), 500);
});

window.editEvent = function (id) {
  const row = document.querySelector(`tr[data-id="${id}"]`);
  if (!row) return;

  const fieldMap = {
    class: 'class',
    date: 'date',
    start: 'start',
    end: 'end',
    recurrence: 'recurrence',
    days: 'daysofweek',
    exceptions: 'recurrenceexceptions',
    'repeat-until': 'repeatuntil'
  };

  Object.entries(fieldMap).forEach(([field, dataKey]) => {
    const el = document.getElementById(`event-${field}`);
    if (el && row.dataset[dataKey] !== undefined) {
      el.value = row.dataset[dataKey];
    }
  });

  document.getElementById('event-id').value = id;
  new bootstrap.Modal(document.getElementById('eventModal')).show();
};

window.deleteEvent = async function(id) {
  if (!confirm('Delete this event?')) return;
  const res = await fetch(urls.deleteEvent(id), {
    method: 'POST',
    headers: { 'X-CSRFToken': csrftoken },
  });
  if (res.ok) document.querySelector(`tr[data-id='${id}']`)?.remove();
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
    headers: { 'X-CSRFToken': csrftoken },
  });
  if (res.ok) {
    document.querySelector(`tr[data-id='${id}']`)?.remove();
  }
};
