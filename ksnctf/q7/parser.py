import sys
from pycparser import parse_file, c_parser, c_generator, c_ast

def main():
    text = ''.join(sys.stdin.readlines()) # 読み込む

    parser = c_parser.CParser() # パーサ
    ast = parser.parse(text, filename='<none>') # パースする

    generator = c_generator.CGenerator() # 生成器
    print(generator.visit(ast)) # 単にパースしたものを書き出すだけ

if __name__ =='__main__':
    main()
