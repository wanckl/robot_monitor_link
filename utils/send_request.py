import requests
import logging

default_headers = {
    'User-Agent': 'neuq_robot',
    'Content-Type': 'application/json',
}


def send_request(data_dict: dict, target: str, headers, timeout: int = 10) -> dict:
    try:
        res = requests.post(target, headers if headers else default_headers, data=data_dict, timeout=timeout)
        res.raise_for_status()
        return res.text
    except requests.ConnectionError as e:
        logging.error("Connection refused error: %s", e)
    except requests.exceptions.HTTPError as e:
        logging.error('Http request error: %s', e)
