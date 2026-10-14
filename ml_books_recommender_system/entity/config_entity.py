#from collections import namedtuple

#DataIngestionConfig = namedtuple("DatasetConfig", ["dataset_download_url",
#                                                   "raw_data_dir",
#                                                   "ingested_dir"])

#DataIngestionConfig = namedtuple("DataIngestionConfig", [
#    "dataset_download_url",
#    "raw_data_dir",
#    "ingested_dir",
#])

# DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
#                                                          "books_csv_file",
#                                                          "ratings_csv_file",
#                                                          "serialized_objects_dir"])   

# la clase de abajo es solo para guardar datos; créale automáticamente lo necesario.
# frozen=True significa congelada: una vez creada, sus valores no se pueden cambiar.
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    dataset_download_url: str
    raw_data_dir: str
    ingested_dir: str


@dataclass(frozen=True)
class DataValidationConfig:
    clean_data_dir: str
    books_csv_file: str
    ratings_csv_file: str
    serialized_objects_dir: str