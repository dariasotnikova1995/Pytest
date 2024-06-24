import pytest
from pixel import Pixel

def test_pixel_initialization():
    p = Pixel(100, 150, 200)
    assert p.red == 100
    assert p.green == 150
    assert p.blue == 200

def test_pixel_initialization_out_of_range():
    with pytest.raises(ValueError):
        Pixel(256, 0, 0)
    with pytest.raises(ValueError):
        Pixel(0, -1, 0)
    with pytest.raises(ValueError):
        Pixel(0, 0, 256)

def test_pixel_addition():
    p1 = Pixel(100, 150, 200)
    p2 = Pixel(50, 50, 100)
    result = p1 + p2
    assert result == Pixel(150, 200, 255)  # Clamping to 255

def test_pixel_subtraction():
    p1 = Pixel(100, 150, 200)
    p2 = Pixel(50, 100, 250)
    result = p1 - p2
    assert result == Pixel(50, 50, 0)  # Clamping to 0

def test_pixel_multiplication():
    p = Pixel(10, 20, 30)
    result = p * 2
    assert result == Pixel(20, 40, 60)
    result = p * 10
    assert result == Pixel(100, 200, 255)  # Clamping to 255

def test_pixel_multiplication_invalid_factor():
    p = Pixel(10, 20, 30)
    with pytest.raises(TypeError):
        p * "invalid"
    with pytest.raises(ValueError):
        p * 0

def test_pixel_division():
    p = Pixel(30, 60, 90)
    result = p / 2
    assert result == Pixel(15, 30, 45)

def test_pixel_division_invalid_factor():
    p = Pixel(30, 60, 90)
    with pytest.raises(TypeError):
        p / "invalid"
    with pytest.raises(ValueError):
        p / 0

def test_pixel_equality():
    p1 = Pixel(10, 20, 30)
    p2 = Pixel(10, 20, 30)
    p3 = Pixel(30, 20, 10)
    assert p1 == p2
    assert p1 != p3

def test_pixel_str():
    p = Pixel(10, 20, 30)
    expected_str = "Pixel object\n\tRed: 10\n\tGreen: 20\n\tBlue: 30"
    assert str(p) == expected_str

def test_pixel_repr():
    p = Pixel(10, 20, 30)
    assert repr(p) == "Pixel(10, 20, 30)"