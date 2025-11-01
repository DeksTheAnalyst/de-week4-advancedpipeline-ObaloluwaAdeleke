import configparser

class ConfigManager:
    def __init__(self, config_path='omnicart_pipeline/pipeline.cfg'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    @property
    def base_url(self):
        return self.config['API']['base_url']

    @property
    def limit(self):
        return int(self.config['API']['limit'])
