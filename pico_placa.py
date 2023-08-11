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
    
    def can_drive(self, license_plate, date_str, time_str):
        last_digit = self.get_last_digit(license_plate)
        return last_digit % 2 == 0     #Placeholder condition

def main():
    predictor = PicoYPlacaPredictor()
    
    license_plate = input("Enter license plate number (e.g., ABC-1234): ")
    date_str = input("Enter date (YYYY-MM-DD): ")
    time_str = input("Enter time (HH:MM): ")
              
    if predictor.can_drive(license_plate, date_str, time_str):
        print("You can drive.")
    else:
        print("You can't drive during this time.")

if __name__ == "__main__":
    main()