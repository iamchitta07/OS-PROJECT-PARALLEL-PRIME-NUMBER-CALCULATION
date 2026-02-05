# PROJECT-1: Parallel Prime Number Calculation

## Overview
This project analyzes the performance of parallel prime number calculation across different numbers of logical CPU cores. It measures execution time for computing prime numbers in a given range using multi-process parallelization and visualizes the results.

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
2. Ensure Python 3.11+ is installed
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Building C Extensions
Compile the C libraries before running the project:
```bash
gcc -shared -fPIC -o utils/libtime.so utils/getTime.c
gcc -shared -fPIC -o utils/libcpu.so utils/getCPU.c
```

## Usage
Run the main program and provide an upper bound for prime number calculation:
```bash
python main.py
```

### Example
```
Please Enter Upper Bound of the Prime Numbers: 100000
Number of Logical Processors Present in the System: [8]
Cores: [1], Time Taken: [0.012345s]
Cores: [2], Time Taken: [0.008123s]
...
Cores: [8], Time Taken: [0.005678s]
Minimum Time taken using [8] Cores, Time: [0.005678s]
```

The program will generate a performance graph at `outputs/line_chart.png`.

## How It Works
1. **CPU Detection**: Queries the system to determine the number of logical CPU cores
2. **Iterative Testing**: For each core count from 1 to N, executes the prime calculation
3. **Parallel Computation**: The C function `findPrimesInParallel` divides the range and spawns child processes
4. **Timing**: Measures wall-clock time using `CLOCK_MONOTONIC`
5. **Visualization**: Plots results with the optimal configuration highlighted

## Author
**Chittajit Nath, NIT Durgapur**
