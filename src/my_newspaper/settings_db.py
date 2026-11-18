from pathlib import Path
import yaml

from settings import Source

with Path("sources.yaml").open(encoding="utf-8") as f:
    sources = yaml.safe_load(f)

def getSources() -> list[Source]:
    return sources