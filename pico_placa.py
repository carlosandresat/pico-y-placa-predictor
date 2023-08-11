import datetime
import re

class PicoYPlacaPredictor:
    def __init__(self):
        self.rules = {
            0: [1, 2],
            1: [3, 4],
            2: [5, 6],
            3: [7, 8],
            4: [9, 0]
        }

    def get_last_digit(self, license_plate):
        return int(license_plate[-1])
    
    def validate_license_plate(self, license_plate):
        pattern = r'^[A-Za-z]{2,3}-[0-9]{3,4}$'
        return bool(re.match(pattern, license_plate))
    
    def is_morning_restriction(self, time):
        return time >= datetime.datetime.strptime("07:00", "%H:%M") and time <= datetime.datetime.strptime("09:30", "%H:%M")
    
    def is_evening_restriction(self, time):
        return time >= datetime.datetime.strptime("16:00", "%H:%M") and time <= datetime.datetime.strptime("19:30", "%H:%M")
        
    def is_restricted_time(self, time):
        return self.is_morning_restriction(time) or self.is_evening_restriction(time)
    
    def can_drive(self, license_plate, date_str, time_str):
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            time = datetime.datetime.strptime(time_str, "%H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format.")
        
        if not self.validate_license_plate(license_plate):
            raise ValueError("Invalid license plate format.")
        
        day_of_week = date.weekday()
        last_digit = self.get_last_digit(license_plate)
        restricted_digits = self.rules.get(day_of_week, [])

        # Special plates can drive at any time
        special_plate_formats = ["CD", "CC", "OI", "AT"]
        license_plate_prefix = license_plate.split("-")[0]
        if license_plate_prefix in special_plate_formats:
            return True

        if last_digit in restricted_digits:
            if (self.is_restricted_time(time)):
                return False

        return True

def main():
    predictor = PicoYPlacaPredictor()
    
    try:
        license_plate = input("Enter license plate number (e.g., ABC-1234): ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        time_str = input("Enter time (HH:MM): ")

        if not license_plate or not date_str or not time_str:
            print("All fields are required.")
            return
              
        if predictor.can_drive(license_plate, date_str, time_str):
            print("You can drive.")
        else:
            print("You can't drive during this time.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()