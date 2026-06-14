CREATE DATABASE heart_disease_db;
USE heart_disease_db;
CREATE TABLE predictions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    age FLOAT,
    sex FLOAT,
    cp FLOAT,
    trestbps FLOAT,
    chol FLOAT,
    fbs FLOAT,
    restecg FLOAT,
    thalach FLOAT,
    exang FLOAT,
    oldpeak FLOAT,
    slope FLOAT,
    caa FLOAT,
    thal FLOAT,
    prediction_result VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from predictions;
