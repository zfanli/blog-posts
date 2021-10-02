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

### 实现一个简单的队列

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

这个队列只能告诉你队列先进先出的特性，如果真的要拿去使用，在不释放元素的情况下个实现会造成极大的内存空间浪费，这在内存空间有限的情况下是不可接受的。

队列的空间在某些场景下是有限的，当队列满了，也就不能再去接受新的元素入列，如果有元素出列，让队列不再处于满的状态时才能继续让新的元素入列。

### 循环队列 Circular Queue

上面例子中我们为了熟悉队列的特性写了一个简单但是低效的队列实现。循环队列是一个更加高效的队列，我们使用一个固定尺寸的数组储存元素，以及 2 个指针来标志队列的头和尾。这样做的目的在于重复使用内存空间。

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = self.rear = -1
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear += 1
            self.rear %= self.max

        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
            self.front %= self.max
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.max == self.front
```

### Queue: Built-in API

很多语言都有内置的队列数据结构，我们不需要重复造轮子。

```java
public class Main {
    public static void main(String[] args) {
        // 1. Initialize a queue.
        Queue<Integer> q = new LinkedList();
        // 2. Get the first element - return null if queue is empty.
        System.out.println("The first element is: " + q.peek());
        // 3. Push new element.
        q.offer(5);
        q.offer(13);
        q.offer(8);
        q.offer(6);
        // 4. Pop an element.
        q.poll();
        // 5. Get the first element.
        System.out.println("The first element is: " + q.peek());
        // 7. Get the size of the queue.
        System.out.println("The size is: " + q.size());
    }
}
```

```python
if __name__ == "__main__":
    q = collections.deque()
    print("After init, is the queue empty?", len(q) == 0)
    q.append(0)
    print("0 is enqueued, is the queue empty?", len(q) == 0)
    print("Peek the front of the queue:", q[0])
    q.append(1)
    q.append(2)
    print("1 and 2 are enqueued, is the queue empty?", len(q) == 0)
    print("Try to perform dequeue, result:", q.popleft())
    print("Let's peek the front now:", q[0])
    print("Try to perform dequeue, result:", q.popleft())
    print("Let's peek the front now:", q[0])
    print("Try to perform dequeue, result:", q.popleft())
    print("All the 3 elements are dequeued, is the queue empty?", len(q) == 0)
    print("Can we perform dequeue anymore?", len(q) != 0)
```

### Queue 和 BFS

BFS 的普遍使用场景是遍历树或图，和寻找根节点到目标节点的最短路径。而很多 BFS 算法都会使用队列数据结构实现。

#### BFS 代码模版：寻找最短路径

```python
def bfs(root, target):
    q = collections.deque([root])
    step = 0
    while q:
        step += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node == target:
                return step
            for n in node.neighbors:
                q.append(n)
    return -1
```

队列可以帮助 BFS 算法完成类似树的层序遍历的方式去遍历目标数据。上面的代码模板中：

1. 当队列 `q` 中存在元素时，进行下一轮遍历；
   - 在这轮遍历中我们对当前 `q` 的长度的元素进行处理，依次将其取出与目标对比；
   - 如果遇到目标则返回步数；
   - 否则将当前节点的所有相邻节点放入队列 `q`；
2. 我们用一个变量 `step` 保存目前处理的步数，在每次进入循环时更新步数。

这个代码模版主要适用于树结构，子节点之间不存在相同子节点。

### BFS 代码模版：重复节点只遍历一次

在遍历图的时候，每个节点的相邻节点可能是已经遍历过的节点，使用上面的代码将会进入无限循环，此时记录访问过的节点非常重要。我们可以通过一个 Hash 表来记录哪些节点已经被访问过。下面代码模版在上面的例子中添加了对重复节点的控制，使其可以对图进行遍历。

```python
def bfs(root, target):
    q = collections.deque([root])
    visited = set([root])
    step = 0
    while q:
        step += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node == target:
                return step
            for n in node.neighbors:
                if n not in visited:
                    q.append(n)
                    visited.add(n)
    return -1
```

## Stack: Last In First Out

后进先出的栈结构中，我们**先处理最后被添加进来的元素**。栈有入栈和出栈两个操作，入栈时将元素添加到栈顶，出栈时移出栈顶的元素。

| Term | Explanation |
| ---- | ----------- |
| push | 入栈        |
| pop  | 出栈        |

> 栈的实现比较简单，并且每种语言都有原生实现，所以略过实现代码。

### Stack 和 DFS

大多数情况如果可以使用 BFS 解决一个问题，那么同样也能用 DFS 来解决这个问题。这两种方法的最重要的区别在于**遍历的顺序**。

不同于 BFS 的顺序，应用 DFS 时，你最先访问的节点可能并非距离根节点最近的节点。换句话说，你遍历完的第一条路径也许并非最短路径。

#### DFS 代码模版：递归

递归方式不会显式使用栈的数据结构，但是还是会隐式的使用**调用栈**来完成递归的过程。下面是一个递归 DFS 的模版，用来查找目标节点是否存在于所有节点之中。

```python
def dfs(node: Node, target: Node, visited: List[Node]) -> bool:
    if node == target: return True
    for n in node.neighbors:
        if n not in visited:
            visited.append(n)
            if dfs(n, target, visited):
                return True
    return False
```

## Reference

- [[LeetCode] Introduction to Data Structure - Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/)
