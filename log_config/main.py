import logging
import logging.config
import yaml
import requests
from log_config.module1.module1 import magical_action_module1
from log_config.module2 import magical_action_module2
from log_config.module3.module3 import magical_action_module3

LOGGER = logging.getLogger("log_config")

def config_loggin():
    # Load the config file
    with open('logging.yml', 'rt') as f:
        config = yaml.safe_load(f.read())

    # Configure the logging module with the config file
    logging.config.dictConfig(config)

def request_all_the_things():
    requests.get("http://google.com")

def log_all_the_things():
    module_name="root"
    LOGGER.debug(f"{module_name} debug")
    LOGGER.info(f"{module_name} info")
    LOGGER.warning(f"{module_name} warn")
    LOGGER.exception(f"{module_name} exception")
    LOGGER.critical(f"{module_name} critical")

def main():
    config_loggin()
    request_all_the_things()
    log_all_the_things()
    magical_action_module1()
    magical_action_module2()
    magical_action_module3()


if __name__ == "__main__":
    main()