# CRUD API — (create/read/update/delete)

> **A minimal, elegant REST API built with Flask — engineered for readability, testability, and fast iteration.**

---

## About This Project

A thoughtfully crafted **CRUD API** that favors **clarity over complexity**. It demonstrates a clean Flask setup, well-defined routes, predictable error handling, and a compact test suite. Perfect as a starter for production-grade microservices or as a learning piece to showcase back-end fundamentals.

**Highlights**

* **Crystal‑clear CRUD** endpoints with a simple resource model.
* **Predictable responses** with consistent error shapes.
* **Tight feedback loop** using `pytest` for fast unit/integration tests.
* **HTTP client examples** powered by `requests` to validate flows end‑to‑end.
* **Lightweight footprint** with only the essentials.

> **Built by:**  — Pedro Motta.\\

---

## Requirements (Pinned)

```txt
Flask==2.3.0
Werkzeug==2.3.0
requests==2.31.0
pytest==7.4.3
```

version that i used.

---

## API 

**Base URL:** `http://127.0.0.1:5000`

| Method | Path          | Description       |
| ------ | ------------- | ----------------- |
| POST   | `/items`      | Create a new item |
| GET    | `/items`      | List all items    |
| GET    | `/items/<id>` | Get item by ID    |
| PUT    | `/items/<id>` | Update item by ID |
| DELETE | `/items/<id>` | Delete item by ID |


## Design Notes

* **Simplicity first.** Small surface area; each module has a single responsibility.
* **Consistent JSON.** Every response (success/error) uses a predictable shape.
* **Version pinning.** Reproducible installs for local and CI.
* **Testability.** `create_app()` pattern enables isolated app instances per test.

---

## &#x20;Contact

&#x20;— Back-end Developer (Python/Flask)

* GitHub: [https://github.com/pedromottadev/](https://github.com/pedromottadev/)
* LinkedIn: [https://www.linkedin.com/in/pedro-motta-6481b4245/](https://www.linkedin.com/in/pedro-motta-6481b4245/)
* Email: [pedromarquesmotta@gmail.com](mailto:pedromarquesmotta@gmail.com)

---

##
