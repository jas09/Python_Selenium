import pytest


@pytest.mark.smoke
def test_firstProgramDemo():
    print("This is a smoke Test")
@pytest.mark.skip
def test_secondProgramDemo():
    print("I want this test to be skipped")