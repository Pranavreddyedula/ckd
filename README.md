# 🩺 Chronic Kidney Disease Detection Using Machine Learning

A complete **machine learning–based web application** to detect **Chronic Kidney Disease (CKD)** using clinical parameters. The system predicts whether a patient is affected by CKD or not and visually explains the model performance using accuracy graphs and a confusion matrix.

---

## 🔗 Live Application

👉 **Deployed Web App (Render):**  
[https://ckd-ezaz.onrender.com/](https://ckd-ezaz.onrender.com/)

👉 **GitHub Repository:**  
[https://github.com/Pranavreddyedula/ckd](https://github.com/Pranavreddyedula/ckd)

---

## 🎓 Project Information

**Project Title:** Chronic Kidney Disease Detection and Prediction Using Machine Learning Techniques  
**Department:** Computer Science and Engineering (CSE – A)  
**College:** Tirumala Engineering College, Andhra Pradesh

### 👩‍🎓👨‍🎓 Batch – I (Team Members)

* 22NE1A0559 – Gunda Harika  \
* 22NE1A0562 – Guntupalli Sravani  \
* 22NE1A0546 – Galla Satish  \
* 23NE5A0502 – Edula Sai Pranav Reddy

### 👨‍🏫 Project Guide

**Dr. K. Satish sir**  
Associate Professor, Department of CSE

---

## 📌 Problem Statement

Chronic Kidney Disease is a serious medical condition that often goes undetected in its early stages. Traditional diagnosis methods require extensive laboratory testing and expert medical evaluation. This project aims to provide a **fast, cost-effective, and accurate CKD prediction system** using machine learning techniques and a web-based interface.

---

## ⚙️ System Features

* ✔ Predicts **CKD / No CKD** using clinical parameters
* ✔ Retains user input values after prediction
* ✔ Auto-fill **CKD Sample** and **Normal Sample** data
* ✔ Reset functionality
* ✔ Visual output using **kidney images**
* ✔ Displays **Model Accuracy Graph**
* ✔ Displays **Confusion Matrix**
* ✔ Deployed as a **Flask web application**

---

## 🧪 Input Parameters

The system uses the following medical attributes:

* Age (years)
* Blood Pressure (mm/Hg)
* Specific Gravity
* Albumin
* Sugar
* Red Blood Cells
* Pus Cell
* Pus Cell Clumps
* Bacteria
* Blood Glucose Random (mg/dl)
* Blood Urea (mg/dl)
* Serum Creatinine (mg/dl)
* Sodium (mEq/L)
* Potassium (mEq/L)
* Hemoglobin (gms)
* Packed Cell Volume
* White Blood Cell Count
* Red Blood Cell Count
* Hypertension
* Diabetes Mellitus
* Coronary Artery Disease
* Appetite
* Pedal Edema
* Anemia

*(Binary values: 0 = No / Abnormal, 1 = Yes / Normal)*

---

## 📊 Model Performance

### ✔ Accuracy

The trained model achieves **high training and testing accuracy**, indicating good generalization performance.

### ✔ Confusion Matrix

* True Positives (CKD correctly predicted)
* True Negatives (Healthy correctly predicted)
* Very low false positives and false negatives

These metrics confirm the reliability of the proposed system.

---

## 🖼️ Application Output

* **CKD Detected:** Displays diseased kidney image
* **No CKD:** Displays healthy kidney image
* Model Accuracy graph
* Confusion Matrix visualization

---

## 🧠 Technology Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Web Framework:** Flask
* **Frontend:** HTML, CSS
* **Deployment:** Render Cloud Platform

---

## 📁 Project Structure

```text
ckd/
│
├── static/
│   ├── accuracy.png
│   ├── confusion_matrix.png
│   ├── ckd_kidney.png
│   ├── healthy_kidney.png
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── ckd_model.pkl
├── scaler.pkl
├── imputer.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/Pranavreddyedula/ckd.git
cd ckd
pip install -r requirements.txt
python app.py
```

Then open: `http://127.0.0.1:5000/`

---

## 🎯 Expected Output

* User enters patient details
* Clicks **Predict**
* System displays:

  * CKD / No CKD result
  * Kidney image
  * Accuracy graph
  * Confusion matrix

---

## 🧾 Conclusion

This project demonstrates the effective use of machine learning techniques for early detection of Chronic Kidney Disease. The system provides accurate predictions, clear visual explanations, and a user-friendly web interface. It can assist healthcare professionals and students in understanding CKD diagnosis using data-driven approaches.

---

## 🔮 Future Enhancements

* Integration with real hospital datasets
* CKD stage-wise prediction
* Mobile application support
* Deep learning–based prediction models






