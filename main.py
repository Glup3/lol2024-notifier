import requests
import schedule
import time
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def log(message):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{formatted_datetime}] {message}", flush=True)

def check_webpage():
    url = "https://www.theo2.co.uk/events/detail/the-2024-league-of-legends-world-championship-finals"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    button = soup.find("div", class_="ticket-button")

    if button:
        return button.text.strip().lower() == "On sale TBA".lower()
    else:
        raise RuntimeError("button not found")

def send_notification_homeassistant(data):
    hass_url = os.getenv("HASS_API_URL")
    api_token = os.getenv("HASS_API_KEY")

    url = hass_url + "/api/services/notify/notify"

    headers = {
        "Authorization": "Bearer " + api_token,
        "content-type": "application/json",
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    log("Sent notification to all home assistant devices")

def main():
    is_tba = check_webpage()    

    if is_tba == False:
        data = {
            "title": "LoL Worlds 2024 Finals Tickets are AVAILABLE",
            "message": "Quickly go and buy 2 tickets!!!",
            "data": {
                "url": "https://www.theo2.co.uk/events/detail/the-2024-league-of-legends-world-championship-finals"
            }
        }

        send_notification_homeassistant(data)
    else:
        log("Tickets are still UNAVAILABLE")
        

if __name__ == "__main__":
    schedule.every(1).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)