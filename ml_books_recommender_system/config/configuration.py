import os
import sys
from ml_books_recommender_system.logger.log import logging
from ml_books_recommender_system.utils.util import read_yaml_file
from ml_books_recommender_system.exception.exception_handler import AppException
from ml_books_recommender_system.entity.config_entity import (DataIngestionConfig)

from ml_books_recommender_system.constant import *


class AppConfiguration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):
        """Read the yaml file and store the configuration information in the configs_info attribute."""
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """ Retrieve from yaml file
            Build the path for the ingested data and raw data directories
            Instance the class DataIngestionConfig with the retrieved information and return it."""
        try:
            data_ingestion_config = self.configs_info['data_ingestion_config']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['raw_data_dir'])

            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e
        