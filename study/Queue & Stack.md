---
title: Queue & Stack
tags:
  - Queue
  - Stack
---

虽然对于数组来说，我们可以通过下标访问**任意位置的元素**，但某些情况下我们希望能**限制处理顺序**。这篇文章介绍两个闲置处理顺序的线性结构。

- `Queue`，**先进先出**的队列；
- `Stack`，**后进先出**的栈。

<!-- more -->

## Queue: First In First Out

队列是先进先出的数据结构，先进入队列的数据将先处理。队列有 2 个操作，一个是 `Enqueue` 表示将元素加入队列，另一个是 `Dequeue` 表示将元素移出队列。

在队列数据结构中，入列的元素只能添加在队列结尾（**back/tail**）的位置，出列的元素只能从队列开始（**front/head**）的位置。

| Term    | Explanation |
| ------- | ----------- |
| Dequeue | 出列        |
| Enqueue | 入列        |

### 实现一个简单

我们可以用数组来实现一个队列数据结构，下面是一个 Python 的例子，实现了一个简单的队列。

```python
class Queue:
    def __init__(self) -> None:
        self.data = []
        self.front_index = 0

    def isempty(self) -> bool:
        if self.front_index >= len(self.data):
            return True
        return False

    def enqueue(self, x: int) -> bool:
        self.data.append(x)
        return True

    def dequeue(self) -> bool:
        if self.isempty():
            return False
        self.front_index += 1
        return True

    def front(self) -> int:
        return self.data[self.front_index]


if __name__ == "__main__":
    q = Queue()
    print("After init, is the queue empty?", q.isempty())
    q.enqueue(0)
    print("0 is enqueued, is the queue empty?", q.isempty())
    print("Peek the front of the queue:", q.front())
    q.enqueue(1)
    q.enqueue(2)
    print("1 and 2 are enqueued, is the queue empty?", q.isempty())
    print("Try to perform dequeue, result:", q.dequeue())
    print("Let's peek the front now:", q.front())
    print("Try to perform dequeue, result:", q.dequeue())
    print("Let's peek the front now:", q.front())
    print("Try to perform dequeue, result:", q.dequeue())
    print("All the 3 elements are dequeued, is the queue empty?", q.isempty())
    print("Can we perform dequeue anymore?", q.dequeue())
```

## Reference

- [[LeetCode] Introduction to Data Structure - Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/)
