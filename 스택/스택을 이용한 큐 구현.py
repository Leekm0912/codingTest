class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def pop(self):
        # peek를 해서 output이 없다면 만들어줌
        self.peek()
        return self.output.pop()

    def empty(self):
        return self.input == [] and self.output == []
