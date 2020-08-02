# -*- coding:utf-8 -*-


# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。


class MinStack:
    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        top = self.data.pop()
        if self.helper and self.helper[-1] == top:
            self.helper.pop()
        return top

    def top(self):
        if self.data:
            return self.data[-1]

    def get_min(self):
        if self.helper:
            return self.helper[-1]


