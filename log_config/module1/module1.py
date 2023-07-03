import logging

from log_config.module1 import submodule1

LOGGER = logging.getLogger(__name__)

def magical_action_module1():
    module_name="Module1"
    LOGGER.debug(f"{module_name} debug")
    LOGGER.info(f"{module_name} info")
    LOGGER.warning(f"{module_name} warn")
    LOGGER.exception(f"{module_name} exception")
    LOGGER.critical(f"{module_name} critical")
    submodule1.magical_action_module1()