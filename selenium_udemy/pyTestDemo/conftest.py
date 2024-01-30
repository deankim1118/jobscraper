import pytest
### fixtures are used as setup and tear down methods for test cases 
### conftest.py file make it available to all test cases

@pytest.fixture(scope="class")
def setup():
    print("This will excute first")
    yield
    print("This will excute last")
    
@pytest.fixture(scope="class")
def dataLoad():
    print("user profile data is being loaded")
    return ["dean", "Kim", "1985/11/18"]