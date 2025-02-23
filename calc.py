import argparse
parser = argparse.ArgumentParser(description="Evaluate a mathematical equation.")
parser.add_argument('equation', type=str, help="The equation to evaluate")
args = parser.parse_args()
eq = args.equation
try:
    print(f"{eq} is {eval(eq.replace('=', '=='))}")
except Exception as error:
    print(f"Error evaluating equation: {error}")