
import csv
import joblib

model = joblib.load("production_model.joblib")

with open(
    "esp32_data_sessions.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        speed = float(row["Conveyor Speed"])
        temperature = float(row["Motor Temperature"])
        current = float(row["Motor Current"])

        prediction = model.predict([
            [speed, temperature, current]
        ])[0]

        print(
            "Reading:", row["Reading"],
            "| Temperature:", temperature,
            "| Current:", current,
            "| Predicted Status:", prediction
        )
