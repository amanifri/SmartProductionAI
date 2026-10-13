
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_score

features = []
labels = []

with open("production_data.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        features.append([
            float(row["Conveyor Speed"]),
            float(row["Motor Temperature"]),
            float(row["Motor Current"])
        ])
        labels.append(row["Status"])

model = DecisionTreeClassifier(max_depth=3, random_state=42)

cv = LeaveOneOut()
scores = cross_val_score(model, features, labels, cv=cv)

print("Number of readings:", len(features))
print("Cross-validation accuracy:", round(scores.mean() * 100, 2), "%")


model.fit(features, labels)

print("\nModel trained successfully!")

print("\nTesting a normal-like reading:")
print(model.predict([[1.50, 44.0, 1.90]])[0])

print("\nTesting a warning-like reading:")
print(model.predict([[1.40, 52.0, 2.75]])[0])

import joblib

joblib.dump(model, "production_model.joblib")

print("\nModel saved as production_model.joblib")