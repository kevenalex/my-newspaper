from pathlib import Path
import yaml

with Path("sources.yaml").open(encoding="utf-8") as f:
    config = yaml.safe_load(f)

for fonte in config["fontes"]:
    print(fonte["nome"], fonte["url"])