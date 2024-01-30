### Any pytest file name, method name should be start with test_
### Any code should be wrapped in method only
### -k stands for method  names excution, -s shows in out put, -v stands for more info metadata
## ex) py.test -k Program -v -s
### Can run specific file with py.test <filename>
### Method name should have sense
### Can mark(tag) specific tests using "@pytest.mark.summation" and then run with -m
### Can mark(tag) specific tests with "@pytest.mark.skip"

import pytest

@pytest.mark.printing
@pytest.mark.skip
def test_firstProgram():
    print("Hello, world!")


@pytest.mark.summation
def test_3Program(setup):
    a = 4
    b = 6
    assert a+2 == b, "Summation isn't correct"
   
    