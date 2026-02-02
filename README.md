# eBay Async Client API

Asynchronous Python client for fetching eBay item information, with **FastAPI endpoints** and **typed Pydantic models**.

Supports **numeric item IDs** and **eBay item URLs**. All responses are validated and serialized using Pydantic.

---

## Features

* Async eBay client using **`aiohttp`**
* Automatic **OAuth token management**
* Mapper from eBay API responses to **typed Pydantic models**
* FastAPI endpoint with **`response_model`** for automatic validation and OpenAPI docs
* Accepts **numeric IDs or full eBay URLs** as input
* Currency conversion from USD → RUB using **CBR API**

---

## Installation

```bash
git clone <repo_url>
cd <repo_folder>
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file with your eBay and Redis credentials:

```env
EBAY_CLIENT=<your_client_id>
EBAY_SECRET=<your_client_secret>
EBAY_API_BASE_URL=https://api.ebay.com

REDIS_HOST=<your_redis_host>
REDIS_PASSWORD=<your_redis_password>
REDIS_PORT=<your_redis_port>
```

---

## Usage

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

### Endpoint

**GET /api/v1/items?item_url_or_id={id_or_url}**

Examples:

```bash
curl "http://127.0.0.1:8000/api/v1/items?item_url_or_id=397549021006"
curl "http://127.0.0.1:8000/api/v1/items?item_url_or_id=https://www.ebay.com/itm/397549021006"
```

Responses are validated against the `EbayItemResponse` Pydantic model.

---

## Project Structure

```
src/
├─ api/
│  ├─ v1/
│  │  ├─ routers/
│  │  │  └─ ebay.py        # FastAPI router
│  │  └─ dependencies.py   # Dependency injection for EbayClient
├─ services/
│  ├─ ebay/
│  │  ├─ client.py         # Async eBay client
│  │  ├─ auth.py           # OAuth token handling
│  │  └─ exchange_rate.py  # Currency conversion
├─ exceptions.py           # Custom exceptions
├─ schemas.py              # Pydantic models
├─ main.py                 # FastAPI app entrypoint
├─ settings.py             # Configuration
├─ utils.py                # Item ID validator
├─ mappers.py              # Items mapping
```

---

## Notes

* Prefer **query parameters** for item IDs/URLs; path parameters require URL encoding.
* Currency conversion uses the **Central Bank of Russia** JSON API.

---

## License

MIT License

