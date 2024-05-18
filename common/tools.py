import sys


def get_opts(name):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name)+1]


if __name__ == '__main__':
    # 可返回命令行的参数
    res = sys.argv
    print(res)