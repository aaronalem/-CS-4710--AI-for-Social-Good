import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


dataset = pd.read_csv('Ethos_Dataset_Binary.csv')
col_names = ['comment', 'isHate']
X = dataset['comment']
y = dataset['isHate']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

clf = DecisionTreeClassifier(random_state=42)

clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
print("Ethos data set")
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))

print("---------------------------")
print("Malignant data set")
dataset2 = pd.read_csv('Malignanttrain.csv')
col_names = ['comment_text', 'malignant']
X_test1 = vectorizer.transform(dataset['comment'])
y_test1 = dataset['isHate']
y_pred1 = clf.predict(X_test1)

print("Accuracy:",metrics.accuracy_score(y_test1, y_pred1))
print("Classification Report:", classification_report(y_test1, y_pred1))
