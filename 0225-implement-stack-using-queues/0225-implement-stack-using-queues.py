from queue import Queue
class MyStack:

    def __init__(self):
        self.q_a = Queue(maxsize=100)
        self.q_b = Queue(maxsize=100)

    def push(self, x: int) -> None:
        self.q_a.put(x)
        while not self.q_b.empty():
            self.q_a.put(self.q_b.get())
        self.q_a, self.q_b = self.q_b, self.q_a

    def pop(self) -> int:
        return self.q_b.get()

    def top(self) -> int:
        return self.q_b.queue[0]

    def empty(self) -> bool:
        return self.q_b.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()