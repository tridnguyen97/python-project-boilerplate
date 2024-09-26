import hypothesis.strategies as st
import pytest
from hypothesis import given

from boilerplate_poetry_project.multiply import multiply_int


def test_multiply_int_success():
    """Test that multiplying two integers returns the correct product.
    # basic functionality"""
    assert multiply_int(2, 3) == 6
    assert multiply_int(-1, -1) == 1
    assert multiply_int(0, 0) == 0


@pytest.mark.parametrize("x, y", [("a", 2), (2, "b"), ("a", "b"), (1.5, 2), (2, 1.5)])
def test_multiply_int_raises_type_error_on_invalid_input(x, y):
    """Test that a TypeError is raised when non-integers are provided."""
    with pytest.raises(TypeError):
        multiply_int(x, y)


@given(x=st.integers(), y=st.integers())
def test_multiply_int_with_hypothesis(x, y):
    """Test that multiplying two integers returns the correct product using Hypothesis."""
    assert multiply_int(x, y) == x * y
