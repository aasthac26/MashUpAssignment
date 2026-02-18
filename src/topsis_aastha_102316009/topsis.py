import pandas as pd
import numpy as np
import os
import sys

def error(msg):
    raise Exception(msg)

def run_topsis(input_file, weights, impacts, output_file):

    # File check
    if not os.path.exists(input_file):
        error("File not found")

    weights = weights
    impacts = impacts

    # Read file
    try:
        if input_file.endswith(".xlsx"):
            df = pd.read_excel(input_file)
        else:
            df = pd.read_csv(input_file)
    except:
        error("Unable to read input file")

    # Minimum column check
    if df.shape[1] < 3:
        error("Input file must contain 3 or more columns")

    # Numeric validation
    try:
        data = df.iloc[:, 1:].astype(float).values
    except:
        error("From 2nd to last columns must be numeric")

    # Length check
    if len(weights) != len(impacts) or len(weights) != data.shape[1]:
        error("Weights/impacts must match number of numeric columns")

    # Impact validation
    for i in impacts:
        if i not in ['+', '-']:
            error("Impacts must be either + or -")

    weights = np.array(weights, float)

    # TOPSIS

    norm = data / np.sqrt((data**2).sum(axis=0))
    weighted = norm * weights

    best = []
    worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            best.append(weighted[:, i].max())
            worst.append(weighted[:, i].min())
        else:
            best.append(weighted[:, i].min())
            worst.append(weighted[:, i].max())

    best = np.array(best)
    worst = np.array(worst)

    s_plus = np.sqrt(((weighted - best)**2).sum(axis=1))
    s_minus = np.sqrt(((weighted - worst)**2).sum(axis=1))

    score = s_minus / (s_plus + s_minus)

    rank = score.argsort()[::-1] + 1

    df["Topsis Score"] = score
    df["Rank"] = rank

    if output_file.endswith(".xlsx"):
        df.to_excel(output_file, index=False)
    else:
        df.to_csv(output_file, index=False)

    print("✅ Result saved to:", output_file)
