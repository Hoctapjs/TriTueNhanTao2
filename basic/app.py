from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Tạo khoảng cách giữa các thành phố dưới dạng ma trận
cities = ['A', 'B', 'C', 'D']
distances = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Hàm GTS để tính toán lộ trình
def greedy_tsp(start_city):
    visited = [start_city]
    current_city = start_city
    total_distance = 0

    while len(visited) < len(cities):
        nearest_city = None
        shortest_distance = math.inf

        # Tìm thành phố gần nhất chưa được thăm
        for city, distance in distances[current_city].items():
            if city not in visited and distance < shortest_distance:
                nearest_city = city
                shortest_distance = distance

        # Di chuyển tới thành phố gần nhất
        if nearest_city:
            visited.append(nearest_city)
            total_distance += shortest_distance
            current_city = nearest_city

    # Quay về thành phố xuất phát
    total_distance += distances[current_city][start_city]
    visited.append(start_city)

    return visited, total_distance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    data = request.json
    start_city = data['start_city']
    
    # Tính toán lộ trình với GTS
    route, total_distance = greedy_tsp(start_city)
    
    return jsonify({
        'route': route,
        'total_distance': total_distance
    })

if __name__ == '__main__':
    app.run(debug=True)
