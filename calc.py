import argparse
parser = argparse.ArgumentParser(description="""
Evaluate a mathematical equation.
Operators: +, -, *, /, ^, %, //, =
Functions, use [] for parameters:
abs, round, pow, max, min, sum, sqrt, log, log10, log2, exp, sin, cos, tan,
asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, tau, inf, nan""")
parser.add_argument('equation', type=str, help="The equation to evaluate")
args = parser.parse_args()
prnt_eq = args.equation
eval_eq = (prnt_eq
    .replace('=', '==')
    .replace('^', '**')
    .replace('[', '(').replace(']',')')
    )
try:
    print(f"{prnt_eq} is {eval(eval_eq)}")
except Exception as error:
    print(f"Error evaluating equation: {error}")