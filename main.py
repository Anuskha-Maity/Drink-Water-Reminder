import time
from plyer import notification

def water_reminder(interval_hours=1):
    """
    Sends a desktop notification to remind the user to drink water at regular intervals.

    Parameters:
    interval_hours (int): Time interval between reminders in hours.
    """
    interval_seconds = interval_hours * 3600
    while True:
        notification.notify(
            title="💧 Stay Hydrated!",
            message="It's time to drink some water. Stay healthy! 😊",
            app_name="Water Reminder",
            timeout=10  # Notification stays for 10 seconds
        )
        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Set your preferred interval in hours
    water_reminder(interval_hours=1)
