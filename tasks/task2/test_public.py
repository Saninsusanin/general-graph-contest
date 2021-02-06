import pytest
from typing import List
from dataclasses import dataclass

from .task2 import task2


@dataclass
class Case:
    name: str
    p: str
    t: str
    ans: List[int]

    def __str__(self) -> str:
        return f'task2_test: {self.name}'


TEST_CASES = [
    Case(
        name='base',
        p='ab?',
        t='ababcabc',
        ans=[0, 2, 5]
    ),
    Case(
        name='All wildcards',
        p='???',
        t='ababcabc',
        ans=[0, 1, 2, 3, 4, 5]
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case):
    ans = task2(case.p, case.t)
    assert case.ans == sorted(ans)
