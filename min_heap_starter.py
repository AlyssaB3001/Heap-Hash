# min_heap_starter.py
# Minimal educational Min-Heap (array-backed)
# Implement push (sift-up), pop/extract_min (sift-down), and peek.

from typing import List

class MinHeap:
    def __init__(self):
        self._a: List[int] = []

    def __len__(self) -> int:
        return len(self._a)

    def __bool__(self) -> bool:
        return bool(self._a)

    # Index helpers (0-based)
    def _parent(self, i: int) -> int: return (i - 1) // 2
    def _left(self, i: int) -> int:   return 2 * i + 1
    def _right(self, i: int) -> int:  return 2 * i + 2

    def peek(self) -> int:
        if not self._a:
            raise IndexError("peek from empty heap")
        return self._a[0]

    def push(self, x: int) -> None:
        #TODO: append x; then sift-up while parent > x. Swap as needed.
        self._a.append(x)
        i = len(self._a) -1
        while i > 0:
            parent = self._parent(i)
            if self._a[parent] > self._a[i]:
                self._a[i], self._a[(i - 1) // 2] = self._a[(i - 1) // 2], self._a[i]
                i = parent
            else:
                break    

    def pop(self) -> int:
        """Remove and return smallest element."""
        if not self._a:
            raise IndexError("pop from empty heap")
        #TODO: store min_val (root), move last to root, and sift-down.
        root = self._a[0]
        last =self._a.pop()

        if self._a:
            self._a[0] = last
            self._sift_down(0)
        return root

    def _sift_down(self, i: int) -> None:
        n = len(self._a)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i
            if left < n and self._a[left] < self._a[smallest]:
                smallest = left
            if right < n and self._a[right] < self._a[smallest]:
                smallest = right
            if smallest == i:
                break
            self._a[i], self._a[smallest] = self._a[smallest], self._a[i]
            i = smallest


if __name__ == "__main__":
    #demo sequence
    h = MinHeap()
    for x in [7, 12, 3, 19, 5]:
        h.push(x)
    print("peek:", h.peek())  # expect 3
    out = []
    while h:
        out.append(h.pop())
    print("popped:", out)     # expect sorted order
