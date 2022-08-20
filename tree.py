Poga = None
class Node:
    def __init__(self, data):
        self.data = data
        self.right = Poga
        self.left = Poga

    def insert(self,value):
        if self.data >= value:
            if self.left == Poga:
                self.left = Node(value)
                print(f"inserted value {value} to the left of {self.data}")

            else:
                self.left.insert(value)


        else:
            if self.right == Poga:
                self.right = Node(value)
                print(f"inserted value {value} to the right of {self.data}")
            else:
                self.right.insert(value)




tree = Node(11)
tree.insert(7)
tree.insert(23)
tree.insert(9)
tree.insert(34)
tree.insert(4)






