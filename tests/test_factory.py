import pytest

from tesla.factory import Tesla

car_1 = Tesla("Model_3", "Red")
car_1.seats_count = 1

def test_color():
    # CHECK IF COLOR IS CORRECT
    assert car_1.color == "Red"

def test_seats_count():
    # CHECK THE NUMBER OF SEATS
    assert car_1.seats_count == 5