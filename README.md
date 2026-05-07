# NeuroVM - AI Driven Predictive Thrashing Detection and Dynamic Virtual Memory Optimization

## Overview

NeuroVM is an AI-based operating system simulation that integrates machine learning with virtual memory management to predict and prevent memory thrashing in real time.

The system simulates operating system behavior under load and uses an AI model to dynamically optimize memory allocation and page replacement strategies.

It combines concepts from operating systems, machine learning, and real-time system monitoring.

---

## How to Run

### Step 1: Install Required Libraries

Open terminal or command prompt in your project folder and run:

pip install -r requirements.txt

---

### Step 2: Open Jupyter Notebook

Run the following command:

jupyter notebook

This will open a browser window.

---

### Step 3: Run the Project

Open the file:

NeuroVM.ipynb

Then click:

Run → Run All Cells

The dashboard will start executing step by step.

---

## Objective

The objective of this project is to:

- Predict memory thrashing before it occurs
- Detect system overload conditions early
- Dynamically optimize memory frame allocation
- Automatically switch page replacement algorithms
- Provide real-time visualization of system performance

---

## System Architecture

1. Memory Simulator
   - Simulates page requests
   - Implements page replacement algorithms (LRU, FIFO, RANDOM)

2. Feature Extraction
   - Page fault rate
   - CPU utilization
   - Working set size

3. AI Prediction Engine
   - Random Forest Classifier
   - Classifies system state into:
     - NORMAL
     - WARNING
     - SEVERE THRASHING

4. Optimization Engine
   - Adjusts memory frames dynamically
   - Prevents system instability

5. Visualization Layer
   - Live dashboard
   - Performance graphs
   - Heatmaps
   - System logs

---

## Machine Learning Model

A Random Forest Classifier is trained using synthetic operating system data.

### Input Features:
- Page fault rate
- CPU utilization
- Working set size

### Output Classes:
- 0 → NORMAL
- 1 → WARNING
- 2 → SEVERE THRASHING

---

## Features

- Real-time memory simulation
- AI-based thrashing prediction
- Dynamic memory optimization
- Algorithm switching (LRU / FIFO)
- CPU and RAM monitoring
- Memory pressure visualization
- Performance graphs
- AI terminal logs

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- psutil
- Jupyter Notebook

---

## Workflow

Page Request → Memory Simulator → Feature Extraction → AI Prediction → Optimization Engine → Algorithm Switching → Dashboard Update

---

## Conclusion

NeuroVM demonstrates how artificial intelligence can enhance operating system design by predicting system failures and optimizing memory management dynamically.

It simulates a smart operating system capable of adapting to workload conditions in real time.

---

## Author

Nispand
