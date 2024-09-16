import json

def test_main():
    main()

def main():
    print(args2.foo*2)

def arg_parser2() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description='Example 2')
	parser.add_argument('--foo', type=float)
	return parser.parse_args()

if __name__ == '__main__':
    sys.argv = ['bezPy08_argparse.py', '--foo=3.1']
    args2 = arg_parser2()
    main()

