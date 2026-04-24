import random
import pandas as pd

rows = []

for _ in range(1000):
    page_fault_rate = random.uniform(0, 1)
    cpu_util = random.uniform(0, 1)
    working_set = random.uniform(0, 1)

    if page_fault_rate > 0.7:
        label = 2
    elif page_fault_rate > 0.4:
        label = 1
    else:
        label = 0

    rows.append([page_fault_rate, cpu_util, working_set, label])


df = pd.DataFrame(rows, columns=[
    "page_fault_rate",
    "cpu_util",
    "working_set",
    "label"
])


df.to_csv("thrashing_dataset.csv", index=False)
print("Dataset generated")