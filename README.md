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



