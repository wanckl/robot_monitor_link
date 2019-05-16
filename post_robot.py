import json
from utils.send_request import send_request


def upload_pkg():
    post_dic = {
        "robot_id": 65535,
        "position_x": "0",
        "position_y": "0",
        "position_z": "0",
        "velocity_y": "0",
        "velocity_x": "0",
        "velocity_z": "0",
        "direction_x": "0",
        "direction_y": "0",
        "direction_z": "0",
        "battery": 80,
        "temperature": 30,
        "ip": "localhost",
        "data": "Null",
    }
    json_pkg = json.dumps(post_dic)
    payload = {'position_y': '0', 'direction_y': '0', 'data': '{}', 'robot_id': '1', 'direction_x': '0',
               'position_x': '0', 'velocity_z': '0', 'velocity_y': '0', 'direction_z': '0', 'velocity_x': '0',
               'ip': '127.0.0.1', 'position_z': '0'}

    server_url = "http://106.13.140.135/api/v1/data/add"
    send_request(payload, server_url, headers=None, timeout=10)


if __name__ == "__main__":
    upload_pkg()
