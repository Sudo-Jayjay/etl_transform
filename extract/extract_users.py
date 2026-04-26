import json

def extract_users(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)