# student_score_predictor
# 🎓 Student Score Predictor

A Machine Learning project that predicts student scores based on study-related input data using regression algorithms. This project provides an interactive Streamlit web application for real-time score prediction.

---

## 🚀 Features

* Student score prediction using Machine Learning
* Regression model training and evaluation
* Interactive Streamlit web application
* CSV dataset processing
* Saved trained models using Pickle
* Dynamic prediction support

---

## 🛠️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Scikit-learn | Machine Learning     |
| Pandas       | Data Processing      |
| NumPy        | Numerical Operations |
| Streamlit    | Web Application      |
| Pickle       | Model Serialization  |

---

## 📂 Project Structure

```bash
student_score_predictor/
│
├── ml project/
│   ├── data/
│   │   ├── data.csv
│   │   ├── test_data.csv
│   │   └── test_predictions.csv
│   │
│   ├── models/
│   │   ├── trained_model.pkl
│   │   └── student_overall_regression_model.pkl
│   │
│   ├── src/
│   │   ├── train_model.py
│   │   ├── test_model.py
│   │   └── predict_dynamic.py
│   │
│   ├── streamlit_app.py
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/student_score_predictor.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd student_score_predictor
```

### 3️⃣ Install Dependencies

```bash
pip install -r "ml project/requirements.txt"
```

---

## ▶️ Run the Application

```bash
streamlit run "ml project/streamlit_app.py"
```

After running the command, open the local URL provided by Streamlit in your browser.

Example:

```bash
http://localhost:8501
```

---

## 🧠 Train the Model

```bash
python "ml project/src/train_model.py"
```

---

## 📊 Test the Model

```bash
python "ml project/src/test_model.py"
```

---

## 🔮 Prediction

```bash
python "ml project/src/predict_dynamic.py"
```

---

## 📁 Dataset

Dataset used for training and testing is available in:

```bash
ml project/data/data.csv
```

---

## 🌟 Future Improvements

* Improve model accuracy
* Add graphical visualizations
* Deploy application online
* Add user authentication
* Support multiple ML algorithms

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Create a Pull Request

---

## 📜 License

This project is developed for educational purposes.

---

