# TESTING

## 1. About Testing
The English Studio website has undergone extensive manual testing to ensure functionality, accessibility, and a smooth UX across devices. This document records **methods**, **steps**, and **results** for each area.

- Codebase validated where applicable (HTML/CSS), and forms & views tested end-to-end.
- Non-technical testers used the live site to simulate real usage.
- Particular focus areas: **Calendar & Recurrence**, **Contact + Mailchimp**, **Blog CRUD**, **Flyers ordering**, **Portal auth**.
- A detailed bug/change log is maintained in **BUGLOG.md**.

---

## 2. Validation <a id="validation"></a>

### HTML (W3C HTML5)
**Method:** https://validator.w3.org/  
**Scope:** `index.html`, `blog_list.html`, `blog_detail.html`, `calendar.html`, `contact.html`, `base.html`, and any portal templates you expose publicly.  
**Result:** _<paste summary + key screenshots/notes>_

### CSS (W3C Jigsaw)
**Method:** https://jigsaw.w3.org/css-validator/  
**Scope:** All compiled CSS served in production (include any Bootstrap overrides).  
**Result:** _<paste summary>_

### Links (W3C Link Checker)
**Method:** https://validator.w3.org/checklink  
**Scope:** Public pages (Home, Blog, Schedule, Contact, Privacy).  
**Result:** _<paste summary>_

### JavaScript Console
**Method:** Chrome DevTools → Console on each public page + portal pages.  
**Scope:** Carousel interactions, tooltips, calendar navigation, portal forms (fetch).  
**Result:** _<paste summary of errors/warnings found or “none”>_

### Accessibility (Lighthouse)
**Method:** Chrome DevTools → Lighthouse (Desktop & Mobile)  
**Scope:** Home, Blog Detail, Calendar, Contact  
**Record:** Accessibility, Performance, Best Practices, SEO  
**Result:** _<scores + notes + screenshots>_

---

## 3. Mobile & Desktop Testing <a id="mobiletesting"></a>

ADD MOBILE TESTING TABLE HERE


### Browser Compatibility
| Page / Feature | Chrome | Safari | Firefox | Edge | Notes |
|----------------|--------|--------|---------|------|-------|
| Home (carousel, i18n flags) | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop pc |
| Blog list/detail | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop pc |
| Calendar (month nav, tooltips) | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop pc |
| Portal login/dashboard | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop pc |
| Portal blog/flyers/schedule forms | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop pc |

---

## 4. Manual Testing <a id="manual"></a>

> Fill Expected vs Actual for each test. Attach screenshots where helpful.

### A. Internationalization (EN/IT)
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Click IT flag on Home | All content switches to Italian | _ | _ | _ |
| Switch EN→IT on Blog List & Detail | Titles/bodies follow locale | _ | _ | _ |
| Switch EN→IT on Calendar | Class names reflect chosen locale | _ | _ | _ |

### B. Homepage (carousel, classes section, flyers feed)
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Carousel auto/arrow nav | Smooth transition, no console errors | _ | _ | _ |
| Class icons (AI icons) | Icons visible; labels readable | _ | _ | _ |
| Flyers order | Matches `sort_order` (portal) | _ | _ | _ |

### C. Blog (public)
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Blog list shows cards | Title, image, date visible | _ | _ | _ |
| Card → detail | Slugged URL, content + media loads | _ | _ | _ |
| Prev/Next links | Navigate chronologically | _ | _ | _ |

### D. Schedule (public calendar)
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Month navigation | Previous/next months load | _ | _ | _ |
| Emoji per event | Emojis show in correct dates | _ | _ | _ |
| Tooltip on hover/tap | Shows one or multiple events for that date | _ | _ | _ |
| Recurrence display | Weekly/biweekly/monthly instances generated | _ | _ | _ |
| Exceptions | Skipped dates are **not** shown | _ | _ | _ |

### E. Contact + Newsletter + Map
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Submit valid form | Success message; redirect with `?sent=1` | _ | _ | _ |
| Email delivery | Email received with correct `reply_to` | _ | _ | _ |
| Mailchimp opt-in checked | Subscriber added to list | _ | _ | _ |
| Mailchimp opt-in unchecked | No list entry created | _ | _ | _ |
| Invalid form | Errors shown; no submission | _ | _ | _ |
| Google Map loads | Custom pin visible; no console API errors | _ | _ | _ |

### F. Portal: Authentication & Security
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Visit `/portal/` logged out | Redirect to login | _ | _ | _ |
| Login valid user | Dashboard visible | _ | _ | _ |
| Logout | Session cleared; login required again | _ | _ | _ |
| Password reset | Reset email flow works (templates render) | _ | _ | _ |
| Direct access to portal sub-routes when logged out | Redirects to login | _ | _ | _ |

### G. Portal: Blog CRUD
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Create blog post (EN/IT) | Saved; appears in list | _ | _ | _ |
| Upload image/video (Cloudinary) | Media previews; loads on detail | _ | _ | _ |
| Edit / delete | Updates persist | _ | _ | _ |
| Draft vs Published | Draft hidden from public; Published visible | _ | _ | _ |

### H. Portal: Flyers CRUD & Reordering
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Create flyer (EN/IT) | Saved; can upload image/PDF | _ | _ | _ |
| Toggle `publish` | Appears/disappears on Home | _ | _ | _ |
| Change `sort_order` | Home list updates to new order | _ | _ | _ |

### I. Portal: Classes & Events (Recurrence)
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Create Class (EN/IT, emoji) | Visible in event form + calendar | _ | _ | _ |
| Create Event (one-time) | Displays on selected date | _ | _ | _ |
| Create Event (weekly/biweekly/monthly) | All instances appear correctly | _ | _ | _ |
| Custom days (days_of_week) | Instances generated on chosen weekdays | _ | _ | _ |
| Add Exceptions | Exception dates omitted | _ | _ | _ |
| Edit/Delete event | Calendar updates accordingly | _ | _ | _ |

### J. User Management (Django Auth)
| Step | Expected | Actual | Pass | Notes |
|-----|----------|--------|------|------|
| Create user (staff) | Can log into portal | _ | _ | _ |
| Change permissions | Access reflects new roles | _ | _ | _ |
| Delete user | Access revoked, can’t login | _ | _ | _ |

---

## 5. User Story Testing <a id="user"></a>

Map each story in the README to concrete tests above.

| User Story | Covered By |
|------------|------------|
| Teacher updates monthly schedule (recurrence & exceptions) | D + I |
| Parent browses events with child | A + C + D |
| Owner manages posts/events/flyers in portal | F + G + H + I |
| Student finds IELTS/Business classes & contacts | C + D + E |
| Sponsor/partner reviews professionalism | A + C + D + E |
| Visitor selects contact category & subscribes | E |
| Newsletter subscriber receives updates | E |

_Add any extra stories you listed and link to the table rows above._

---

## 6. Performance (Lighthouse)
Run Lighthouse (Mobile + Desktop) on: Home, Blog Detail, Calendar, Contact.  
Record scores and any remediation done.

| Page | Perf | Access | Best Prac | SEO | Notes/Actions |
|------|------|--------|-----------|-----|---------------|
| Home | _ | _ | _ | _ | _ |
| Blog Detail | _ | _ | _ | _ | _ |
| Calendar | _ | _ | _ | _ | _ |
| Contact | _ | _ | _ | _ | _ |

---

## 7. Known Issues & Bug Log
- See **BUGLOG.md** for the full log and unresolved items.
- Outstanding issues (snapshot):  
  - _<list any still-open bugs here>_

---

## 8. Automated Testing (Optional / Not Configured Yet)
> You do **not** currently have unit tests or CI configured in this repo. If you add them later:

### Django Unit Tests
```bash
python manage.py test
# or keep DB between runs
python manage.py test --keepdb
