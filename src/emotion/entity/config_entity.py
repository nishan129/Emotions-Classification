from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    data_path: Path
    train_data_dir : Path
    test_data_dir : Path