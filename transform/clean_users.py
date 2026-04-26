def clean_users(data):
    cleaned = []

    for user in data:
        name = user["name"].strip().lower()
        age = user["age"]
        country = user["country"].upper()

        # Handle missing age
        if age == "":
            continue

        cleaned.append({
            "name": name,
            "age": int(age),
            "country": country
        })

    return cleaned