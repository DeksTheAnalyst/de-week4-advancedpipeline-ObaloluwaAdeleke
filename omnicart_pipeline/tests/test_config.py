import pytest
from omnicart_pipeline.pipeline.config import ConfigManager

def test_config_manager_reads_values(tmp_path):
    """
    Test that ConfigManager correctly reads base_url and limit
    from a temporary pipeline.cfg file.
    """
    # Create a temporary pipeline.cfg file
    config_file = tmp_path / "pipeline.cfg"
    config_file.write_text("""
    [API]
    base_url = https://fakeapi.test
    limit = 10
    """)

    # Initialize ConfigManager with the temp config path
    config = ConfigManager(config_path=str(config_file))

    # Assertions: check that properties return expected values
    assert config.base_url == "https://fakeapi.test"
    assert config.limit == 10

def test_config_manager_missing_section(tmp_path):
    # Create a config file **without the [API] section**
    config_file = tmp_path / "pipeline.cfg"
    config_file.write_text("""
    [NOT_API]
    base_url = https://fakeapi.test
    limit = 10
    """)

    # ConfigManager should raise KeyError when trying to access the missing section
    config = ConfigManager(config_path=str(config_file))
    with pytest.raises(KeyError) as exc_info:
        _ = config.base_url  # Attempt to access missing section

    # Optional: assert the error message contains 'API'
    assert 'API' in str(exc_info.value)