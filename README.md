# NeuroVM - AI Driven Predictive Thrashing Detection and Dynamic Virtual Memory Optimization

## Overview

NeuroVM is an AI-based operating system simulation that integrates machine learning with virtual memory management to predict and prevent memory thrashing in real time.

The system simulates operating system behavior under load and uses an AI model to dynamically optimize memory allocation and page replacement strategies.

It combines concepts from operating systems, machine learning, and real-time system monitoring.

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

The system consists of the following components:

1. Memory Simulator
   - Simulates page requests
   - Implements page replacement algorithms such as LRU, FIFO, and RANDOM

2. Feature Extraction
   - Page fault rate
   - CPU utilization
   - Working set size

3. AI Prediction Engine
   - Uses Random Forest Classifier
   - Classifies system state into NORMAL, WARNING, or SEVERE THRASHING

4. Optimization Engine
   - Adjusts memory frames dynamically based on AI prediction
   - Prevents system instability

5. Visualization Layer
   - Real-time dashboard
   - Graphs and heatmaps
   - System logs

---

## Machine Learning Model

A Random Forest Classifier is trained using synthetic operating system data.

Input features:
- Page fault rate
- CPU utilization
- Working set size

Output classes:
- 0: NORMAL
- 1: WARNING
- 2: SEVERE THRASHING

---

## Workflow

Page Request → Memory Simulator → Feature Calculation → AI Prediction → Optimization Engine → Algorithm Switching → Dashboard Update

---

## Features

- Real-time memory simulation
- AI-based thrashing prediction
- Dynamic memory optimization
- Automatic algorithm switching (LRU, FIFO)
- CPU and RAM monitoring
- Memory pressure analysis
- Performance graphs and heatmaps
- Terminal-style system logs

---

## Visual Components

- CPU usage monitor
- RAM usage monitor
- System health indicator
- AI risk prediction panel
- Memory block visualization
- Performance graphs
- Heatmap visualization
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

## How to Run

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Open Jupyter Notebook

jupyter notebook

Step 3: Run the project

Open NeuroVM.ipynb and execute all cells

---

## requirements.txt

numpy
pandas
matplotlib
seaborn
scikit-learn
plotly
psutil
ipython

---

## Project Highlights

- Real operating system memory simulation
- AI-based predictive system behavior analysis
- Dynamic resource optimization
- Real-time visualization dashboard
- Integration of OS concepts with machine learning

---

## Real World Applications

This project is relevant to:

- Operating system design
- Cloud resource management
- System performance optimization
- AI-based infrastructure monitoring

---

## Conclusion

NeuroVM demonstrates how artificial intelligence can enhance operating system design by predicting system failures and optimizing memory management dynamically.

It provides a simulation of an intelligent operating system capable of adapting its behavior based on system load conditions.

---

## Author

NeuroVM AI Project
