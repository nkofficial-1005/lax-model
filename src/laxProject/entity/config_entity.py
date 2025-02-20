from dataclasses import dataclass
from pathlib import Path

#Working with this to configure the entity
@dataclass(frozen=True)
class DataIngestionConfig: #return type of the function defined in the config.yml file
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict