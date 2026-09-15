import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Архиватор Хаффмана")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--compress", action="store_true", help="сжатие текста")
    group.add_argument("-d", "--decompress", action="store_true", help="распоковка текста")
    
    parser.add_argument("input", help="входной файл")
    parser.add_argument("output", nargs="?", default=None, help="выходной файл")
    
    return parser