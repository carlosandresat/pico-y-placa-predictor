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
    
    def validate_license_plate(self, license_plate):
        pattern = r'^[A-Za-z]{2,3}-[0-9]{3,4}$'
        return bool(re.match(pattern, license_plate))
    
    def validate_date_format(self, date_str):
        pattern = r'^\d{4}-(?:0[1-9]|1[0-2])-?(?:0[1-9]|[12]\d|3[01])$'
        return bool(re.match(pattern, date_str))
    
    def validate_time_format(self, time_str):
        pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d$'
        return bool(re.match(pattern, time_str))
    
    def parse_date(self, date_str):
        year, month, day = map(int, date_str.split("-"))
        return year, month, day

    def parse_time(self, time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours, minutes

    def calculate_day_of_week(self, year, month, day):
        # Zeller's congruence algorithm
        if (month == 1) :
            month = 13
            year = year - 1
 
        if (month == 2) :
            month = 14
            year = year - 1
        q = day
        m = month
        k = year % 100
        j = year // 100
        h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
        h = (h+5) % 7
        return h
    
    def get_last_digit(self, license_plate):
        return int(license_plate[-1])
    
    def is_special_plate(self, license_plate):
        special_plate_formats = ["CD", "CC", "OI", "AT"]
        license_plate_prefix = license_plate.split("-")[0]
        return license_plate_prefix in special_plate_formats
    
    def is_morning_restriction(self, hours, minutes):
        total_minutes = hours * 60 + minutes

        morning_start = 7 * 60  # 7:00 am
        morning_end = 9 * 60 + 30  # 9:30 am       

        return total_minutes >= morning_start and total_minutes <= morning_end
    
    def is_evening_restriction(self, hours, minutes):
        total_minutes = hours * 60 + minutes

        evening_start = 16 * 60  # 4:00 pm
        evening_end = 19 * 60 + 30 # 7:30 pm

        return total_minutes >= evening_start and total_minutes <= evening_end
        
    def is_restricted_time(self, hours, minutes):
        return self.is_morning_restriction(hours, minutes) or self.is_evening_restriction(hours, minutes)
    
    
    
    def can_drive(self, license_plate, date_str, time_str):
        if not self.validate_license_plate(license_plate):
            raise ValueError("Invalid license plate format.")
        
        if not self.validate_date_format(date_str):
            raise ValueError("Invalid date format.")
        
        if not self.validate_time_format(time_str):
            raise ValueError("Invalid time format.")
        
        year, month, day = self.parse_date(date_str)
        hours, minutes = self.parse_time(time_str)
        
        day_of_week = self.calculate_day_of_week(year, month, day)
        last_digit = self.get_last_digit(license_plate)
        restricted_digits = self.rules.get(day_of_week, [])

        # Special plates can drive at any time
        if self.is_special_plate(license_plate):
            return True

        if last_digit in restricted_digits and self.is_restricted_time(hours, minutes):
            return False

        return True

def get_user_input(value):
    return input(value).strip()

def main():
    predictor = PicoYPlacaPredictor()
    
    try:
        license_plate = get_user_input("Enter license plate number (e.g., ABC-1234): ")
        date_str = get_user_input("Enter date (YYYY-MM-DD): ")
        time_str = get_user_input("Enter time (HH:MM): ")

        if not license_plate or not date_str or not time_str:
            print("All fields are required.")
            return
              
        if not predictor.can_drive(license_plate, date_str, time_str):
            print("You can't drive during this time.")
        else:
            print("You can drive.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()