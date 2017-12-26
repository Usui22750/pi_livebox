import requests
import json

def init_ip():
    with open('./livebox.json', 'r+') as file:
        try:
            data = json.load(file)
        except:
            data = {}
    init_ip = True
    found_ip = None
    if 'ip' in data:
        ret = requests.get(data['ip'])
        found_ip = data['ip']
        if ret.status_code == 200:
            init_ip = False
    if init_ip:
        ip = "http://192.168.1.{}:8080"
        for i in range(0, 255):
            format_ip = ip.format(i)
            try:
                ret = requests.get(format_ip, timeout=0.01)
            except:
                continue
            if ret.status_code == 200:
                data['ip'] = format_ip
                found_ip = format_ip
                break
    with open('./livebox.json', 'w+') as file:
        json.dump(data, fp=file)
    return found_ip
