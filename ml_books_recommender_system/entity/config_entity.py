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


# DataTransformationConfig = namedtuple("DataTransformationConfig", ["clean_data_file_path",
#                                                                    "transformed_data_dir"]) 


# ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["transformed_data_file_dir",
#                                                       "trained_model_dir",
#                                                       "trained_model_name"])


# ModelRecommendationConfig = namedtuple("ModelRecommendationConfig", ["book_name_serialized_objects",
#                                                       "book_pivot_serialized_objects",
#                                                       "final_rating_serialized_objects",
#                                                       "trained_model_path"])


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


@dataclass(frozen=True)
class DataTransformationConfig:
    clean_data_file_path: str
    transformed_data_dir: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    transformed_data_file_dir: str
    trained_model_dir: str
    trained_model_name: str

@dataclass(frozen=True)
class ModelRecommendationConfig:
    book_name_serialized_objects: str
    book_pivot_serialized_objects: str
    final_rating_serialized_objects: str
    trained_model_path: str