import requests
import json

def get_id():
    pass

def upload_pkg():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Content-Type': 'application/json',
        'Cookie': 'session:eyJ1c2VyX2lkIjoxfQ.XM2GHw.SHJseg_EOjBUAKvjGQfzn99twg8'
        # 'Connection':'keep-alive'
    }

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
    payload = "{\n    \"robot_id\": \"1\",\n    \"direction_x\": \"0\",\n    \"direction_y\": \"0\",\n    \"direction_z\": \"0\",\n    \"position_x\": \"0\",\n    \"position_y\": \"0\",\n    \"position_z\": \"0\",    \n    \"velocity_x\": \"0\",\n    \"velocity_y\": \"0\",\n    \"velocity_z\": \"0\",\n    \"ip\": \"127.0.0.1\",\n    \"data\": \"{}\"\n}"

    server_url = "http://106.13.140.135/api/v1/data/add"
    try:
        res = requests.post(server_url, headers=headers, data=payload, timeout=10)
        res.raise_for_status()  # lead to exception when status isn't 200
        if res.encoding == "ISO-8859-1":
            res.encoding = res.apparent_encoding
        print(res.text)
        # print(res.text.split("\n")[16], end="")

    except requests.ConnectionError:
        print("Connection refused!")
    except requests.exceptions.HTTPError:
        print("URL Error!")

if __name__ == "__main__":
    upload_pkg()
