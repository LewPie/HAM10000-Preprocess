import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

# Đường dẫn đến thư mục chứa dataset
dataset_path = 'path_to_ham10000'

# Đường dẫn đến thư mục đầu ra
output_path = 'data3'
train_path = os.path.join(output_path, 'train')
test_path = os.path.join(output_path, 'test')

# Tạo các thư mục đầu ra nếu chưa tồn tại
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Đọc file CSV chứa thông tin về dataset
csv_file = os.path.join(dataset_path, 'HAM10000_metadata.csv')  # Thay tên file nếu khác
metadata = pd.read_csv(csv_file)

# Tạo danh sách các lớp bệnh từ cột 'dx' trong metadata
diseases = metadata['dx'].unique()

# Tạo thư mục cho mỗi lớp bệnh
for disease in diseases:
    os.makedirs(os.path.join(train_path, disease), exist_ok=True)
    os.makedirs(os.path.join(test_path, disease), exist_ok=True)

# Phân chia dữ liệu thành train và test
for disease in diseases:
    # Lọc các ảnh thuộc lớp bệnh này
    disease_data = metadata[metadata['dx'] == disease]
    
    # Phân chia thành train và test
    train_data, test_data = train_test_split(disease_data, test_size=0.2, random_state=42)

    # Di chuyển ảnh vào các thư mục tương ứng
    for _, row in train_data.iterrows():
        src = os.path.join(dataset_path, 'images', row['image_id'] + '.jpg')  # Thay đổi phần mở rộng nếu cần
        dst = os.path.join(train_path, disease, row['image_id'] + '.jpg')
        shutil.copy(src, dst)

    for _, row in test_data.iterrows():
        src = os.path.join(dataset_path, 'images', row['image_id'] + '.jpg')  # Thay đổi phần mở rộng nếu cần
        dst = os.path.join(test_path, disease, row['image_id'] + '.jpg')
        shutil.copy(src, dst)

print("Dataset đã được tổ chức thành công!")
