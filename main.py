from utils import getTime, visualisation, getCPU

def main():
    upper_bound = int(input("Please Enter Upper Bound of the Prime Numbers: "))

    logical_cores = getCPU.get_logical_cores()
    print(f"Number of Logical Processors Present in the System: [{logical_cores}]")

    x: list[int] = []
    y: list[float] = []

    for i in range(1, logical_cores+1):
        time_taken:float = getTime.get_runtime(upper_bound, i)
        x.append(i)
        y.append(time_taken)
        print(f"Cores: [{i}], Time Taken: [{time_taken:.6f}s]")

    min_index = y.index(min(y))
    print(f"Minimum Time taken using [{x[min_index]}] Cores, Time: [{y[min_index]}s]")
    visualisation.plot_graph(x, y, upper_bound, min_index)

if __name__=="__main__":
    main()