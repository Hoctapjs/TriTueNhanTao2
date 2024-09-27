import pandas as pd
import json

# Chuyển đổi khoảng cách từ JSON thành Excel
def convert_distances_to_excel(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        distances = json.load(f)

    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame(distances)

    # Ghi DataFrame vào file Excel
    df.to_excel(output_file, index=True)

# Chuyển đổi tọa độ từ JSON thành Excel
def convert_coordinates_to_excel(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        coordinates = json.load(f)

    # Chuyển đổi dữ liệu thành DataFrame
    coords_df = pd.DataFrame(coordinates).T  # Chuyển đổi để có dạng đúng

    # Ghi DataFrame vào file Excel
    coords_df.to_excel(output_file, index=True)

if __name__ == '__main__':
    # Đường dẫn tới file JSON và file Excel đầu ra
    distances_json = 'data/distances.json'
    distances_excel = 'data/distances.xlsx'
    coordinates_json = 'data/coordinates.json'
    coordinates_excel = 'data/coordinates.xlsx'

    # Chuyển đổi dữ liệu
    convert_distances_to_excel(distances_json, distances_excel)
    convert_coordinates_to_excel(coordinates_json, coordinates_excel)

    print("Đã chuyển đổi thành công!")
