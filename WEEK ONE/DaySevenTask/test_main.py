import pytest
import DaySevenTask.code


@pytest.mark.advanced
def test_square():
    assert DaySevenTask.code.square(2) == 4


@pytest.mark.basic
def test_add():
    assert DaySevenTask.code.add(2, 3) == 5


@pytest.mark.basic
def test_sub():
    assert DaySevenTask.code.sub(5, 3) == 2
