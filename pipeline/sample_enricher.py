from omnicart_pipeline.pipeline.data_enricher import DataEnricher

# Mock data to test
products = [
    {"id": 1, "title": "T-Shirt", "price": 15.99, "userId": 10, "rating": {"count": 3}},
    {"id": 2, "title": "Headphones", "price": 45.50, "userId": 11, "rating": {"count": 2}},
    {"id": 3, "title": "Shoes", "price": 60.00, "userId": 99, "rating": {"count": 1}},  # user missing
]

users = [
    {"id": 10, "username": "samuel", "email": "sam@example.com"},
    {"id": 11, "username": "ada", "email": "ada@example.com"},
]

enricher = DataEnricher(products, users)
enriched_data = enricher.enrich_data()
print(enriched_data)
