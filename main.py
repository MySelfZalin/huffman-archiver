from cli import build_parser
from collections import Counter
import heapq
import json



# class TreeNode:
#     def __init__(self, left, right, count, freq):
#         self.left = left
#         self.right = right
#         self.count = count
#         self.freq = freq


# with open('input.txt', 'r', encoding='utf-8') as input_file, open('count.txt', 'w', encoding='utf-8') as freq:
#     text = input_file.read()
    
#     freq.write(
#         json.dumps(
#             dict(Counter(text))
#         )
#     )
#     print("ok")


def compress(input_file: str, output_file: str):
    print(f"{input_file} сжимаем в {output_file}")

def decompress(input_file: str, output_file: str):
    print(f"{input_file} распоковываем в {output_file}")




def main():
    args = build_parser().parse_args()
    
    if args.output is None:
        output = "output.bin" if args.compress else "output.txt" # если мы compressing file то он становится бинарный
    else:
        output = args.output
    
    if args.compress:
        compress(args.input, output)
    else:
        decompress(args.input, output)
    

if __name__ == "__main__":
    main()