from flask import Flask, render_template, request
import joblib
import mysql.connector

app = Flask(__name__)

# Load model
model = joblib.load("../saved_model/heart_model.pkl")

# MySQL Connection
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    sex = float(request.form["sex"])
    cp = float(request.form["cp"])
    trestbps = float(request.form["trestbps"])
    chol = float(request.form["chol"])
    fbs = float(request.form["fbs"])
    restecg = float(request.form["restecg"])
    thalach = float(request.form["thalach"])
    exang = float(request.form["exang"])
    oldpeak = float(request.form["oldpeak"])
    slope = float(request.form["slope"])
    caa = float(request.form["ca"])
    thal = float(request.form["thal"])

    features = [[
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        caa, thal
    ]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    # Save into database
    query = """
    INSERT INTO predictions (
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        caa, thal, prediction_result
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        caa, thal, result
    )

    cursor.execute(query, values)
    db.commit()

    return render_template("result.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)