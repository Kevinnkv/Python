# Viet chuong trinh thuật toán Random Forest
# Su dung thu vien scikit-learn
# Du lieu iris
# Chia du lieu thanh 2 phan: train va test
# Su dung Random Forest de train du lieu
# Dua ra ket qua du doan
# Su dung accuracy_score de danh gia ket qua
# code Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Load du lieu
iris = load_iris()
X = iris.data
y = iris.target
# Chia du lieu thanh 2 phan: train va test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# Train du lieu
clf = RandomForestClassifier()
