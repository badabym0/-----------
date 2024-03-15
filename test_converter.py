import pytest
from convertera import cm_to_inches

@pytest.mark.parametrize("input_cm, expected_inches", [
    (0, 0),
    (2.54, 1),
    (5, 1.97),
    (10, 3.94),
    (20, 7.87),
    (-2.54, -1),
    (-5, -1.97),
    (-10, -3.94),
    (-20, -7.87),
    (0.03, 0.01),
    (0.1, 0.04),
    (0.345, 0.14),
])
def test_cm_to_inches(input_cm, expected_inches):
    assert cm_to_inches(input_cm) == expected_inches
