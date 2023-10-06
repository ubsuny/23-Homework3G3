#This unit test tests the cases of a spring constant with a known (real) value,
#as well as the two main cases that would give errors/non physical results
#(zero mass and zero displacement.) This should cover all possible
#use cases of the function.

import unittest

class SpringConstantTest(unittest.TestCase):
  """Unit tests for the spring_constant function."""

  def test_spring_constant_with_known_values(self):
    """Tests the spring_constant function with known values."""

    mass = [1.0]  # kilograms
    displacement = [0.1]  # meters

    expected_spring_constant = [9810]  # Dyne per cm

    actual_spring_constant = calculate_spring_constants(mass, displacement)

    self.assertEqual(expected_spring_constant, actual_spring_constant)

  def test_spring_constant_with_zero_mass(self):
    """Tests the spring_constant function with a zero mass."""

    mass = [0.0]  # kilograms
    displacement = [0.1]  # meters

    expected_spring_constant = [0.0]  # Newtons per meter

    actual_spring_constant = calculate_spring_constants(mass, displacement)

    self.assertEqual(expected_spring_constant, actual_spring_constant)

  def test_spring_constant_with_zero_displacement(self):
    """Tests the spring_constant function with a zero displacement."""

    mass = [1.0]  # kilograms
    displacement = [0.0]  # meters

    expected_spring_constant = ["ERROR"]  # Newtons per meter

    actual_spring_constant = calculate_spring_constants(mass, displacement)

    self.assertEqual(expected_spring_constant, actual_spring_constant)

    self.assertEqual(expected_spring_constant, actual_spring_constant)

if __name__ == '__main__':
  unittest.main()
