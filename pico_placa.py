class PicoYPlacaPredictor:
    def __init__(self):
        pass
    
    def can_drive(self, license_plate, date_str, time_str):
        return True
    

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