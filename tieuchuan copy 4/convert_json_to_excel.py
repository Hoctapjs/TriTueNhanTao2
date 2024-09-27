import pandas as pd
import json

# Đọc dữ liệu từ file JSON
with open('distances.json', 'r', encoding='utf-8') as f:
    distances = json.load(f)

# Chuyển đổi dữ liệu thành DataFrame
df = pd.DataFrame(distances)

# Ghi DataFrame vào file Excel
df.to_excel('distances.xlsx', index=True)
