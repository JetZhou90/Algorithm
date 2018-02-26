class TwoStackQueue:
    stackPush = []
    stackPop = []

    def add(self, newNum):
        self.stackPush.append(newNum)

    def poll(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is empty!")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is empty!")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop[-1]