import pytest
from typing import List
from dataclasses import dataclass

from .task1 import task1, Key


@dataclass
class Case:
    name: str
    preorder: List[Key]
    postorder: List[Key]
    inorder: List[Key]

    def __str__(self) -> str:
        return f'task1_test: {self.name}'


TEST_CASES = [
    Case(
        name='1',
        preorder=[4, 2, 1, 3, 6, 5, 7],
        postorder=[1, 3, 2, 5, 7, 6, 4],
        inorder=[1, 2, 3, 4, 5, 6, 7],
    ),
    Case(
        name='2',
        preorder=[5, 3, 2, 3, 5, 6],
        postorder=[2, 3, 3, 6, 5, 5],
        inorder=[2, 3, 3, 5, 5, 6],
    ),
    Case(
        name='One key',
        preorder=[4],
        postorder=[4],
        inorder=[4],
    ),
    Case(
        name='3',
        preorder=[4, 3, 5],
        postorder=[3, 5, 4],
        inorder=[3, 4, 5],
    ),
    Case(
        name='4',
        preorder=[4, 2, 1],
        postorder=[1, 2, 4],
        inorder=[1, 2, 4],
    ),
    Case(
        name='5',
        preorder=[4, 5, 6, 7],
        postorder=[7, 6, 5, 4],
        inorder=[4, 5, 6, 7],
    ),
    Case(
        name='6',
        preorder=[4, 6, 5, 7],
        postorder=[5, 7, 6, 4],
        inorder=[4, 5, 6, 7],
    ),
    Case(
        name='Empty',
        preorder=[],
        postorder=[],
        inorder=[],
    ),
    Case(
        name='Same elements',
        preorder=[5, 5, 5, 5, 5],
        postorder=[5, 5, 5, 5, 5],
        inorder=[5, 5, 5, 5, 5],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case):
    (postorder, inorder) = task1(case.preorder)
    assert postorder == case.postorder
    assert inorder == case.inorder
