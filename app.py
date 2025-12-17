from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# ---------------- PATH FIX FOR RENDER ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "ckd_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
imputer = joblib.load(os.path.join(BASE_DIR, "imputer.pkl"))
# ----------------------------------------------------

FEATURES = [
    'age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc',
    'sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane'
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image = None

    if request.method == "POST":
        values = []
        for f in FEATURES:
            v = request.form.get(f)
            if v == "" or v is None:
                v = 0
            values.append(float(v))

        X = np.array(values).reshape(1, -1)
        X = imputer.transform(X)
        X = scaler.transform(X)

        prediction = model.predict(X)[0]

        if prediction == 1:
            result = "Chronic Kidney Disease Detected"
            image = "ckd_kidney.png"
        else:
            result = "No Chronic Kidney Disease"
            image = "healthy_kidney.png"

    return render_template(
        "index.html",
        result=result,
        image=image,
        accuracy_img="accuracy.png",
        cm_img="confusion_matrix.png"
    )

if __name__ == "__main__":
    app.run(debug=True)
