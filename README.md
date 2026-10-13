

# SmartProductionAI

**Industrial Monitoring and Machine Learning Prototype**

## Overview

SmartProductionAI is a student project exploring how machine learning can be applied to industrial monitoring. The prototype processes conveyor speed, motor temperature, and motor current readings to classify machine operating conditions as `Normal` or `Warning`.

## Features

- Receives telemetry messages using MQTT.
- Stores sensor readings in CSV files.
- Trains a Decision Tree classifier using Scikit-learn.
- Saves and reloads the trained model.
- Predicts machine status from recorded sensor readings.

## Technologies

- Python
- Scikit-learn
- MQTT
- ESP32 telemetry
- CSV data processing
- GitHub

## Project Workflow

1. Receive telemetry through MQTT.
2. Store readings in a CSV file.
3. Train a machine-learning model using sample data.
4. Load the saved model and predict machine status.

## Current Status

The project is under development. The current training dataset is small and experimental, and the initial predictions are preliminary. The model has not yet been validated for real industrial use.

## Planned Improvements

- Integrate automatic predictions into the MQTT receiver.
- Develop an industrial monitoring dashboard using Ignition SCADA.
- Evaluate the model with more representative data.
- Improve fault detection and validation.

## Author

**Amani Frigui**  
Electrical Engineering and Industrial Computing student

GitHub: [@amanifri](https://github.com/amanifri)
