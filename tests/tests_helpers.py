import pytest
import datetime
from datetime import datetime
from helpers import *


def test_binary():
    assert binary_search ([2,3,4,5,],1) == (2,0)
    assert binary_search([2,3,4,5,],6) == (None,None)
    assert binary_search([2, 3, 4, 5,6 ], 3) == (3, 1)
    assert binary_search([2, 3, 4, 5, 6], 6) == (6, 4)
    assert binary_search([2, 3, 4, 5,6 ], 2.5) == (3, 1)


def test_time_to_str():
    time = datetime.strptime('03:59:59', '%H:%M:%S')
    assert time_to_str(time) == "03:59:59"
