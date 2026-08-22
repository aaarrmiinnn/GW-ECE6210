# Fall 2026 course plan

## Design principles

1. The course remains a machine learning course.
2. The primary audience is MS Electrical Engineering students.
3. Each lecture has no more than three main learning objectives.
4. Each lecture uses one main engineering example.
5. Hardware appears as an implementation constraint.
6. VLSI, HDL, and processor design are outside the course scope.
7. Repeated definitions and demonstrations are moved to appendices.
8. Each deck is tested before presentation.

## Lecture sequence

### Lecture 1: Machine learning for electrical engineers

- Define machine learning using engineering measurements.
- Distinguish supervised, unsupervised, and reinforcement learning.
- Introduce computation, memory, latency, and numerical precision.
- Main example: sensor calibration.

### Lecture 2: Data, models, objectives, and optimization

- Define datasets, features, targets, and data splits.
- Introduce model class, objective function, and optimizer.
- Discuss sampling, normalization, and leakage.
- Main example: multichannel measurements.

### Lecture 3: Linear regression and least squares

- Derive least squares and gradient descent.
- Discuss conditioning and regularization.
- Compare closed-form and iterative computation.
- Main example: parameter estimation or system identification.

### Lecture 4: Classification and logistic regression

- Define binary and multiclass classification.
- Derive logistic regression from conditional likelihood.
- Interpret decision thresholds.
- Main example: fault or event detection.

### Lecture 5: Generalization, regularization, and evaluation

- Explain bias, variance, and model capacity.
- Use validation data and cross-validation.
- Select metrics for engineering costs.
- Main example: missed detection and false alarm.

### Lecture 6: Probabilistic classification and uncertainty

- Apply Bayes' rule to classification.
- Introduce Gaussian class models.
- Interpret posterior probabilities and uncertainty.
- Main example: classification under measurement noise.

### Lecture 7: PCA and clustering

- Derive PCA using covariance and eigenvectors.
- Apply K-means to unlabeled measurements.
- Introduce GMM and EM as optional advanced material.
- Main example: operating regimes in sensor data.

### Lecture 8: Neural networks and backpropagation

- Define layers and activation functions.
- Explain backpropagation using a compact derivation.
- Train a small network using NumPy.
- Main example: nonlinear signal classification.

### Lecture 9: Deep learning for one-dimensional signals

- Relate convolution to digital filtering.
- Define one-dimensional convolutional layers.
- Discuss training and evaluation of a compact CNN.
- Main example: waveform, vibration, or audio classification.

### Lecture 10: Trees, ensembles, and model comparison

- Explain decision trees and ensemble averaging.
- Compare linear, tree-based, and neural models.
- Include latency, memory, and interpretability in model selection.
- Main example: complete engineering model comparison.

## Hardware-aware content

Hardware content is limited and distributed across the course.

| Topic | Hardware-aware question |
|---|---|
| Linear regression | Is a matrix inverse necessary? What memory is required? |
| Regularization | Can sparsity reduce storage and computation? |
| PCA | Can fewer features reduce sensing, storage, or transmission cost? |
| Neural networks | What operations dominate inference? |
| Convolution | How does a learned filter differ from a fixed digital filter? |
| Model evaluation | What are the latency, memory, and precision requirements? |
| Final comparison | Which model satisfies the engineering constraints? |

## Deck size

Each online deck should contain:

- 30 to 45 presented cells
- One main derivation
- One main code demonstration
- One short student activity
- One summary slide
- Optional appendix cells marked as skipped in RISE

## Deck validation

Each deck must pass the following checks:

1. The notebook is valid JSON.
2. Every cell has valid RISE slide metadata.
3. Python code parses after notebook magic commands are excluded.
4. Local image references exist.
5. Stored outputs contain no execution error.
6. The notebook executes in a clean course environment.
7. The notebook exports to Reveal.js slides.
8. The title, equations, plots, and code are visually inspected.
9. No slide contains an em dash.
10. Text is short, direct, and academic.
