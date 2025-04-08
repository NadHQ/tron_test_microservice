# 🧠 Tron Wallet Info Microservice

## 📌 Описание

Микросервис, написанный с использованием FastAPI, предоставляет информацию о кошельке в сети Tron — текущий баланс TRX, доступный **bandwidth** и **energy**.
Сервис сохраняет каждый запрос в базу данных, включая адрес запрашиваемого кошелька.

---

## 🚀 Технологии

- Python 3.12
- FastAPI
- SQLAlchemy ORM
- Alembic (миграции)
- PostgreSQL (через Docker)
- TronPy (интеграция с сетью Tron)
- Pytest (юнит и интеграционные тесты)
- Docker + Docker Compose

---

## ⚙️ Запуск проекта

1. **Клонировать репозиторий:**

   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```

2. **Создать `.env` файл (если используется). Пример:**

   ```env
   DATABASE_USER=myuser
   DATABASE_PASSWORD=mypassword
   DATABASE_HOST=postgres_tron
   DATABASE_PORT=5432
   DATABASE_DB=tron

   DATABASE_URL=postgresql+asyncpg://myuser:mypassword@postgres_tron:5432/tron

   TRONGRID_API_KEY=<your_api_key>
   ```

3. **Запустить через Docker Compose:**

   ```bash
   docker-compose up --build
   ```

4. **Применить миграции:**

   ```bash
   docker-compose exec backend alembic upgrade head
   ```

---

## 📫 Эндпоинты

### `POST /v1/tron/check_adress`

Получение информации по адресу Tron.

#### 🔸 Пример запроса:

```json
{
  "address": "TRON_WALLET_ADDRESS"
}
```

#### 🔸 Пример ответа:

```json
{
  "address": "TRON_WALLET_ADDRESS",
  "balance": 123.45,
  "bandwidth": 1234,
  "energy": 5678
}
```

---

### `GET /v1/tron/get_records`

Получение последних записей из БД с пагинацией.

#### 🔸 Query-параметры:

- `page` — страница (по умолчанию: 1)
- `per_page` — количество записей на странице (по умолчанию: 10)

---

## 🧪 Тесты

- ✅ Интеграционный — проверка POST эндпоинта
- ✅ Юнит-тест — проверка записи данных в базу

#### Запуск тестов:

```bash
pytest tests/ -v
```

---

## 🗂️ Структура проекта

```
src/
├── config/         # Настройки и инициализация
├── core/           # Клиенты, утилиты, сериализаторы
├── tron/           # Бизнес-логика, API, модели
tests/              # Тесты
alembic/            # Миграции
```

---

## 📌 Особенности

- Используются type-hints и dependency injection
- Чистая архитектура: API / Сервис / Репозиторий
- Поддержка миграций через Alembic
- Обёрнуто в Docker-контейнеры
- Оформление кода по best practices

---

## 🧩 Возможности для расширения

- Добавление кэширования запросов
- Поддержка других сетей (например, Ethereum)
