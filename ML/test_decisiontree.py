from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Nhập dữ liệu từ người dùng
temperature = float(input("Nhập nhiệt độ (độ C): "))
humidity = float(input("Nhập độ ẩm (%): "))
windy = input("Có gió hay không (True/False): ").lower()  # Chuyển đổi về chữ thường

# Chuyển đổi dữ liệu gió thành giá trị boolean
if windy == 'true':
    windy = True
else:
    windy = False

# Sample dataset (features: temperature, humidity, windy; labels: Go out or not)
X = [[30, 60, False], [25, 70, True], [20, 80, False], [15, 75, False], [22, 90, True]]
y = ['Yes', 'Yes', 'No', 'Yes', 'No']

# Thêm dữ liệu mới từ người dùng vào dataset
X.append([temperature, humidity, windy])

# Chia dataset thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo bộ phân loại cây quyết định
clf = DecisionTreeClassifier()

# Huấn luyện bộ phân loại
clf.fit(X_train, y_train)

# Tạo dự đoán
y_pred = clf.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
print("Độ chính xác:", accuracy)

# Dự đoán cho dữ liệu mới
new_data = [[temperature, humidity, windy]]
prediction = clf.predict(new_data)
print("Dự đoán cho dữ liệu mới:", prediction)