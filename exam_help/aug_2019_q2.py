from typing import List, Any, Dict


class Queue:
    _data: Dict[int, Any]

    def __init__(self) -> None:
        """ Initialize an empty Queue """
        self._data = {}

    def to_multiset(self) -> List[Any]:
        """ Return a copy of the values in the Queue in an arbitrary order """
        return list(self._data.values())

    def is_empty(self) -> bool:
        """ Return True if there are no values in the Queue """
        return len(self._data) == 0

    def enqueue(self, item: Any):
        # O(1)
        lst = self._data.setdefault(0, [])
        lst.append(item)

    def dequeue(self):
        # O(n)
        if 0 not in self._data:
            return None
        lst = self._data[0]
        item = lst.pop(0)
        # Update the data list again
        self._data[0] = lst
