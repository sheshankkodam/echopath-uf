# python modules
import os
import yaml
from os.path import abspath, join, dirname, realpath, isfile
from dotmap import DotMap


class ConfigFactory:
    def __init__(self):
        pass

    os_env = os.getenv("ESEENV", "PROD").lower()

    @staticmethod
    def create_log_config():
        """
        Opens logging configurations for the SOUP
        :return: dict of logging configuration
        """
        conf_base = ConfigFactory._get_conf_location()
        log_conf_file = abspath(join(conf_base, 'log_conf.yaml'))
        log_data = yaml.load(open(log_conf_file))[ConfigFactory.os_env]
        return log_data

    @staticmethod
    def create_app_config():
        """
        Opens configuration files for SOUP
        :return: DotMap of the SOUP configs
        """
        conf_base = ConfigFactory._get_conf_location()
        app_conf_file = abspath(join(conf_base, 'app_conf.yaml'))

        with open(app_conf_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)[ConfigFactory.os_env]
        conf_dotmap = DotMap(cfg)
        return conf_dotmap

    @staticmethod
    def _get_conf_location():
        """
        Retrieves the base configuration location by environment
        :return: the base location for configuration files depending on the ESEENV environment variable
        """
        app_root = dirname(realpath(__file__))
        conf_location = abspath(join(app_root, 'conf'))
        return conf_location
