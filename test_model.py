
import joblib

model = joblib.load("production_model.joblib")

print("Testing the saved model")

speed = float(input("Conveyor Speed: "))
temperature = float(input("Motor Temperature: "))
current = float(input("Motor Current: "))

prediction = model.predict([[speed, temperature, current]])

print("Machine Status:", prediction[0])
