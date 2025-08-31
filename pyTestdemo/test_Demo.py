import pytest

@pytest.mark.xfail
def test_firstProgram():
    print("Flag the test as expected to fail")
@pytest.mark.smoke
def test_secondProgram():
    print("This is a smoke Test")