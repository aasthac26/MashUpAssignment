import sys
from .topsis import run_topsis

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis input.csv weights impacts output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    run_topsis(input_file, weights, impacts, output_file)

if __name__ == "__main__":
    main()
