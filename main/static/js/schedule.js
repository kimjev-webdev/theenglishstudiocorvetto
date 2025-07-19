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
  const eventId = document.getElementById('event-id').value;
  const url = eventId ? urls.updateEvent(eventId) : urls.createEvent;

  const dayNameToIndex = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
  const daysOfWeek = daysOfWeekRaw.split(',').map(d => dayNameToIndex[d.trim()]).filter(d => !isNaN(d));

  const eventsToCreate = [];

  if (recurrence === 'none' || eventId) {
    eventsToCreate.push(startDate.toISOString().split('T')[0]);
  } else {
    let current = new Date(startDate);
    const endLimit = new Date(current);
    endLimit.setMonth(endLimit.getMonth() + 3); // 3-month cap

    while (current <= endLimit) {
      if (daysOfWeek.includes(current.getDay())) {
        eventsToCreate.push(current.toISOString().split('T')[0]);
      }
      current.setDate(current.getDate() + 1);
    }
  }

  try {
    const responses = await Promise.all(eventsToCreate.map(date =>
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
          class_id: classId,
          date: date,
          start_time: startTime,
          end_time: endTime,
          recurrence: recurrence,
          days_of_week: daysOfWeekRaw,
          recurrence_exceptions: exceptions,
        })
      })
    ));

    if (responses.every(res => res.ok)) {
      eventForm.reset();
      document.getElementById('event-id').value = '';
      bootstrap.Modal.getInstance(document.getElementById('eventModal'))?.hide();
      location.reload();
    } else {
      alert('Some events failed to save.');
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
  const row = document.querySelector(`tr[data-id="${id}"]`);
  if (!row) return;

  document.getElementById('event-id').value = id;
  document.getElementById('event-class').value = row.dataset.classId;
  document.getElementById('event-date').value = row.dataset.date;
  document.getElementById('event-start').value = row.dataset.start;
  document.getElementById('event-end').value = row.dataset.end;
  document.getElementById('event-recurrence').value = row.dataset.recurrence || 'none';
  document.getElementById('event-days').value = row.dataset.days || '';
  document.getElementById('event-exceptions').value = row.dataset.exceptions || '';
  new bootstrap.Modal(document.getElementById('eventModal')).show();
};

window.deleteEvent = async function(id) {
  if (!confirm('Delete this event?')) return;
  const res = await fetch(urls.deleteEvent(id), {
    method: 'POST',
    headers: { 'X-CSRFToken': csrftoken },
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
    headers: { 'X-CSRFToken': csrftoken },
  });
  if (res.ok) {
    document.querySelector(`tr[data-id='${id}']`)?.remove();
  }
};
