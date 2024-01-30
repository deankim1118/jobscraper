import pytest

@pytest.mark.usefixtures("dataLoad")
class Test_dataLoader:
    def test_load(self, dataLoad):
        print(f"User profile is loaded{dataLoad}")