from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_fizz_buzz_tree(rng):

    def get_fizz_buzz_val(val):
        if not (val%3 or val%5):
            return "fizzbuzz"
        if not val%3:
            return "fizz"
        if not val%5:
            return "buzz"
        return val

    def helper(root, idx):
        if idx < len(rng):
            root = Node(get_fizz_buzz_val(rng[idx]))
            root.left = helper(root.left, idx*2+1)
            root.right = helper(root.right, idx*2+2)
        return root

    root = None
    return helper(root, 0)


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right) 


def print_pre_order(root):
    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)   


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)   
        print(root.val)


def print_bfs(root):
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if not node:
            continue

        print(node.val)
        dq.append(node.left)
        dq.append(node.right)


rng = range(1, 101)
root = create_fizz_buzz_tree(rng)
barrier = "#" * 20

print(f"{barrier} pre order {barrier}")
print_pre_order(root)

print(f"{barrier} in order {barrier}")
print_in_order(root)

print(f"{barrier} post order {barrier}")
print_post_order(root)

print(f"{barrier} bfs {barrier}")
print_bfs(root)
