from __future__ import annotations
from typing import Dict, Any, List


class Module:
    """A class representing a full Python program.

    === Attributes ===
    body: A sequence of statements.
    """
    body: List[Statement]

    def __init__(self, body: List[Statement]) -> None:
        """Initialize a new module with the given body."""
        self.body = body

    def evaluate(self) -> None:
        """Execute the statements in this module."""
        env = {}
        for statement in self.body:
            statement.evaluate(env)

    def __str__(self) -> str:
        """Return a string representation of this module."""
        return '\n'.join(str(stmt) for stmt in self.body)


class Statement:
    """An abstract class representing a Python statement.

    We think of a Python statement as being a more general piece of code than a
    single expression, and that can have some kind of "effect".
    """

    def evaluate(self, env: Dict[str, Any]) -> Optional[Any]:
        """Evaluate this statement with the given environment.

        This should have the same effect as evaluating the statement by the
        real Python interpreter.

        Note that the return type here is Optional[Any]: evaluating a statement
        could produce a value (this is true for all expressions), but it might
        only have a *side effect* like mutating `env` or printing something.
        """
        raise NotImplementedError


################################################################################
# Expressions
################################################################################
class Expr(Statement):
    """An abstract class representing a Python expression.

    This subclass is useful even though it adds no additional methods or
    attributes to its superclass, because we use it to *restrict the types of
    expressions that can appear inside other expressions*.

    For example, in a BinOp instance, its left and right attributes must refer
    to *expressions*, and cannot use other forms of statements like assignments.
    """
    pass
# Q8


class ListComprehension(Expr):
    """
    A list comprehension restricted to using a for range. 
    The general form is [build for target in range(start, stop) if cond]
    """

    def __init__(self, build: Expr, target: str, start: Expr, stop: Expr, cond: Expr) -> None:
        self.build = build
        self.target = target
        self.start = start
        self.stop = stop
        self.cond = cond

    def evaluate(self, env: Dict[str, Any]) -> List[Any]:
        lst = []
        for i in range(self.start.evaluate(env), self.stop.evaluate(env)):
            env[self.target] = i
            if self.cond.evaluate(env):
                lst.append(self.build.evaluate(env))
        return lst


# Q5
def reverse_list(lst: List[Any], start: int, end: int) -> None:
    """
    Reverse the list from start - end (inclusive).
    """
    if start >= end:
        return
    else:
        # Swap start and end
        lst[start], lst[end] = lst[end], lst[start]
        reverse_list(lst, start + 1, end - 1)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    reverse_list(lst, 0, 4)
    assert lst == [5, 4, 3, 2, 1]
    lst = [1, 2, 3, 4, 5]
    reverse_list(lst, 0, 3)
    assert lst == [4, 3, 2, 1, 5]
    lst = [1, 2, 3, 4, 5]
    reverse_list(lst, 0, 0)
    assert lst == [1, 2, 3, 4, 5]
    lst = [1, 2, 3, 4, 5]
    reverse_list(lst, 1, 3)
    assert lst == [1, 4, 3, 2, 5]
    lst = [1, 2, 3, 4, 5]
    reverse_list(lst, 1, 2)
    assert lst == [1, 3, 2, 4, 5]
