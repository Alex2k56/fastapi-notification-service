# 🚀 Enterprise Notification Dispatcher

Un microserviciu simplu și rapid construit cu **FastAPI**, creat pentru a gestiona și trimite notificări în fundal (asincron) fără a bloca aplicația principală.

---

## 📌 Ce știe să facă?

- **Trimitere în fundal (`BackgroundTasks`):** Notificările sunt procesate separat, iar utilizatorul primește un răspuns instant.
- **Sistem de priorități:**
  - `HIGH`: Procesare rapidă (~0.5s) pentru urgențe (ex: resetare parolă, coduri 2FA).
  - `LOW` / `MEDIUM`: Procesare normală (~1.5s) pentru e-mailuri promoționale sau notificări de sistem.
- **Logging structurat:** Fiecare notificare primește un `task_id` unic pentru a fi ușor de urmărit în consolă.
- **Documentație interactivă:** Swagger UI gata de utilizare direct din browser.

---

## 📁 Structura proiectului

```text
├── services/
│   └── notification_service.py  # Logica de livrare și procesare asincronă
├── config.py                    # Configurarea aplicației (nume, setări)
├── main.py                      # Punctul de intrare și rutele API
├── schemas.py                   # Validarea datelor (Pydantic Models & Enums)
└── .gitignore                   # Ignoră mediul virtual și fișierele temporare