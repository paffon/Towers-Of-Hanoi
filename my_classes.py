import numpy as np
from time import sleep


class Rod:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.stack = []
        self.size = 0

    def push(self, element):
        if self.size < self.height:
            self.stack.append(element)
            self.size += 1
        else:
            print("ERROR: Trying to push {} onto a full rod ({})".format(element, self.name))
            exit(1)

    def pop(self):
        if self.size > 0:
            element = self.stack.pop()
            self.size -= 1
            return element
        else:
            print("ERROR: Trying to pop an empty rod ({})".format(self.name))
            exit(1)

    def peek(self):
        return self.stack[-1]

    def to_array(self):
        stack = self.stack
        size = len(stack)
        height = self.height

        res = np.asarray(stack)

        i = 0
        while i < height - size + 1:  # Adds 0's until one more than max possible height
            res = np.concatenate((res, [0]))
            i += 1
        return np.asarray(res).astype(int)


step = 1


class Board:
    def __init__(self, rings, name1="A", name2="B", name3="C"):
        global step
        step = 1
        self.rings = rings
        self.rod1 = Rod(name1, rings)
        self.rod2 = Rod(name2, rings)
        self.rod3 = Rod(name3, rings)
        self.display = []
        for i in range(self.rings, 0, -1):
            self.rod1.push(i)
        self.update_display()
        self.show_me()

    def update_display(self):
        arr1 = self.rod1.to_array()
        arr2 = self.rod2.to_array()
        arr3 = self.rod3.to_array()
        self.display = [arr1, arr2, arr3]

    def move(self, origin_rod, destination_rod):
        global step
        print("\n{}. Move ring number {} from {} to {}".format(step, origin_rod.peek(), origin_rod.name,
                                                               destination_rod.name))
        step += 1

        element = origin_rod.pop()
        destination_rod.push(element)
        self.update_display()

    def solve_me(self):
        input("Press ENTER to start solving.")
        print("\n=====\nSolving in {} moves...".format(2 ** self.rings - 1))
        self.solve(self.rings, self.rod1, self.rod2, self.rod3)
        print("\nSolved!\n=====")

    def solve(self, n, origin, helper, destination):
        if n > 0:
            self.solve(n - 1, origin, destination, helper)
            self.move(origin, destination)
            self.show_me()
            sleep(0)
            self.solve(n - 1, helper, origin, destination)

    def show_me(self):
        res = np.asmatrix(self.display)
        print(np.rot90(res))
