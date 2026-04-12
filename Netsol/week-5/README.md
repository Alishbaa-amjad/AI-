# 📘 Week 5 — AI/ML Learning Journey (NETSOL)

## 📌 Overview

This repository contains my **Week 5 tasks** from the **AI/ML course at NETSOL**.
The focus of this week was on **Data Distributions** and **Classification Metrics**, along with practical implementation using Python on the **Titanic dataset**.

Key areas covered:

* 📊 Applying different distributions on dataset columns
* 🧮 Understanding and implementing classification metrics
* 🧠 Building intuition on which metric to use in different scenarios

---

## 📂 Repository Structure

```bash
week-5/
│── 00_Titanic-Dataset.csv
│── 01_Titanic_Dataset.ipynb
│── 02_classification_metrics.ipynb
│── 03_quiz1.pdf
│── README.md
```

---

## 📚 Tasks Breakdown

### 🔹 00 — Titanic Dataset

* 🌐 Dataset downloaded from the internet
* 📂 Prepared for analysis in notebooks

---

### 🔹 01 — Titanic Dataset Analysis

* 📊 Explored columns and data types
* 📈 Applied **Probability Distributions** on different columns:

  * 🎲 Bernoulli Distribution
  * 🎯 Binomial Distribution
  * 📉 Normal Distribution
  * 🧮 Poisson Distribution
  * 📊 Exponential Distribution
* 🧩 Distribution Fitting & KDE Plots
* 📏 Q-Q Plot for Age
* 🔄 Data Transformation:

  * Age before & after log transformation
  * Fare before & after log transformation

---

## 📊 Distributions Applied

| Distribution       | Column Used            | Reason                               |
| ------------------ | ---------------------- | ------------------------------------ |
| **Bernoulli**      | Survived, Sex (binary) | Binary outcomes (0/1)                |
| **Binomial**       | Survived               | Multiple Bernoulli trials            |
| **Poisson**        | SibSp, Parch           | Count data                           |
| **Exponential**    | Fare                   | Continuous & right-skewed            |
| **Normal**         | Age                    | Continuous & approximately symmetric |
| **t-Distribution** | Age (sample)           | Small sample analysis                |

---

### 🔹 02 — Classification Metrics

* 📊 **The Confusion Matrix** — Foundation of all classification metrics
* ✅ **Accuracy** — The most intuitive metric (but with limitations)
* 🎯 **Precision** — Trustworthiness of positive predictions
* 🩺 **Recall** — Ability to find all actual positive cases
* ⚖️ **F1 Score** — Balancing precision and recall using harmonic mean
* 🔍 **Specificity** — The forgotten partner of recall
* 📊 **Dashboard** — All metrics together
* 🤖 **Real Model Demo** — Logistic Regression on imbalanced Titanic data
* 📌 **Decision Guide** — Choosing the right metric for the right scenario

> Note: This notebook covers **lecture notes from the instructor**, including explanations, plots, and applied examples.

---

### 🔹 03 — Quiz 1

* 📝 MCQ type quiz based on **Week 5 topics**
* 🎯 Topics included:

  * Recall, Precision, Accuracy, F1 Score
  * Identifying TP, FP, FN, TN
  * Choosing the right metric for scenarios
  * Calculation-based and institution-based questions
* 🏆 Score: 100%

---

## 🛠️ Technologies Used

* 🐍 Python
* 📊 Pandas
* 🔢 NumPy
* 📈 Matplotlib
* 🎨 Seaborn
* 🤖 Scikit-learn

---

## 🎯 Key Learnings

* 📊 Applied different **probability distributions** on real dataset columns
* ✅ Learned how to **interpret classification metrics** effectively
* 🧠 Understood **when to use which metric** for different scenarios
* 🔍 Practiced transforming skewed features for better analysis
* 🏆 Achieved **full score** in Week 5 quiz validating understanding

---

## 🧾 Conclusion

Week 5 strengthened my understanding of **data distributions** and **classification evaluation metrics**.
I gained hands-on experience applying transformations, plotting distributions, and analyzing classification performance, which is crucial for building **reliable ML models**.

---

## 👩‍💻 Author

**Alishba Amjad**

🎓 BS Computer Science Graduate

📍 AI/ML Trainee at NETSOL

---

## ⭐ Note

This repository reflects my **Week 5 learning and practice** with Titanic dataset analysis and classification metrics.
Next week, we will explore **model evaluation, cross-validation, and advanced ML workflows**.

---

✨ **Stay tuned for Week 6! 🚀**


