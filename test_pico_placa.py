import unittest
from pico_placa import PicoYPlacaPredictor

class TestPicoYPlacaPredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = PicoYPlacaPredictor()
    
    def test_can_drive_during_allowed_times(self):
        # Monday, last digit 4, allowed time
        self.assertTrue(self.predictor.can_drive("ABC-1234", "2023-08-14", "08:30"))
        # Friday, last digit 6, allowed time
        self.assertTrue(self.predictor.can_drive("XYZ-9876", "2023-08-18", "17:30"))
    
    def test_cannot_drive_during_restricted_times(self):
        # Tuesday, last digit 4, restricted time
        self.assertFalse(self.predictor.can_drive("ABC-1234", "2023-08-15", "08:30"))
        # Wednesday, last digit 6, restricted time
        self.assertFalse(self.predictor.can_drive("XYZ-9876", "2023-08-16", "17:30"))

    def test_valid_license_plate(self):
        self.assertTrue(self.predictor.validate_license_plate("ABC-1234"))
        self.assertTrue(self.predictor.validate_license_plate("XYZ-9876"))
    
    def test_invalid_license_plate(self):
        self.assertFalse(self.predictor.validate_license_plate("AB12-123"))
        self.assertFalse(self.predictor.validate_license_plate("ABC-12345"))
        self.assertFalse(self.predictor.validate_license_plate("ABCD-123"))

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            self.predictor.can_drive("ABC-1234", "2023/08/14", "08:30")
    
    def test_invalid_time_format(self):
        with self.assertRaises(ValueError):
            self.predictor.can_drive("ABC-1234", "2023-08-14", "8:30 AM")

    def test_edge_cases(self):
        # Sunday should not restrict any digit
        self.assertTrue(self.predictor.can_drive("ABC-1234", "2023-08-13", "08:30"))
        # Test the latest allowed time 
        self.assertTrue(self.predictor.can_drive("XYZ-9876", "2023-08-16", "06:59"))
        # Test the earliest restricted time
        self.assertFalse(self.predictor.can_drive("XYZ-9876", "2023-08-16", "07:00"))
        # Test the latest restricted time
        self.assertFalse(self.predictor.can_drive("XYZ-9876", "2023-08-16", "19:30"))
        # Test the earliest allowed time 
        self.assertTrue(self.predictor.can_drive("XYZ-9876", "2023-08-16", "19:31"))

if __name__ == "__main__":
    unittest.main()
