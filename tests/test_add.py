import hypothesis.strategies as st
import pytest
from hypothesis import given

from boilerplate_poetry_project.add import add_int


def test_add_int_success():
    """Test that adding two integers returns the correct sum.
    # basic functionality"""
    assert add_int(2, 3) == 5
    assert add_int(-1, -1) == -2
    assert add_int(0, 0) == 0


# Test for error handling with non-integer inputs
@pytest.mark.parametrize("x, y", [("a", 2), (2, "b"), ("a", "b"), (1.5, 2), (2, 1.5)])
def test_add_int_raises_type_error_on_invalid_input(x, y):
    """Test that a TypeError is raised when non-integers are provided.
    # basic functionality"""
    with pytest.raises(TypeError):
        add_int(x, y)


# Use Hypothesis to test a wide range of integer inputs
@given(x=st.integers(), y=st.integers())
def test_add_int_with_hypothesis(x, y):
    """Test that adding two integers returns the correct sum.
    # hypothesis"""
    assert add_int(x, y) == x + y
