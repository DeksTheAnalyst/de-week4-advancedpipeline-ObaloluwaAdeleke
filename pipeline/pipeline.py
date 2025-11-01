import json
from omnicart_pipeline.pipeline.config import ConfigManager
from omnicart_pipeline.pipeline.api_client import APIClient
from omnicart_pipeline.pipeline.data_enricher import DataEnricher
from omnicart_pipeline.pipeline.data_analyzer import DataAnalyzer


class Pipeline:
    def run(self):
        config = ConfigManager()
        client = APIClient(config.base_url, config.limit)

        print("Fetching products...")
        products = client.get_all_products()

        print("Fetching users...")
        users = client.get_all_users()

        print("Enriching data...")
        enricher = DataEnricher()
        enriched = enricher.enrich(products, users)

        print("Analyzing data...")
        analyzer = DataAnalyzer()
        results = analyzer.analyze(enriched)

        print("Saving report...")
        with open('seller_performance_report.json', 'w') as f:
            json.dump(results, f, indent=4)

        print("Pipeline completed successfully.")
