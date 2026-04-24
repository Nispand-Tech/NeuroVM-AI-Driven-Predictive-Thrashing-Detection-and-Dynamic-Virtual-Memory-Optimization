import random

class MemoryOptimizer:
    def __init__(self):
        self.cooldown = 0

    def optimize(self, simulator, prediction, current_algo="LRU"):

        action = "System Stable"
        recommended_algo = current_algo
        risk = prediction["risk"]

        # 🔴 Severe thrashing → increase fast
        if prediction["state"] == "SEVERE_THRASHING":
            simulator.frame_count = min(32, simulator.frame_count + 2)
            recommended_algo = "LRU"
            action = "🔥 CRITICAL: Scaling RAM"

        # 🟡 Warning → increase slowly
        elif prediction["state"] == "WARNING":
            simulator.frame_count = min(32, simulator.frame_count + 1)
            action = "⚠️ PREEMPTIVE: Increasing Frames"

        # 🟢 NORMAL → FORCE DECAY (KEY FIX)
        else:
            if simulator.frame_count > 4:

                # 🔥 ALWAYS decay slowly (not dependent on risk)
                if random.random() > 0.3:
                    simulator.frame_count -= 1
                    action = "📉 Releasing Memory"

        # 🔥 HARD RESET IF STUCK AT MAX
        if simulator.frame_count >= 30 and random.random() > 0.7:
            simulator.frame_count -= random.randint(2, 4)
            action = "🔄 Rebalancing System (Anti-Stuck)"

        return {
            "new_frame_count": simulator.frame_count,
            "recommended_algorithm": recommended_algo,
            "action": action
        }