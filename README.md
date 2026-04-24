# NeuroVM: AI-Based Thrashing Detection and Optimization

##  Overview

NeuroVM is an AI-powered virtual memory management system that predicts and prevents thrashing using Machine Learning techniques.

Traditional operating systems detect thrashing only after performance drops. This system predicts it early and dynamically optimizes memory allocation.

---

##  Features

* Virtual Memory Simulation (LRU)
* AI-based Thrashing Prediction
* Dynamic Frame Optimization
* Real-time Web Dashboard
* Performance Analytics (Hits vs Faults)

---

## Machine Learning Used

* Model: Random Forest Classifier

* Features:

  * Page Fault Rate
  * CPU Utilization
  * Working Set Size

* Output:

  * NORMAL
  * WARNING
  * SEVERE THRASHING

---

##  Tech Stack

* Backend: FastAPI, Python
* Frontend: React (Vite), Tailwind CSS
* ML: Scikit-learn, Pandas, NumPy

---

##  How to Run

### **Step 0: Clone Project**

```bash
git clone https://github.com/Nispand-Tech/NeuroVM-AI-Driven-Predictive-Thrashing-Detection-and-Dynamic-Virtual-Memory-Optimization.git
cd NeuroVM-AI-Driven-Predictive-Thrashing-Detection-and-Dynamic-Virtual-Memory-Optimization
```

---

### **Step 1: Backend**

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

---

### **Step 2: Frontend**

```bash
cd frontend
npm install
npm run dev
```

---

##  Access

* Backend API Docs:
  http://127.0.0.1:8000/docs

* Frontend Dashboard:
  http://localhost:5173 *(or port shown in terminal)*

---

##  Results

* Reduced Page Faults
* Improved Hit Ratio
* Early Thrashing Detection
* Dynamic Optimization

---

##  Conclusion
NeuroVM transforms virtual memory management into a predictive system using AI. It prevents performance degradation and improves efficiency compared to traditional algorithms.

---

##  Author

**Nispand**
Department of Computer Science
Chandigarh College of Engineering and Technology

GitHub:
https://github.com/Nispand-Tech/NeuroVM-AI-Driven-Predictive-Thrashing-Detection-and-Dynamic-Virtual-Memory-Optimization
