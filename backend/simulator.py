import random

class MemorySimulator:
    def __init__(self, frame_count=4):
        self.frame_count = frame_count
        self.frames = []
        self.page_faults = 0
        self.hits = 0
        self.history = []  # track recent activity

    # =========================
    # MAIN ACCESS FUNCTION
    # =========================
    def access_page(self, page, algorithm="LRU"):

        # 🔥 occasional workload spike (adds realism)
        if random.random() > 0.9:
            page = random.randint(0, 50)

        hit = page in self.frames
        status = "HIT" if hit else "FAULT"

        if hit:
            self.hits += 1

            if algorithm == "LRU":
                # move to most recent
                self.frames.remove(page)
                self.frames.append(page)

        else:
            self.page_faults += 1

            if len(self.frames) >= self.frame_count:

                if algorithm == "FIFO":
                    self.frames.pop(0)

                elif algorithm == "LRU":
                    self.frames.pop(0)

                elif algorithm == "RANDOM":
                    self.frames.pop(random.randint(0, len(self.frames) - 1))

            self.frames.append(page)

        # 🔥 store history (for pressure + AI)
        self.history.append(status)
        if len(self.history) > 20:
            self.history.pop(0)

        # 🔥 simulate pressure drift (VERY IMPORTANT)
        self._apply_pressure_drift()

        return {
            "page": page,
            "status": status,
            "frames": self.frames.copy(),
            "faults": self.page_faults,
            "hits": self.hits,
            "frame_count": self.frame_count,
            "pressure": self.compute_pressure(),  # 🔥 new field
        }

    # =========================
    # SYSTEM STATS
    # =========================
    def stats(self):
        total = self.hits + self.page_faults

        hit_ratio = self.hits / total if total else 0
        fault_ratio = self.page_faults / total if total else 0

        return {
            "total_requests": total,
            "hits": self.hits,
            "faults": self.page_faults,
            "hit_ratio": round(hit_ratio, 3),
            "fault_ratio": round(fault_ratio, 3),
        }

    # =========================
    # PRESSURE CALCULATION (NEW)
    # =========================
    def compute_pressure(self):
        # combines faults + memory usage + randomness
        pressure = (
            (self.page_faults * 0.05) +
            (len(self.frames) / max(self.frame_count, 1)) * 0.5 +
            random.uniform(-0.05, 0.1)
        )
        return round(max(0, min(pressure, 1)), 3)

    # =========================
    # PRESSURE DRIFT (CRITICAL)
    # =========================
    def _apply_pressure_drift(self):
        # 🔥 simulate real OS instability

        if self.page_faults > 0 and self.page_faults % 10 == 0:
            # sudden load spike
            self.frame_count = min(32, self.frame_count + 1)

        if self.frame_count > 6 and random.random() > 0.8:
            # gradual release
            self.frame_count -= 1