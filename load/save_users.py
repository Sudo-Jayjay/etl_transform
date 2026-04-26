import csv

def save_to_csv(data, file_path):
    if not data:
        return

    keys = data[0].keys()

    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)