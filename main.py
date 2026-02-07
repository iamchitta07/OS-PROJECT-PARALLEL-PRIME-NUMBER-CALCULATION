from utils import getTime, visualisation, getCPU, getUserName, logUserData

def main():
    lower_bound = int(input("Please Enter Lower Bound of the Prime Numbers: "))
    upper_bound = int(input("Please Enter Upper Bound of the Prime Numbers: "))

    logical_cores: int = getCPU.get_logical_cores()

    x: list[int] = []
    y: list[float] = []

    for i in range(1, logical_cores+1):
        time_taken:float = getTime.get_runtime(upper_bound, lower_bound, i)
        x.append(i)
        y.append(time_taken)

    min_index = y.index(min(y))
    logUserData.log_user_data(x, y, getUserName.get_user_name(), logical_cores, min_index, upper_bound, lower_bound)
    visualisation.plot_graph(x, y, lower_bound, upper_bound, min_index, getUserName.get_user_name())

if __name__=="__main__":
    main()