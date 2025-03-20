import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('customerchurn.csv')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna(df.median(numeric_only=True), inplace=True)
df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'], drop_first=True)
df['Churn'] = df['Churn'].str.strip().str.capitalize()
df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
df['AvgMonthlySpend'] = df['TotalCharges'] / (df['tenure'] + 1)
df['LongTermCustomer'] = (df['tenure'] > 12).astype(int)

X = df.drop(columns=['customerID', 'Churn']) 
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

feature_importance = pd.Series(model.coef_[0], index=X.columns)
feature_importance.nlargest(10).plot(kind='barh')
plt.title('Top Features Driving Customer Churn')
plt.show()