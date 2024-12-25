from main import factorial
from hypothesis import given, strategies as st
import math

@given(st.integers(min_value=0, max_value=100))
def test_factorial(n):
    assert factorial(n) == math.factorial(n)    #Сравнение с build-in функционалом