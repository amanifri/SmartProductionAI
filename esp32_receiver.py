

import csv
from pathlib import Path
import paho.mqtt.client as mqtt
import joblib

model = joblib.load("production_model.joblib")

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "smartproductionai/477713172791977985/telemetry"

CSV_FILE = Path("esp32_data_sessions.csv")

HEADERS = [
    "Session ID",
    "Reading",
    "Conveyor Speed",
    "Motor Temperature",
    "Motor Current",
]


def on_connect(client, userdata, flags, reason_code, properties):
    print("MQTT connection result:", reason_code)

    if reason_code == 0:
        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8").strip()
    print("Received:", payload)

    try:
        values = payload.split(",")

        if len(values) != 5:
            print("Skipping invalid message: expected 5 values")
            return

        session_id = values[0]
        reading = int(values[1])
        speed = float(values[2])
        temperature = float(values[3])
        current = float(values[4])

        # Ignore duplicates only within the same session
        if CSV_FILE.exists() and CSV_FILE.stat().st_size > 0:
            with CSV_FILE.open(
                "r", newline="", encoding="utf-8"
            ) as file:
                for row in csv.DictReader(file):
                    if (
                        row.get("Session ID") == session_id
                        and row.get("Reading") == str(reading)
                    ):
                        print("Duplicate ignored:", session_id, reading)
                        return

        file_is_new = (
            not CSV_FILE.exists()
            or CSV_FILE.stat().st_size == 0
        )

        with CSV_FILE.open(
            "a", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)

            if file_is_new:
                writer.writerow(HEADERS)

            writer.writerow([
                session_id,
                reading,
                speed,
                temperature,
                current,
            ])

        print("Saved to CSV")

    except ValueError:
        print("Skipping invalid numeric data")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")
client.connect(BROKER, PORT, 60)
client.loop_forever()
