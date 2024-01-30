import pytest    

@pytest.mark.usefixtures("setup")
class TestFixtures:
    def test_program1(self):
        print("1 :Hello", "This will excute it after fixture method")

    def test_program2(self):
        print("2 :Hello", "This will excute it after fixture method")
        
    def test_program3(self):
        print("3 :Hello", "This will excute it after fixture method")
        
    def test_program4(self):
        print("4 :Hello", "This will excute it after fixture method")