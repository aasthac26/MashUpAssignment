# Topsis-Aastha-102316009

Python package for TOPSIS ranking.

Install:
pip install Topsis-Aastha-102316009

Run:
topsis data.csv 1,1,1 +,+,+ result.csv

Link:
https://pypi.org/project/Topsis-Aastha-102316009/


# TOPSIS-Based Selection of Conversational AI Models

## Project Title
Selection of Best Pre-trained Conversational AI Model Using TOPSIS Method

---

## Introduction

In Natural Language Processing (NLP), many pre-trained models are available for conversational applications such as chatbots and virtual assistants. Each model differs in performance, size, speed, and resource usage.

Selecting the best model becomes difficult when multiple criteria must be considered. To solve this problem, the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method is used in this project.

This project applies TOPSIS to rank different conversational AI models and select the most suitable one.

---

## Objective

The main objective of this project is:

- To evaluate multiple pre-trained conversational models.
- To compare them using multiple performance criteria.
- To apply the TOPSIS method for ranking.
- To identify the best-performing model.

---

##  Selected Models (Alternatives)

The following conversational models are considered:

1. DialoGPT  
2. T5 
3. BERT
4. BlenderBot  
5. GPT-2

These models are widely used for chatbot and dialogue systems.

---

## Evaluation Criteria

Five criteria are selected for evaluation:

| Criterion           | Description                         | Type    |
| ------------------- | ----------------------------------- | ------- |
| BLEU Score          | Measures response quality           | Benefit |
| ROUGE Score         | Measures text overlap quality       | Benefit |
| Inference Time (ms) | Measures response speed             | Cost    |
| Model Size (MB)     | Storage requirement                 | Cost    |
| Perplexity          | Measures language model uncertainty | Cost    |


- Benefit Criteria: Higher value is better  
- Cost Criteria: Lower value is better

---

##  Weights Assigned

Each criterion is assigned a weight based on its importance:

| Criterion      | Weight   |
| -------------- | -------- |
| BLEU Score     | 0.30     |
| ROUGE Score    | 0.15     |
| Inference Time | 0.15     |
| Model Size     | 0.15     |
| Perplexity     | 0.25     |
| **Total**      | **1.00** |


---


##  Methodology (TOPSIS Steps)

The TOPSIS method is applied using the following steps:

### Step 1: Construct Decision Matrix
All alternatives and criteria values are arranged in tabular form.

### Step 2: Normalize the Matrix
Each value is normalized to remove scale differences using vector normalization.

### Step 3: Weighted Normalized Matrix
Normalized values are multiplied by their respective weights.

### Step 4: Determine Ideal Solutions
- Positive Ideal Solution (Best)
- Negative Ideal Solution (Worst)

These are selected based on benefit and cost criteria.

### Step 5: Calculate Separation Measures
The Euclidean distance of each alternative from the ideal best and ideal worst is calculated.

### Step 6: Calculate Performance Score
The TOPSIS score is computed using:

C = D⁻ / (D⁺ + D⁻)

where:
- D⁺ = Distance from ideal best
- D⁻ = Distance from ideal worst

### Step 7: Ranking
Models are ranked based on their TOPSIS scores. Higher score means better performance.

---

## Implementation

The TOPSIS algorithm is implemented in Python using:

- NumPy
- Pandas
- Matplotlib

---

## Result Table

After execution, the result table is generated

It contains:

- Model Name
- TOPSIS Score
- Rank

Example Format:

| Model | TOPSIS Score | Rank |
|-------|--------------|------|
| BlenderBot | 0.724136 | 1 |
| DialoGPT | 0.671138 | 2 |

(The actual values may vary.)

<img width="418" height="205" alt="image" src="https://github.com/user-attachments/assets/ae2e26da-a4dd-4473-a250-9800b1eaea90" />


---

## Result Graph

A bar graph of TOPSIS scores is generated


The graph shows:

- X-axis: Models
- Y-axis: TOPSIS Score

<img width="828" height="577" alt="image" src="https://github.com/user-attachments/assets/91c6fe0e-5b4c-492c-beb6-56088a3a9b67" />



---

## Conclusion

Based on the TOPSIS analysis, the model with the highest performance score is selected as the best conversational AI model.

From the results, BlenderBot achieved the highest TOPSIS score and is therefore considered the most suitable model among the selected alternatives.

The TOPSIS method proved to be effective for multi-criteria decision-making in model selection.

# Assignment 6 Data Generation using Modelling and Simulation

1. Objective

The objective of this project is to generate synthetic data using a simulation model and evaluate the performance of multiple machine learning models on the generated dataset. The study includes:

Defining a mathematical simulation model

Generating 1000 random simulations

Training and comparing multiple ML models

Evaluating them using weighted performance metrics

2. Simulation Model

A linear system model was used for simulation:

y = a·x₁ + b·x₂ + c·x₃ + ε

Where:

x₁, x₂, x₃ are input features

a, b, c are randomly generated system parameters

ε is the noise term

y is the simulated output

This model represents a simplified stochastic physical system.

3. Parameter Bounds
   
| Parameter  | Lower Bound | Upper Bound |
| ---------- | ----------- | ----------- |
| a          | 0.5         | 2.0         |
| b          | -1.0        | 1.0         |
| c          | 0.1         | 1.5         |
| Noise      | 0           | 0.2         |
| x₁, x₂, x₃ | 0           | 10          |


4.Data Generation

Total simulations performed: 1000

Random sampling used for all parameters

Dataset created using simulator outputs

Dataset split:

80% Training

20% Testing

5. Machine Learning Models Used

The following models were trained and evaluated:

Linear Regression

Ridge Regression

Lasso Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

6. Evaluation Metrics and Weights

| Criterion       | Weight |
| --------------- | ------ |
| BLEU            | 0.30   |
| ROUGE           | 0.15   |
| Time Efficiency | 0.15   |
| Accuracy (R²)   | 0.15   |
| Satisfaction    | 0.25   |
| Total           | 1.00   |


Notes:

BLEU and ROUGE were mapped from prediction performance for comparative scoring

Time efficiency was normalized (lower training time gives higher score)

Satisfaction was considered proportional to prediction accuracy

7. Final Score Formula

Final Score = 0.30(BLEU) + 0.15(ROUGE) + 0.15(Time) + 0.15(Accuracy) + 0.25(Satisfaction)

This weighted score was used to rank all models.

8. Results

The bar graph of final scores shows the comparative performance of all models.
<img width="733" height="622" alt="image" src="https://github.com/user-attachments/assets/db249c24-8f6d-4359-969c-8dccbeddfe29" />

Best performing model: Ridge Regression

Reason:

High prediction accuracy

Robust performance on noisy simulated data

Balanced bias–variance tradeoff

9. Observations

Linear models performed best due to the linear simulation equation

Ridge Regression achieved the highest weighted score

Lasso Regression performed similarly but slightly lower than Ridge

Decision Tree showed moderate performance

Random Forest and Gradient Boosting performed poorly because the dataset lacks non-linear structure

10. Conclusion

Simulation-based data generation was used to create a synthetic linear dataset for evaluating multiple machine learning models. Linear models performed best because the underlying system follows a linear relationship. Ridge Regression achieved the highest final score, followed by Lasso and Linear Regression, while tree-based ensemble models performed poorly due to the absence of non-linear patterns. Weighted multi-metric evaluation provided a more reliable comparison, and Ridge Regression was identified as the most suitable model for this simulation.


