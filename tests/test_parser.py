from typing import List

import pytest

from mypy_silent.parser import FilePosition
from mypy_silent.parser import get_info_form_mypy_output
from mypy_silent.parser import MypyMessage


@pytest.mark.parametrize(
    "input,output",
    (
        (["test"], []),
        (
            [
                "utils/template.py:49: error: Cannot assign to a method",
                "utils/template.py:53: error: Statement is unreachable",
            ],
            [
                MypyMessage(
                    position=FilePosition(filename="utils/template.py", line=49),
                    message="error: Cannot assign to a method",
                ),
                MypyMessage(
                    position=FilePosition(filename="utils/template.py", line=53),
                    message="error: Statement is unreachable",
                ),
            ],
        ),
    ),
)
def test_get_info_form_mypy_output(input: List[str], output: List[MypyMessage]) -> None:
    assert list(get_info_form_mypy_output(input)) == output
