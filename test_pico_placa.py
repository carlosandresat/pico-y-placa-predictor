import unittest
from datetime import datetime, timedelta
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

if __name__ == "__main__":
    unittest.main()
