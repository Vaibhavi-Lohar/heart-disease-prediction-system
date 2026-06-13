# Heart Disease Prediction System

## Overview

The Heart Disease Prediction System is a Machine Learning based web application that predicts whether a patient is at risk of heart disease using various medical parameters. The system provides quick predictions through a simple web interface and stores prediction records in a MySQL database.

## Problem Statement

Heart disease is one of the leading causes of death worldwide. Early prediction can help patients take preventive measures and seek medical attention at the right time.

## Objectives

- Predict heart disease using machine learning.
- Provide a simple web-based interface.
- Store prediction records in a database.
- Integrate machine learning with web development.

## Features

- Heart disease prediction
- User-friendly interface
- Database integration
- Prediction result display
- Prediction history storage

## Technologies Used

### Frontend
- HTML
- CSS

### Backend
- Flask (Python)

### Machine Learning
- Scikit-learn
- Joblib

### Database
- MySQL

## Project Workflow

1. User enters patient details.
2. Flask receives the input data.
3. The trained machine learning model processes the data.
4. The system predicts whether heart disease is detected.
5. The prediction result is displayed to the user.
6. The result is stored in the MySQL database.

## Input Parameters

The model uses the following parameters:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Rest ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- Slope
- CA
- Thal

## Output

The system generates one of the following results:

- Heart Disease Detected
- No Heart Disease Detected

## Applications

- Healthcare assistance systems
- Medical research
- Educational projects
- Preliminary health assessment

## Future Enhancements

- User authentication
- Prediction history dashboard
- Health report generation
- Risk percentage calculation
- Doctor recommendation system

## Conclusion

The Heart Disease Prediction System demonstrates the integration of Machine Learning, Flask, and MySQL to provide an effective solution for heart disease prediction. The project offers a simple and efficient platform for analyzing patient health data and generating predictions.
