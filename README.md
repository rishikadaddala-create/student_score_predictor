# student_score_predictor
🎓 Student Score Predictor

A Machine Learning project that predicts student scores based on study-related input data. This project uses Python, Scikit-learn, and Streamlit to train a regression model and provide an interactive web interface for predictions.

🚀 Features
📊 Student score prediction using Machine Learning
🧠 Regression model training and testing
📁 CSV dataset handling
🌐 Interactive Streamlit web application
💾 Saved trained model using Pickle
✅ Dynamic prediction support
🛠️ Tech Stack
Python
Scikit-learn
Pandas
NumPy
Streamlit
Pickle
📂 Project Structure
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
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/student_score_predictor.git
2️⃣ Navigate to the Project Folder
cd student_score_predictor
3️⃣ Install Dependencies
pip install -r "ml project/requirements.txt"
▶️ Run the Project
Run Streamlit Application
streamlit run "ml project/streamlit_app.py"

After running the command, Streamlit will provide a local URL such as:

http://localhost:8501

Open it in your browser.

🧪 Model Training

To train the model manually:

python "ml project/src/train_model.py"
📈 Model Testing

To test the model:

python "ml project/src/test_model.py"
🔮 Prediction

Dynamic prediction script:

python "ml project/src/predict_dynamic.py"
📊 Dataset

The dataset is stored in:

ml project/data/data.csv

It contains student-related data used for training and evaluating the regression model.

🌟 Future Improvements
Improve model accuracy
Add more visualization charts
Deploy the application online
Add authentication system
Support multiple ML algorithms
🤝 Contributing

Contributions are welcome.

Fork the repository
Create a feature branch
Commit your changes
Push to your branch
Create a Pull Request
📜 License

This project is for educational and learning purposes.
