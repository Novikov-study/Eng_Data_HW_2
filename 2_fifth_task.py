import pandas as pd
import os
import json
import msgpack

columns = [
    "Elevation", "Aspect", "Slope", "Horizontal_Distance", "Hillshade_Noon",
    "Horizontal_Fire", "Cover_Type"
]

data = pd.read_csv("./data/covtype.data.gz", header=None, names=columns)

selected_columns = [
    "Elevation", "Aspect", "Slope", "Horizontal_Distance", "Hillshade_Noon",
    "Horizontal_Fire", "Cover_Type"
]
data = data[selected_columns]

stats = {}

numerical_fields = ["Elevation", "Aspect", "Slope", "Horizontal_Distance", "Hillshade_Noon", "Horizontal_Fire"]
for column in numerical_fields:
    stats[column] = {
        "max": int(data[column].max()),
        "min": int(data[column].min()),
        "mean": float(data[column].mean()),
        "sum": float(data[column].sum()),
        "std": float(data[column].std())
    }

categorical_field = "Cover_Type"
stats[categorical_field] = {int(k): int(v) for k, v in data[categorical_field].value_counts().to_dict().items()}

with open("fifth_task_stats.json", "w") as f:
    json.dump(stats, f, indent=4)

data.to_csv("fifth_task_result.csv", index=False)
data.to_json("fifth_task_result.json", orient="records")
data.to_pickle("fifth_task_result.pkl")

with open("fifth_task_result.msgpack", "wb") as f:
    msgpack.dump(data.to_dict(orient="records"), f)

file_sizes = {}
for fmt in ["csv", "json", "pkl", "msgpack"]:
    file_path = f"fifth_task_result.{fmt}"
    file_sizes[fmt] = os.path.getsize(file_path)

print("Размеры файлов:", file_sizes)
