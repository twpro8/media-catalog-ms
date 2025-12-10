<h1 align="center">Media Catalog</h1>

<br>

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54" alt="Python" />
    <img src="https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi" alt="FastAPI" />
    <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=flat&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <br>
    <img src="https://img.shields.io/badge/sqlalchemy-%23D71F00.svg?style=flat&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
    <img src="https://img.shields.io/badge/pydantic-%23E92063.svg?style=flat&logo=pydantic&logoColor=white" alt="Pydantic" />
    <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=flat&logo=redis&logoColor=white" alt="Redis" />
    <img src="https://img.shields.io/badge/pytest-%23ffffff.svg?style=flat&logo=pytest&logoColor=2f9fe3" alt="Pytest" />
    <br>
    <img src="https://img.shields.io/badge/-Swagger-%23Clojure?style=flat&logo=swagger&logoColor=white" alt="Swagger" />
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/uv-%23DE5FE9.svg?style=flat&logo=uv&logoColor=white" alt="uv"  alt="SQLAlchemy" />
    <br>
    <img src="https://img.shields.io/github/license/Ileriayo/markdown-badges?style=Flat" alt="License" />
</p>

<br><br>

A service for managing a media catalog, built with **FastAPI**, **PostgreSQL**, and **Docker Compose** for easy setup and deployment.  

This service provides a ready-to-run backend with database migrations and secure non-root execution.

## 🚀 Quickstart

<hr>

### Requirements

* Docker 28+
* Docker Compose 2+
* Git

<hr>

### 📥 Clone the repository

```bash
git clone https://github.com/twpro8/media-catalog-ms
cd media-catalog-ms
```

<hr>

### 🔐 Environment variables

Create root `.env`:

```bash
cp .env-example .env
```

<hr>

### ▶️ Build and run the application

```bash
docker compose up --build -d
```

<hr>

### 🌍 URLs
|              |                                                          |
|--------------|----------------------------------------------------------|
| Base URL     | [http://127.0.0.1:8000](http://127.0.0.1:8000)           |
| Swagger Docs | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |

---

### 🔍 View logs

```bash
docker compose logs -f
```

<hr>

### Stop

```bash
docker compose down
```

To remove local data as well:

```bash
docker compose down -v
```

<hr>

### Check running containers

```bash
docker ps
```

<hr>

🎉 Congratulations! Media Catalog MS is now up and running on your machine! 🎉
