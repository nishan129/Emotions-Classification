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
    
    