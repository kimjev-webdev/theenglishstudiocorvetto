// ===== CSRF cookie helper =====
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

/* ------------------------------------------------------------------ *
 * Toasts (Bootstrap 5)
 * ------------------------------------------------------------------ */
function ensureToastContainer() {
  let c = document.getElementById('toast-container');
  if (!c) {
    c = document.createElement('div');
    c.id = 'toast-container';
    c.className = 'position-fixed top-0 end-0 p-3';
    c.style.zIndex = '1080';
    document.body.appendChild(c);
  }
  return c;
}

function showToast(message, variant = 'success') {
  const container = ensureToastContainer();
  const wrapper = document.createElement('div');
  // Map variants to BS classes
  const bg = {
    success: 'bg-success text-white',
    danger: 'bg-danger text-white',
    warning: 'bg-warning',
    info: 'bg-info'
  }[variant] || 'bg-secondary text-white';

  wrapper.className = `toast align-items-center border-0 ${bg}`;
  wrapper.setAttribute('role', 'alert');
  wrapper.setAttribute('aria-live', 'assertive');
  wrapper.setAttribute('aria-atomic', 'true');
  wrapper.innerHTML = `
    <div class="d-flex">
      <div class="toast-body">${message}</div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
  `;
  container.appendChild(wrapper);
  const t = new bootstrap.Toast(wrapper, { delay: 2500 });
  t.show();
  wrapper.addEventListener('hidden.bs.toast', () => wrapper.remove());
}

/* ------------------------------------------------------------------ *
 * Fetch helper: JSON in/out + unified errors
 * ------------------------------------------------------------------ */
async function fetchJSON(url, options = {}) {
  const opts = {
    credentials: 'same-origin',
    headers: { 'X-CSRFToken': csrftoken, ...(options.headers || {}) },
    ...options
  };
  const res = await fetch(url, opts);
  let data = null;
  try { data = await res.json(); } catch { /* not JSON, leave null */ }

  // Prefer server's {ok:false,error} contract
  if (!res.ok || (data && data.ok === false)) {
    const msg = (data && (data.error || data.message)) || `HTTP ${res.status}`;
    const err = new Error(msg);
    err.status = res.status;
    err.payload = data;
    throw err;
  }
  return data || { ok: true, message: 'OK' };
}

/* ------------------------------------------------------------------ *
 * Helpers
 * ------------------------------------------------------------------ */
function buildEventPayloadFromForm() {
  // Keep raw string values to avoid TZ issues.
  const repeatUntilStr = document.getElementById('event-repeat-until').value; // "YYYY-MM-DD" | ""
  return {
    class_id: document.getElementById('event-class').value,
    date: document.getElementById('event-date').value,               // "YYYY-MM-DD"
    start_time: document.getElementById('event-start').value,        // "HH:MM"
    end_time: document.getElementById('event-end').value,            // "HH:MM"
    recurrence: document.getElementById('event-recurrence').value,   // e.g. "weekly"
    days_of_week: document.getElementById('event-days').value,       // "Mon,Wed,Fri"
    recurrence_exceptions: document.getElementById('event-exceptions').value, // "YYYY-MM-DD, YYYY-MM-DD"
    repeat_until: repeatUntilStr || null
  };
}

/* ------------------------------------------------------------------ *
 * EVENT HANDLERS
 * ------------------------------------------------------------------ */
const eventForm = document.getElementById('event-form');
eventForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const saveBtn = eventForm.querySelector('button[type="submit"]');
  saveBtn && (saveBtn.disabled = true);

  const eventId = document.getElementById('event-id').value;
  const url = eventId ? urls.updateEvent(eventId) : urls.createEvent;
  const payload = buildEventPayloadFromForm();

  try {
    const data = await fetchJSON(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    showToast(data.message || (eventId ? 'Event updated.' : 'Event created.'), 'success');

    // Reset + close modal then refresh to reflect table/calendar
    eventForm.reset();
    document.getElementById('event-id').value = '';
    const modalEl = document.getElementById('eventModal');
    bootstrap.Modal.getInstance(modalEl)?.hide();
    // If you have a client-side table refresh, call it here instead of reloading
    location.reload();
  } catch (err) {
    console.error('Event save failed:', err);
    const variant = err.status === 403 ? 'warning' : 'danger';
    const msg = err.message || 'Error saving event.';
    showToast(msg, variant);
  } finally {
    saveBtn && (saveBtn.disabled = false);
  }
});

// Modal open (add)
document.querySelector('#add-event-btn')?.addEventListener('click', () => {
  document.getElementById('event-id').value = '';
  eventForm?.reset();
  new bootstrap.Modal(document.getElementById('eventModal')).show();
  setTimeout(() => document.getElementById('event-class')?.focus(), 150);
});

// Modal open (edit)
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

// Delete event
window.deleteEvent = async function (id) {
  if (!confirm('Delete this event?')) return;
  try {
    const data = await fetchJSON(urls.deleteEvent(id), { method: 'POST' });
    document.querySelector(`tr[data-id='${id}']`)?.remove();
    showToast(data.message || 'Event deleted.', 'success');
  } catch (err) {
    console.error('Delete failed:', err);
    showToast(err.message || 'Failed to delete event.', 'danger');
  }
};

/* ------------------------------------------------------------------ *
 * CLASS HANDLERS
 * ------------------------------------------------------------------ */
const classForm = document.getElementById('class-form');
classForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const saveBtn = classForm.querySelector('button[type="submit"]');
  saveBtn && (saveBtn.disabled = true);

  const payload = {
    name_en: document.getElementById('class-name-en').value,
    name_it: document.getElementById('class-name-it').value,
    emoji: document.getElementById('class-emoji').value,
  };

  const id = document.getElementById('class-id').value;
  const url = id ? urls.updateClass(id) : urls.createClass;

  try {
    const res = await fetchJSON(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = res.data || res; // support either shape
    showToast(res.message || (id ? 'Class updated.' : 'Class created.'), 'success');

    if (id) {
      // Update the existing row without reloading
      const row = document.querySelector(`tr[data-id='${id}']`);
      if (row) {
        const cells = row.querySelectorAll('td');
        // assuming cols: emoji | name_en | name_it | actions
        cells[0].textContent = (data.emoji ?? payload.emoji ?? '').trim();
        cells[1].textContent = (data.name_en ?? payload.name_en ?? '').trim();
        cells[2].textContent = (data.name_it ?? payload.name_it ?? '').trim();
      }
      classForm.reset();
      document.getElementById('class-id').value = '';
    } else {
      // Simplest: refresh to show the new row
      location.reload();
    }
  } catch (err) {
    console.error('Class save failed:', err);
    const variant = err.status === 403 ? 'warning' : 'danger';
    showToast(err.message || 'Something went wrong while saving the class.', variant);
  } finally {
    saveBtn && (saveBtn.disabled = false);
  }
});

window.editClass = function (id) {
  const row = document.querySelector(`tr[data-id='${id}']`);
  if (!row) return;
  const cells = row.querySelectorAll('td');
  document.getElementById('class-id').value = id;
  document.getElementById('class-name-en').value = cells[1].textContent.trim();
  document.getElementById('class-name-it').value = cells[2].textContent.trim();
  document.getElementById('class-emoji').value = cells[0].textContent.trim();
};

window.deleteClass = async function (id) {
  if (!confirm('Delete this class?')) return;
  try {
    const res = await fetchJSON(urls.deleteClass(id), { method: 'POST' });
    document.querySelector(`tr[data-id='${id}']`)?.remove();
    showToast(res.message || 'Class deleted.', 'success');
  } catch (err) {
    console.error('Delete class failed:', err);
    showToast(err.message || 'Failed to delete class.', 'danger');
  }
};
