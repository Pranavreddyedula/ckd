from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# ---------------- LOAD MODELS (RENDER SAFE) ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "ckd_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
imputer = joblib.load(os.path.join(BASE_DIR, "imputer.pkl"))
# -----------------------------------------------------------

FEATURES = [
    'age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc',
    'sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane'
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image = None
    form_data = {}

    # ---------------- SAMPLE DATA ----------------
    sample_ckd = {
        'age':55,'bp':150,'sg':1.010,'al':4,'su':3,'rbc':0,'pc':0,'pcc':1,'ba':1,
        'bgr':180,'bu':80,'sc':4.5,'sod':120,'pot':6.1,'hemo':8.5,'pcv':28,
        'wc':7200,'rc':3.2,'htn':1,'dm':1,'cad':0,'appet':0,'pe':1,'ane':1
    }

    sample_normal = {
        'age':30,'bp':120,'sg':1.025,'al':0,'su':0,'rbc':1,'pc':1,'pcc':0,'ba':0,
        'bgr':95,'bu':20,'sc':0.9,'sod':140,'pot':4.2,'hemo':15.2,'pcv':45,
        'wc':8000,'rc':5.1,'htn':0,'dm':0,'cad':0,'appet':1,'pe':0,'ane':0
    }
    # ---------------------------------------------------------

    if request.method == "POST":

        # ---------- AUTO-FILL BUTTONS ----------
        if "fill_ckd" in request.form:
            form_data = sample_ckd

        elif "fill_normal" in request.form:
            form_data = sample_normal

        elif "reset" in request.form:
            form_data = {}

        # ---------- PREDICTION ----------
        else:
            values = []
            for f in FEATURES:
                v = request.form.get(f)
                if v == "" or v is None:
                    v = 0
                form_data[f] = v
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
        cm_img="confusion_matrix.png",
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)
