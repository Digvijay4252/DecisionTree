import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv('student_performance.csv')

X = data[['hours_studied', 'attendance', 'assignments_completed', 'sleep_hours']]
y = data['result']

pass_map = {'Pass': 1, 'Fail': 0}
y = y.map(pass_map)

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
joblib.dump(pass_map, 'pass_map.pkl')
