from __future__ import annotations
import sys
from cli import build_parser
from collections import Counter, deque
import heapq
import json
import os



class TreeNode:
    def __init__(self, val: int | None, count: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.count < other.count




def read_data(input_file: str) -> Counter:
    freq = Counter()
    with open(input_file, "rb") as f:
        while chunk := f.read(262144): # 256 KiB
            freq.update(chunk)
        return freq


def make_leaf(raw_bytes: int, count: int) -> TreeNode:
    return TreeNode(val=raw_bytes, count=count)

def make_internal(left: TreeNode, right: TreeNode) -> TreeNode:
    return TreeNode(val=None, count=left.count + right.count, left=left, right=right)


def _levelOrderTraversal(root: TreeNode) -> list:
    if not root:
        return []

    res = []
    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    return res
    
    
def build_tree(heap: list[TreeNode]) -> TreeNode:
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        node = make_internal(left = left, right = right)
        heapq.heappush(heap, node)
    return heap[0]


def generate_codes(root: TreeNode) -> dict[int, str]:
    if not root.left and not root.right:
        return {root.val: "0"}
    ... # todo


def compress(input_file: str, output_file: str) -> bool:  # TODO: цель записать результат компресинга в output_file
    if os.path.getsize(input_file) == 0:
        open(output_file, "wb").close()
        return True
    
    heap = []
    freq = read_data(input_file)
        
    for raw_bytes, count in freq.items():
        heapq.heappush(heap, make_leaf(raw_bytes, count))
    
    root = build_tree(heap)
   
    codes = generate_codes(root)
    
    print(_levelOrderTraversal(root)) #для визуализации
    
    #вызываем запись
    
    return True


def decompress(input_file: str, output_file: str) -> bool: # TODO
    print(f"{input_file} распоковываем в {output_file}")
    return True

def main():
    args = build_parser().parse_args()
    
    if not os.path.isfile(args.input):
        print(f"Файла {args.input} не существует", file=sys.stderr)
        sys.exit(1)
    
    if args.output is None:
        output = "output.bin" if args.compress else "output.txt" # если мы compressing file то он становится бинарный
    else:
        output = args.output
    
    ok = compress(args.input, output) if args.compress else decompress(args.input, output)
    if not ok:
        sys.exit(1)
    

if __name__ == "__main__":
    main()