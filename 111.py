from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# 自己创建数据
data = {
    "面积": [80, 90, 100, 110, 120],
    "价格": [180, 200, 220, 250, 270]
}

df = pd.DataFrame(data)

X = df[["面积"]]
y = df["价格"]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)