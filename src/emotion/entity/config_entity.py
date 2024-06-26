from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    data_path: Path
    STATUS_FILE: Path
    all_schema : dict
    
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    transform_data_path: Path
   

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    tokenizer_path: Path
    model: Path
    model_path: Path 
    
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path : Path
    model_path: Path
    tokenizer_path : Path
    mode_evaluation_path : Path
    matrix_path : Path
    
@dataclass(frozen=True)
class PredictionConfig:
    model_path: Path
    tokenizer_path : Path