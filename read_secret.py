import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
db_password = os.getenv("DB_PASSWORD")
api_secret = os.getenv("API_SECRET")

print("Application:", app_name)
print("Database password loaded:", bool(db_password))
print("API secret loaded:", bool(api_secret))
