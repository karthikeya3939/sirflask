import pytest
def fn(x):
    return x+2
def test_sam():
    assert fn(10)==13
    assert fn(11) == 13