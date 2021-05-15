"""CSC148 Lab 1

=== CSC148 Winter 2020 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    # Size N
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5) == 1
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 0) == 0
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 40) == 8
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 44) == -1
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], -5) == -1
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 25) == 5
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 27) == -1
    # size 0 list
    assert binary_search([], 25) == -1
    # size 1 list
    assert binary_search([25], 25) == 0


if __name__ == '__main__':

    import pytest
    pytest.main(['test_search.py'])
