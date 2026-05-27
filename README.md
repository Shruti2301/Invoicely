# ⚡ Invoicely

> Clean, beautiful invoices for startups. No accounts. No subscriptions. Just ship.

![Invoicely](https://img.shields.io/badge/built%20with-Flask-c9727a?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11-6b4c3b?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-f2d4c2?style=flat-square)

---

## ✨ What is Invoicely?

Invoicely is a free, minimal invoice generator built for early-stage startups and founders. Stop wrestling with Google Docs or paying $20/month for a tool that does one thing. Fill in your details, add your line items, and get a beautiful PDF invoice in seconds.

If you're a founder who sends invoices, this is for you.
Try it → [Invoicely](YOUR_RENDER_URL_HERE)
---

## 🌸 Features

- **No account needed** — open it and go
- **Beautiful warm UI** — designed to feel calm and professional
- **Multiple line items** — add as many services as you need
- **Auto-calculates totals** — no manual math
- **Print / Save as PDF** — one click, done
- **Mobile friendly** — works on any screen size

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| Templating | Jinja2 |
| Frontend | Vanilla HTML, CSS, JavaScript |
| PDF Export | Browser `window.print()` |
| Deployment | Render |

---

## 🚀 Run it locally

**1. Clone the repo**
```bash
git clone https://github.com/Shruti2301/invoicely.git
cd invoicely
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open your browser**
```
http://localhost:5000
```

---

## 📁 Project Structure

```
invoicely/
├── app.py                  # Flask backend — routes and logic
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Invoice form page
│   └── invoice.html        # Generated invoice page
├── static/
│   ├── css/
│   │   └── style.css       # Warm, minimal styling
│   └── js/
│       └── main.js         # Dynamic line item rows
└── README.md
```

---

## 💡 How it works

1. User fills in **From**, **To**, invoice number, due date and line items
2. Form submits via `POST` to `/generate` in `app.py`
3. Flask calculates totals and renders `invoice.html` with the data
4. User clicks **Print / Save as PDF** to download

---

## 🗺️ Roadmap

- [ ] Email invoice directly to client
- [ ] Add company logo upload
- [ ] Tax calculation support
- [ ] Invoice history (local storage)
- [ ] Dark mode
- [ ] Multiple currencies

---

## 🤍 Built by

**Shruti Mandaokar** — built and shipped in one night in the Bay Area.


---

## 📄 License

MIT — free to use, fork, and build on.

---

*Made with love, Flask, and way too much coffee ☕*
