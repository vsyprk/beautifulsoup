# Milestone-4

For Milestone 4, I updated the `BeautifulSoup` class in `bs4/__init__.py` so that a `soup` object can be iterated over directly in a `for` loop (`for node in soup:`), yielding every node in the parse tree one at a time in depth-first pre-order.

Instead of collecting all nodes into a list or using recursion, I implemented `__iter__` as a generator that walks the existing `.next_element` pointers:

```python
def __iter__(self) -> Iterator[PageElement]:
    current: Optional[PageElement] = self.next_element
    while current is not None:
        next_node: Optional[PageElement] = current.next_element
        yield current
        current = next_node