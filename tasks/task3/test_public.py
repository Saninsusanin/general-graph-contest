import pytest
from typing import List
from dataclasses import dataclass

from .task3 import task3, Game


@dataclass
class Case:
    name: str
    n: str
    games: List[Game]
    ans: int

    def __str__(self) -> str:
        return f'task3_test: {self.name}'


TEST_CASES = [
    Case(
        name='1',
        n=4,
        games=[
            (1, 2, 1),
            (2, 3, 1),
            (3, 4, 1),
        ],
        ans=4
    ),
    Case(
        name='2',
        n=3,
        games=[
            (1, 2, 1),
            (1, 2, 2),
            (1, 3, 1),
            (1, 3, 2),
            (2, 3, 1),
            (2, 3, 2),
        ],
        ans=1,
    ),
    Case(
        name='3',
        n=9,
        games=[
            (1, 6, 1),
            (1, 7, 1),
            (2, 6, 1),
            (2, 7, 1),
            (1, 2, 1),
            (1, 2, 2),
            (3, 6, 1),
            (3, 7, 1),
            (4, 6, 1),
            (4, 7, 1),
            (5, 6, 1),
            (5, 7, 1),
            (3, 4, 1),
            (4, 5, 1),
            (5, 3, 1),
            (6, 8, 1),
            (6, 9, 1),
            (7, 8, 1),
            (7, 9, 1),
        ],
        ans=8,
    ),
    Case(
        name='4',
        n=7,
        games=[
            (1, 7, 1),
            (2, 7, 1),
            (4, 7, 1),
            (2, 3, 1),
            (3, 2, 1),
            (4, 5, 1),
            (6, 5, 2),
            (4, 6, 2),
        ],
        ans=7
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case):
    ans = task3(case.n, case.games)
    assert case.ans == ans
