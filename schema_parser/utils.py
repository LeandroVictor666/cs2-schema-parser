import os
import glob
from pathlib import Path


def clean_output_dir(path: str = "output"):
    os.makedirs(path, exist_ok=True)
    for file_path in glob.glob(os.path.join(path, "*")):
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f" [/] Cleaned output directory: {path}")
