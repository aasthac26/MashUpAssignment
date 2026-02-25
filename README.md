# Topsis-Aastha-102316009

Python package for TOPSIS ranking.

Install:
pip install Topsis-Aastha-102316009

Run:
topsis data.csv 1,1,1 +,+,+ result.csv

Link:
https://pypi.org/project/Topsis-Aastha-102316009/

# TOPSIS-Based Selection of Best Pre-trained Conversational Model
Objective

The objective of this project is to apply the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method to identify the best pre-trained conversational model based on multiple evaluation criteria.

The implementation was performed in a Kaggle notebook using Python.

Alternatives (Conversational Models Evaluated)

DialoGPT

BlenderBot

T5 (Dialogue fine-tuned)

BERT (Retrieval-based conversational setup)

GPT-2 (Chat fine-tuned)

Evaluation Criteria
Code	Criterion	Type
C1	BLEU Score	Benefit ↑
C2	ROUGE Score	Benefit ↑
C3	Inference Time	Cost ↓
C4	Model Size	Cost ↓
C5	Perplexity	Cost ↓

Benefit criteria are maximized, while cost criteria are minimized.

Weights Used
Criterion	Weight
BLEU	0.30
ROUGE	0.15
Time	0.15
Size	0.15
Perplexity	0.25

Higher importance was given to BLEU and Perplexity as they directly affect conversational response quality.

Methodology – TOPSIS Implementation
Step 1 – Decision Matrix

A decision matrix was constructed containing performance values of each model for all five criteria.

Step 2 – Normalization

Vector normalization was applied to remove scale differences:​
​
Step 3 – Weighted Normalized Matrix

Each normalized value was multiplied by its respective weight:

​
​

Step 4 – Ideal Best and Ideal Worst

Ideal Best (A⁺)

Maximum for BLEU and ROUGE

Minimum for Time, Size, Perplexity

Ideal Worst (A⁻)

Minimum for BLEU and ROUGE

Maximum for Time, Size, Perplexity

Step 5 – Distance Calculation



Step 6 – TOPSIS Score
​

​


Higher score ⇒ closer to ideal solution ⇒ better model.

Result Table
Model	TOPSIS Score	Rank
BlenderBot	0.724136	1
DialoGPT	0.671138	2
GPT-2	0.622072	3
BERT	0.526934	4
T5	0.407827	5

 Result Graph

The bar graph represents the TOPSIS score of each conversational model in the original dataset order.

Observations:

BlenderBot achieved the highest score, indicating the closest proximity to the ideal solution.

DialoGPT and GPT-2 showed strong balanced performance.

BERT ranked lower because it is primarily a retrieval-based model rather than a generative conversational model.

T5 received the lowest score due to higher model size and inference time.

Final Conclusion

Based on the TOPSIS analysis:

BlenderBot is the best pre-trained conversational model
because it provides:

Highest conversational quality (BLEU & ROUGE)

Low perplexity

Acceptable computational cost

Thus, it has the highest closeness coefficient and is the optimal choice among the evaluated alternatives.
