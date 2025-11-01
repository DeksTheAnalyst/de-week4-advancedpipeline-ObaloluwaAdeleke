# de-week4-advancedpipeline-<yourname>

Overview
OmniCart data enrichment pipeline: fetch products & users from FakeStore API, enrich product data with seller info, compute seller-level metrics (total revenue, products sold, average price), and output `seller_performance_report.json`.

Pagination strategy
The API client fetches `/products` in pages using `limit` and `skip` query parameters:
- Start with `skip = 0`.
- Request `/products?limit={limit}&skip={skip}`.
- Append returned list to local buffer.
- If response returns an empty list, stop.
- Otherwise, increase `skip += limit` and repeat.

This approach:
- Prevents memory spikes for very large APIs.
- Works with APIs that return fixed-size pages.

Data enrichment logic
- Convert `products` and `users` JSON lists into `pandas.DataFrame`.
- Perform a **left join** on `products.userId == users.id` to enrich products with seller fields (`username`, `email`).
  - Left join preserves all products even if seller info is missing.
- Calculate a `revenue` column as `price * rating.count` (assumes `rating.count` is quantity sold).
- Fill missing seller fields with `"Unknown"`.

Running the pipeline
1. Activate venv: `source .venv/Scripts/activate` (Windows Git Bash)  
2. Install deps: `pip install -r requirements.txt`  
3. Run: `python -m omnicart_pipeline.main`  
4. Output: `seller_performance_report.json`

Tests
Run `pytest -v` in the project root.

Notes
- Config: `pipeline.cfg` contains `[API] base_url` and `limit`.
- Tests mock network calls — they do not hit the real API.
