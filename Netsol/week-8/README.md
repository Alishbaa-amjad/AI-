# 📘 Week 8 — AI/ML Mini Application (NETSOL)

## 📌 Overview

This repository contains my **Week 8 tasks** from the **AI/ML course at NETSOL**.
This week focused on building a **real-world Machine Learning Mini Application**, along with completing practical assignments on **KNN and Decision Trees**. 🤖📊

The highlight of this week is an **end-to-end ML project**, where I implemented a system that predicts whether a student will **Pass or Fail** based on study patterns and previous performance. 🎯

---

## 🎯 Objectives

* 🧠 Apply ML concepts in a real-world scenario
* ⚙️ Build and train a classification model
* 💾 Save and reuse trained models
* 🌐 Develop an interactive UI using Streamlit
* 🔄 Understand complete ML workflow (training → prediction → deployment)

---

## 💡 Mini App — Project Idea

This ML-based application predicts:

👉 **Will a student pass or fail?** 🎓

### 📥 Input Features:

* ⏱️ Study Hours
* 📊 Previous Results

### 📤 Output:

* ✅ Pass
* ❌ Fail

The model learns from data patterns and provides predictions based on user input. 🤖

---

## 📂 Repository Structure

```bash id="wk8final"
week-8/
│── Mini-App/
│   │── app.py
│   │── main.py
│   │── main1.py
│   │── train_model.py
│   │── model.pkl
│   │── streamlit_app.py
│   │── std_success_predictor_vdo.mp4
│   │── __pycache__/
│
│── 01_KNN_Spotify_Lab.ipynb
│── 02_decision_tree_worksheet.ipynb
│── README.md
```

---

## ⚙️ How the Mini App Works

### 🔹 1. Model Training

* 📊 Dataset used to train a classification model
* ⚙️ Implemented in `train_model.py`
* 💾 Model saved as `model.pkl`

---

### 🔹 2. Prediction Logic

* 🧠 Core logic implemented in:

  * `main.py`
  * `main1.py`
  * `app.py`

---

### 🔹 3. User Interface (Frontend)

* 🌐 Built using **Streamlit**
* 📥 User provides inputs (study hours, previous result)
* 📤 App predicts outcome (Pass/Fail)

---

### 🔹 4. Demo

* 🎥 `std_success_predictor_vdo.mp4` demonstrates the working application

---

## 📚 Assignments Covered

### 🔹 01 — KNN Spotify Lab 🎵

* 📂 Load the Spotify Dataset
* 📊 Visualise the Audio Features
* 🧹 Preprocessing
* 📏 Distance Functions
* 🧠 Build the KNNClassifier Class
* 🚀 First Real Run on Spotify Data
* 🔍 Finding the Best K
* ⚖️ Comparing Distance Metrics
* 🤖 Benchmark Against Sklearn
* 🌟 Bonus Challenges
* 📝 Final Reflection

---

### 🔹 02 — Decision Tree Worksheet 🌳

* 📥 Import Libraries
* 📉 Decision Tree Regression
* 📊 Dataset: Diabetes (442 patients)
* 📝 Reflection 1
* 🌸 Decision Tree Classification
* 📊 Dataset: Iris Flowers (150 samples)
* 📝 Reflection 2
* 🌟 BONUS Challenges

---

## 🤖 Machine Learning Concepts Used

* 📊 Classification Algorithms
* 🧠 K-Nearest Neighbors (KNN)
* 🌳 Decision Trees
* 💾 Model Saving (`.pkl`)
* 🔍 Prediction Systems
* 🔄 End-to-End ML Pipeline

---

## 🛠️ Technologies Used

* 🐍 Python
* 🤖 Scikit-learn
* 📊 Pandas
* 🔢 NumPy
* 🌐 Streamlit

---

## 🚀 How to Run the App

1. 📥 Clone the repository
2. 📦 Install dependencies:

```bash
pip install -r requirements.txt
```

3. ▶️ Run the app:

```bash
streamlit run streamlit_app.py
```

---

## 🎯 Key Learnings

* 🧠 Building real-world ML applications
* ⚙️ Training and saving models
* 🔍 Making predictions from user input
* 🌐 Creating interactive ML apps
* 📊 Applying ML algorithms (KNN, Decision Tree)

---

## 🚀 Practical Impact

By completing this week, I can now:

* ✔️ Build and deploy ML-based applications
* ✔️ Connect backend ML logic with UI
* ✔️ Work with real prediction systems
* ✔️ Apply multiple ML algorithms in practice

---

## 🧾 Conclusion

Week 8 was a **major practical milestone** in my AI/ML journey. 🚀
I moved from theory to implementation by building a **complete ML application** and applying multiple algorithms like **KNN and Decision Trees**.

This week significantly improved my understanding of how machine learning models are **trained, deployed, and used in real-world applications**. 🤖📈

---

## 👩‍💻 Author

**Alishba Amjad**

🎓 BS Computer Science Graduate
📍 AIML Trainee at NETSOL

I am passionate about building intelligent systems and continuously improving my skills through **hands-on AI/ML projects**. 💡

---

## ⭐ Note

This project can be further enhanced by:

* 📊 Using larger datasets
* 🤖 Trying advanced ML models
* 🎨 Improving UI/UX of the application

---

✨ **Stay tuned for Week 9! 🚀**
