from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 假设 X 是特征矩阵，y 是目标变量
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)