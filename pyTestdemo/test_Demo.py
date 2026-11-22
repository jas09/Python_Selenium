import pytest

@pytest.mark.xfail
def test_firstProgram():
    print("This is a smoke Test 1")
@pytest.mark.smoke
def test_secondProgram():
    print("This is a smoke Test")