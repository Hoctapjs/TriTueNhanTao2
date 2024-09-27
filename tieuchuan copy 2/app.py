from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Đọc dữ liệu khoảng cách từ file Excel
def read_distances():
    df = pd.read_excel('distances.xlsx', index_col=0)
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tsp', methods=['POST'])
def tsp_route():
    start_city = request.form.get('start_city')
    locations = read_distances()

    if start_city not in locations.index:
        return jsonify({"error": "City not found!"})

    # Giả sử thuật toán GTS đã được định nghĩa ở đây
    path, total_distance = greedy_tsp_dynamic(start_city, locations)

    # Chuyển đổi total_distance sang kiểu int
    total_distance = int(total_distance)

    return jsonify({
        "path": path,
        "total_distance": total_distance,
        "locations": locations.to_dict()  # Chuyển đổi DataFrame sang dictionary
    })


def greedy_tsp_dynamic(start_city, locations):
    path = [start_city]  # Đường đi khởi đầu
    total_distance = 0
    current_city = start_city

    while len(path) < len(locations.index):
        next_city = min(
            locations.index.difference(path),
            key=lambda city: locations.loc[current_city, city]
        )
        path.append(next_city)
        total_distance += locations.loc[current_city, next_city]
        current_city = next_city

    # Quay về thành phố khởi đầu
    total_distance += locations.loc[current_city, start_city]
    path.append(start_city)
    
    return path, total_distance

if __name__ == '__main__':
    app.run(debug=True)
