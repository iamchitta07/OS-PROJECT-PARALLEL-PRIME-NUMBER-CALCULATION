# PROJECT-1: Parallel Prime Number Calculation

## Overview
This project analyzes the performance of parallel prime number calculation across different numbers of logical CPU cores. It measures execution time for computing prime numbers in a given range using multi-process parallelization and visualizes the results.

## Problem Statement
```
Write a code that accepts integer values of rl & rh and computes the list of prime numbers in that given range and stores them in a file prime.txt. You should write a code that minimizes the overall execution time by creating multiple child processes (say n) which exploit ultiple logical cores of your machine. For a given range say 1000 – 10000 provide the plot of n vs physical execution time.

Show results/plots: 
(a) for varying ranges say 1000- 10000; 50000-100000, etc. 
(b) for each range run in atleast 3 machines with different configurations (number of logical processors).
```
## Features
- **Parallel Processing**: Utilizes multiple child processes to calculate primes in parallel ranges
- **Performance Analysis**: Measures and compares execution times across 1 to N logical cores
- **Visualization**: Generates performance graphs showing core count vs. execution time
- **Optimal Core Detection**: Identifies the number of cores that provides the best performance

## Project Structure
```
.
├── main.py                 # Main entry point
├── utils/
│   ├── __init__.py
│   ├── getTime.py         # Python wrapper for time measurement
│   ├── getTime.c          # C implementation for parallel prime calculation with timing
│   ├── getCPU.py          # Python wrapper for CPU info retrieval
│   ├── getCPU.c           # C implementation to get logical CPU count
│   └── visualisation.py   # Graph plotting functionality
├── outputs/               # Directory for generated graphs
├── pyproject.toml         # Python project configuration
└── README.md             # Readme file
```

## Requirements
- Python 3.11+
- matplotlib >= 3.10.8
- ruff >= 0.15.0
- GCC compiler (for C extensions)
- Linux/Unix environment (uses `lscpu` and POSIX APIs)

## Installation
1. Clone or download the project
   ```bash
   git clone https://github.com/iamchitta07/OS-PROJECT-PARALLEL-PRIME-NUMBER-CALCULATION.git
   ```
2. Ensure Python 3.11+ is installed
3. Ensure UV is installed
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. Install dependencies:
   ```bash
   uv add -r requirements.txt
   ```

## Building C Extensions
Compile the C libraries before running the project:
```bash
gcc -shared -fPIC -o utils/libtime.so utils/getTime.c
gcc -shared -fPIC -o utils/libcpu.so utils/getCPU.c
gcc -shared -fPIC -o utils/libusername.so utils/getUserName.c
```

## Usage
Run the main program and provide an upper bound for prime number calculation:
```bash
uv run main.py
```

### Example
```
Logged Time: [20:50:44 - 07:02:2026], [chitta] has [28] logical cores, Given Range: [100,1000000]
Using [1] cores, Time taken: [0.069788s]
Using [2] cores, Time taken: [0.030623s]
Using [3] cores, Time taken: [0.024932s]
Using [4] cores, Time taken: [0.022116s]
Using [5] cores, Time taken: [0.016377s]
Using [6] cores, Time taken: [0.018643s]
Using [7] cores, Time taken: [0.016374s]
Using [8] cores, Time taken: [0.014263s]
Using [9] cores, Time taken: [0.013787s]
...
Using [28] cores, Time taken: [0.018468s]
Optimal: Using [12] cores, Minimum Time is Found: [0.012020s]
```

The program will generate a performance graph at `outputs/username_line_chart.png`. and `prime.txt` Log File.

## How It Works
1. **CPU Detection**: Queries the system to determine the number of logical CPU cores
2. **Iterative Testing**: For each core count from 1 to N, executes the prime calculation
3. **Parallel Computation**: The C function `findPrimesInParallel` divides the range and spawns child processes
4. **Timing**: Measures wall-clock time using `CLOCK_MONOTONIC`
5. **Visualization**: Plots results with the optimal configuration highlighted

