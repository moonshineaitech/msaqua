import yaml
import json


def load_config(config_file):
    """
    Loads configuration from a YAML or JSON file.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        dict: The loaded configuration data.

    Raises:
        ValueError: If the file format is not supported or the file is missing.
    """
    with open(config_file, 'r') as f:
        if config_file.endswith('.yaml') or config_file.endswith('.yml'):
            return yaml.safe_load(f)
        elif config_file.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError(f"Unsupported configuration file format: {config_file}")


def get_value(section, key, default=None):
    """
    Retrieves a configuration value from the loaded data structure.

    Args:
        section (str): The section name in the configuration file.
        key (str): The key for the desired value.
        default (optional): A default value to return if the key is not found.

    Returns:
        The value associated with the key in the specified section,
        or the default value if not found.

    Raises:
        ValueError: If the section or key is missing and no default is provided.
    """
    config = load_config(config_file)
    try:
        return config[section][key]
    except (KeyError, TypeError):
        if default is not None:
            return default
        else:
            raise ValueError(f"Missing configuration value: '{section}.{key}'")