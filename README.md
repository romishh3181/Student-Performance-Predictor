
# Student Exam Performance Predictor

This project predicts a student's math score based on several input features such as gender, ethnicity, parental education, lunch type, and test preparation course. The prediction is made using a machine learning model trained on the [Students Performance dataset from Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Model Details](#model-details)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## Project Overview

The **Student Exam Performance Predictor** is a Flask web application that predicts a student's math score based on various inputs. It uses a machine learning model trained on the Students Performance dataset from Kaggle. The inputs are collected via a form in the web application, and the model predicts the likely math score based on the input features.

## Dataset

The dataset used is the **Students Performance Dataset** from Kaggle, which contains information about students' exam scores in subjects like math, reading, and writing, along with demographic details and educational background. The main features used in this project include:

- **Gender**
- **Race/Ethnicity**
- **Parental Level of Education**
- **Lunch Type**
- **Test Preparation Course**
- **Reading and Writing Scores**

You can download the dataset from [here](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

## Technologies Used

- **Python**
- **Flask**: For building the web application.
- **scikit-learn**: For building the machine learning model.
- **HTML/CSS**: For the front-end form.
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical operations.
- **Jinja2**: For rendering HTML templates in Flask.

## How to Run the Project

### 1. Clone the repository:
```bash
git clone https://github.com/romishh3181/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

### 2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app:
```bash
python app.py
```

### 4. Open the web app:
Go to `http://127.0.0.1:5000` in your browser to access the Student Performance Predictor form.

### 5. Input Data:
Fill in the details such as gender, parental education, and test scores, and click **Predict** to get the predicted math score.

## Model Details

The machine learning model is trained using the multiple algorithms to predict math score. 
It performs hyperparameter tuning to find the best Machine Learning algorithm for prediction. 

The model takes the following features as input:

- **Gender**
- **Race/Ethnicity**
- **Parental Level of Education**
- **Lunch Type**
- **Test Preparation Course**
- **Reading and Writing Scores**

The model was evaluated using the R2_Score metric, and cross-validation was performed to ensure robustness.

## Contributors

- **Rohan Mishra** - [GitHub](https://github.com/romishh3181)
