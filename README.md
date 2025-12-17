🩺 Chronic Kidney Disease Detection Using Machine Learning
📌 Project Overview

Chronic Kidney Disease (CKD) is a serious medical condition that can lead to kidney failure if not detected early. This project uses Machine Learning techniques to predict whether a patient is suffering from CKD based on clinical parameters. The system provides accurate predictions, visual results, and model performance evaluation through graphs.

This project is developed as part of a B.Tech Computer Science Engineering final-year project.

🎯 Objectives

Early detection of Chronic Kidney Disease

Reduce manual diagnosis errors

Provide visual and interpretable results

Build a user-friendly web-based prediction system

🧠 Features

✅ CKD / No CKD prediction

🩺 Kidney image visualization based on result

📊 Accuracy graph display

📈 Confusion matrix for model evaluation

🌐 Web interface using Flask

📁 Easy deployment and GitHub-ready structure

🛠️ Tech Stack
Category	Technology
Programming Language	Python
Web Framework	Flask
ML Library	Scikit-learn
Data Processing	NumPy
Model Storage	Joblib
Frontend	HTML, CSS
Deployment Ready	Render
📂 Project Structure
ckd/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── ckd_model.pkl
├── scaler.pkl
├── imputer.pkl
│
├── static/
│   ├── style.css
│   ├── accuracy.png
│   ├── confusion_matrix.png
│   ├── ckd_kidney.png
│   └── healthy_kidney.png
│
├── templates/
│   └── index.html
│
└── Chronic-Kidney-Disease-Detection-Using-Machine-Learning-final.pptx

🧪 Input Parameters

The model uses the following clinical features:

age, bp, sg, al, su, rbc, pc, pcc, ba,
bgr, bu, sc, sod, pot, hemo, pcv, wc,
rc, htn, dm, cad, appet, pe, ane


Note: Binary values are encoded as
0 = No / Abnormal, 1 = Yes / Normal

⚙️ How It Works

User enters patient medical details

Input data is preprocessed using:

Missing value imputer

Feature scaler

Trained ML model predicts CKD status

Output is displayed with:

Result message

Kidney image

Accuracy graph

Confusion matrix

🚀 Run the Project Locally
Step 1: Clone Repository
git clone https://github.com/Pranavreddyedula/ckd.git
cd ckd

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run Flask App
python app.py

Step 4: Open Browser
http://127.0.0.1:5000/

📊 Model Performance

Training Accuracy: ~99%

Testing Accuracy: ~97%

Evaluation Metrics:

Accuracy

Confusion Matrix

True Positives & Negatives

🧩 Output Screens

CKD detected → Diseased kidney image

No CKD → Healthy kidney image

Accuracy bar graph

Confusion matrix heatmap

🎓 Academic Use

This project is suitable for:

B.Tech CSE Final Year Project

Mini Projects

Machine Learning Labs

IEEE-style Project Reports

Viva & Demonstrations

⚠️ Limitations

Model trained on limited dataset

Real-world diagnosis requires doctor confirmation

Performance may vary with unseen data

🔮 Future Enhancements

Deep Learning-based prediction

Real-time hospital data integration

Cloud database support

Mobile application

Multi-disease prediction system

👨‍🎓 Author

Edula Sai Pranav Reddy
B.Tech Computer Science Engineering
GitHub: https://github.com/Pranavreddyedula

📜 License

This project is developed for educational purposes only.
