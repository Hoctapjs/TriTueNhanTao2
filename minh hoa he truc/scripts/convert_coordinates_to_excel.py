import pandas as pd
import json

# Đọc dữ liệu tọa độ từ file JSON
with open('coordinates.json', 'r', encoding='utf-8') as f:
    coordinates = json.load(f)

# Chuyển đổi dữ liệu thành DataFrame
df = pd.DataFrame(coordinates).T  # Chuyển đổi kiểu dữ liệu

# Ghi DataFrame vào file Excel
df.to_excel('coordinates.xlsx', index=True)
