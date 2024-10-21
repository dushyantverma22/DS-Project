from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL:Path
    local_data_file:Path                                   ## Name should always same
    unzip_dir:Path
    ## Data class we don't need to use self variable

@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

