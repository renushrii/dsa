class stack:
    def __init__(self):
        self.list = []
    
    def push(self, e):
        self.list.append(e)

    def pop(self):
        return self.list.pop(-1)


s = stack()

s.push(11)
s.push(23)

print(s.pop())
s.push(69)
print(s.pop())
print("love you poga :)")
