import datetime
import os

def log_user_data(a: list[int], b: list[float], user_name: str, total_cores: int, min_idx: int, upper_bound: int, lower_bound: int):
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M:%S - %d:%m:%Y")
    
    with open("./outputs/prime.txt", "a") as f:
        f.write(f"Logged Time: [{timestamp}], [{user_name}] has [{total_cores}] logical cores, Given Range: [{lower_bound},{upper_bound}]\n")
        
        for x, y in zip(a, b):
            f.write(f"Using [{x}] cores, Time taken: [{y:.6f}s]\n")
        f.write(f"Optimal: Using [{a[min_idx]}] cores, Minimum Time is Found: [{b[min_idx]:.6f}s]\n\n")
