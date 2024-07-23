# Use agrparse to create command line tools
# see https://docs.python.org/3/howto/argparse.html
# Note 'Click' & 'Typer' are external libraries you can use for parsing arguments

import argparse     # built-in library
import sys          # for sys.argv


#  -h, --help  show this help message and exit
# try python bezpy_08_argparse.py -h
# try python bezpy_08_argparse.py --help
# try python bezpy_08_argparse.py YYY 45 -a3 VALUE -a5
# try python bezpy_08_argparse.py YYY 45
# try python bezpy_08_argparse.py -a3 VALUE -s YYY 45
# try python bezpy_08_argparse.py -a3=VALUE -s YYY 45
# try python bezpy_08_argparse.py YYY 45 -a3=VALUE -a4=2 -a5=HELLO

# sys.argv = ['bezPy08_argparse.py', '-a3', 'VALUE', '-s', 'YYY', '45', '-a5', '7']
# sys.argv = ['bezPy08_argparse.py', 'YYY', '45', '-a3', 'VALUE', '-s', '-a5', '7']  # This gives same output as above
sys.argv = ['bezPy08_argparse.py', 'YYY', '45', '-s',  '-a3=VALUE', '-a5=7']       # This gives same output as above
# using sys.argv is the easy way to retrieve the parameters


def arg_parser() -> argparse.ArgumentParser:

	parser = argparse.ArgumentParser(description='Simple Example')

	# Postitional Arguments (always required, can NOT set default value if not passed)
	parser.add_argument("first_arg", help="This is an 8-digit policy number")
	parser.add_argument("second_arg", help="2nd arg must be integer", type=int)

	# Optional Arguments . Order is not important. They take this format.
	# action="store_true" => not followed by a value
	parser.add_argument("-s", "--switch", dest='switch', help="this turns on the switch", action="store_true")  # this is a boolean - True if Present
	parser.add_argument("-a3", "--third_arg", dest='third_arg', help="third arg MUST be followed by a value")
	parser.add_argument('-a4', '--fourth_arg', dest='fourth_arg', default=1, help="fourth arg is an OPTIONAL int defaulted to 1", type=int)
	parser.add_argument('-a5', '--fifth_arg', dest='fifth_arg', default='YES', help="fifth arg is an OPTIONAL int defaulted to YES", type=str)
	return parser.parse_args()


args = arg_parser()

vars(args)  # returns dictionary of args
# {'first_arg': 'YYY',
#  'second_arg': 45,
#  'switch': True,
#  'third_arg': 'VALUE',
#  'fourth_arg': 1,
#  'fifth_arg': '7'}

print(f"args.first_arg = {args.first_arg}")     # REQUIRED FIRST ARGUMENT
print(f"args.second_arg = {args.second_arg} ")  # REQUIRED SECOND ARGUMENT FORCES TYPE INT
print(f"args.switch = {args.switch}")           # OPTIONAL SWITCH -s  OR --function;   args.switch is boolean
print(f"args.third_arg = {args.third_arg}")     # OPTIONAL SWITCH -o  OR --optional; must be followed by a value, args.optional holds that value
print(f"args.fourth_arg = {args.fourth_arg}")   # OPTIONAL Third argument defaulted to 1
print(f"args.fifth_arg = {args.fifth_arg}")     # OPTIONAL Fourth argument, string '7' is provided

# args.first_arg = 'YYY'
# args.second_arg = 45
# args.switch = True
# args.third_arg = 'VALUE'
# args.fourth_arg = 1
# args.fifth_arg = '7'


# ======================================================================================================================
# Values for 'action'
# ======================================================================================================================
# “store_true”    # argument is a boolean value True if present
# “store_false”   # argument is a boolean value False if present
# “store_const”
# “append”
# “append_const”
# “count”
# “version”
# “extend”

def arg_parser2() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(description='Example 2')
	parser.add_argument('--verbose', '-v', action='count', default=0)   			# args.verbose will return number of v's passed e.g. -vvv ->  args.verbose = 3
	parser.add_argument('--coordinates', type=float, nargs=2,)          			# accepts exactly two values for flag
	parser.add_argument('--soo', type=float, nargs='*',)          					# accepts one or more values for flag,  '*' as used in regex.
	parser.add_argument('--foo', type=float, nargs='+',)          					# accepts at least one value for flag,  '+' as used in regex.
	parser.add_argument('--boo', type=float, nargs='?', default='x', const='y') 	# accepts zero or one value for flag,   '?' as used in regex. If flag excluded default value used, if flag included without a value  then 'const' value used

	# only choices accepted
	parser.add_argument('--trading-pair', type=str, default='BTC-ETH', choices=['BTC-ETH', 'BTC-USD', 'ETH-USD', 'ADA-USD'])

args2 = arg_parser2()