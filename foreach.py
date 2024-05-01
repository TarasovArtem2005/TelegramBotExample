from typing import Callable


def foreach(collection: iter, action: Callable) -> None:
    for item in collection:
        action(item)

lst = [1, 2, 4, 5]
num = []
foreach(lst, lambda x: num.append(x))
print(num)
