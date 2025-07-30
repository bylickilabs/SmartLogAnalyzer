import pandas as pd
import json
import os

def parse_log(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".csv":
        return pd.read_csv(filepath)
    elif ext == ".json":
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    elif ext in [".log", ".txt"]:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        df = pd.DataFrame({"line": lines})
        return df
    else:
        raise ValueError("Unbekanntes Dateiformat: %s" % ext)