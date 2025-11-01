from omnicart_pipeline.pipeline.data_analyzer import DataAnalyzer
from omnicart_pipeline.pipeline.data_enricher import DataEnricher

# You can reuse the same fake data from before:
products = [
    {"id": 1, "title": "T-Shirt", "price": 15.99, "userId": 10, "rating": {"count": 3}},
    {"id": 2, "title": "Headphones", "price": 45.50, "userId": 11, "rating": {"count": 2}},
    {"id": 3, "title": "Shoes", "price": 60.00, "userId": 99, "rating": {"count": 1}},
]

users = [
    {"id": 10, "username": "samuel", "email": "sam@example.com"},
    {"id": 11, "username": "ada", "email": "ada@example.com"},
]

# Step 1: Enrich the data
enricher = DataEnricher(products, users)
enriched_df = enricher.enrich()

# Step 2: Analyze the data
analyzer = DataAnalyzer(enriched_df)
results = analyzer.analyze()

print(results)
