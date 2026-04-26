def enrich_users(data):
    country_map = {
        "PH": "Philippines",
        "US": "United States"
    }

    enriched = []

    for user in data:
        enriched.append({
            "name": user["name"].title(),
            "age": user["age"],
            "country": country_map.get(user["country"], "Unknown"),
            "age_group": "Adult" if user["age"] >= 18 else "Minor"
        })

    return enriched