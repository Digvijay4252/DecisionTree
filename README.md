<!-- # DecisionTree


<img width="872" height="746" alt="image" src="https://github.com/user-attachments/assets/e544c60a-2dbd-475b-9883-059a438387e1" /> -->


## Decision Tree Classifier – Student Performance Predictor

This project implements a Decision Tree Classifier using Python and Flask to predict student performance based on various input features such as study hours, attendance, assignments, and more.

---

## What is a Decision Tree?

A Decision Tree is a supervised learning algorithm used for both classification and regression tasks. It models decisions and their possible consequences using a tree-like structure of conditions and outcomes.

---

## Model Details
- Algorithm: DecisionTreeClassifier from scikit-learn

- Criterion: Gini impurity or entropy

- Encoded labels using a dictionary for mapping

- Trained on a student performance dataset

- Model and label mappings are saved using joblib

---

##  Project Structure
```
DecisionTree/
├── app.py               # Flask web application
├── train_model.py       # Model training script
├── student_data.csv     # Input dataset
├── model.pkl            # Trained Decision Tree model
├── pass_map.pkl         # Mapping for encoded target variable
│
├── templates/
│   └── index.html       # Web interface
└── README.md            # Project documentation


```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/DecisionTree.git
cd DecisionTree
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:10000

# Sample Input
```
Hours_Studied: 5
Attendance: 88
Assignments_Completed: 90
Sleep_Hours: 6
Prediction Output: Yes (Pass)

```
## Screenshots

### Step 1
<img width="872" height="746" alt="image" src="https://github.com/user-attachments/assets/e544c60a-2dbd-475b-9883-059a438387e1" />

### Step 2
<img width="1883" height="906" alt="image" src="https://github.com/user-attachments/assets/0fce8bb9-9632-4493-b76e-5a0d804146d0" />

### Step 3
<img width="1901" height="914" alt="image" src="https://github.com/user-attachments/assets/b79d8cfd-e6a8-499e-bd92-146617fe228e" />

## Future Improvements
Future Enhancements
Add model visualization (tree graph)

Include feature importance chart

Improve input validation and error handling

Add option to upload custom CSV for prediction
