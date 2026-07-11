from faker import Faker
import random
import csv

fake = Faker("en_IN")

categories = [
    "Restaurant",
    "Electronics",
    "Medical",
    "Gym",
    "School",
    "Hotel",
    "Salon",
    "Cafe",
    "Clothing",
    "Mobile"
]

cities = [
    "Delhi",
    "Agra",
    "Jaipur",
    "Lucknow",
    "Noida",
    "Gurgaon",
    "Kanpur",
    "Mumbai",
    "Pune",
    "Bengaluru"
]

sources = [
    "Google",
    "Justdial",
    "Sulekha"
]

with open("business_listings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "business_name",
        "category",
        "city",
        "address",
        "phone",
        "source"
    ])

    for _ in range(500):
        writer.writerow([
            fake.company(),
            random.choice(categories),
            random.choice(cities),
            fake.address().replace("\n", ", "),
            fake.phone_number(),
            random.choice(sources)
        ])

print("✅ 500 business listings generated successfully!")