from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

from simulator import MemorySimulator
from predictor import ThrashingPredictor
from optimizer import MemoryOptimizer

app = FastAPI(title="NeuroVM Backend")

# =========================
# ✅ CORS FIX (ROBUST)
# =========================
# This ensures React (Port 5173/5174) can always talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# CORE COMPONENTS
# =========================
simulator = MemorySimulator(frame_count=4)
predictor = ThrashingPredictor()
optimizer = MemoryOptimizer()


# =========================
# REQUEST MODEL
# =========================
class PageRequest(BaseModel):
    page: int = 0
    algorithm: str = "LRU"


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {
        "message": "NeuroVM backend running",
        "status": "active"
    }


# =========================
# MAIN ENDPOINT
# =========================
@app.post("/access")
def access_page(request: PageRequest):
    try:
        # If frontend sends 0 or no page, generate a random one for simulation
        target_page = request.page if request.page != 0 else random.randint(1, 15)
        
        print(f"REQUEST → page={target_page}, algo={request.algorithm}")

        # 1. Simulate memory access
        result = simulator.access_page(target_page)

        # 2. System stats
        stats = simulator.stats()

        # 3. Dynamic CPU (Realistic calculation)
        hit_ratio = stats.get("hit_ratio", 0)
        cpu_utilization = min(0.98, hit_ratio + 0.2)

        # 4. AI prediction
        # Safety: Ensure no division by zero
        current_frame_total = getattr(simulator, 'frame_count', 4)
        prediction = predictor.predict(
            page_fault_rate=stats.get("fault_ratio", 0),
            cpu_utilization=cpu_utilization,
            working_set_size=len(getattr(simulator, 'frames', [])) / max(current_frame_total, 1),
        )

        # 5. Optimization
        optimization = optimizer.optimize(simulator, prediction)

        response = {
            "memory_event": result,
            "stats": stats,
            "prediction": prediction,
            "optimization": optimization,
        }

        return response

    except Exception as e:
        print("!!! BACKEND CRASH PREVENTED !!! Error:", str(e))
        # This "Safe Return" prevents the React White Screen
        return {
            "memory_event": {"page": 0, "status": "ERROR", "frames": [0,0,0,0], "faults": 0, "hits": 0},
            "stats": {"hit_ratio": 0, "fault_ratio": 0, "total_requests": 0},
            "prediction": {"state": "BACKEND_ERROR", "risk": 0.99},
            "optimization": {"new_frame_count": 4, "action": f"Fixing: {str(e)[:30]}"},
        }

# Cleared the junk text from the end of the file.