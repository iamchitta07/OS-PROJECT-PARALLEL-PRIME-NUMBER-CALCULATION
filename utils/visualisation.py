import matplotlib.pyplot as plt

def plot_graph(x_values: list[int], y_values: list[float], upper_bound: str, index: int):
    plt.figure(figsize=(14, 6))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='red', label='Performane Line')
    plt.plot(x_values[index], y_values[index], 'ro', label=f'Optimal: {y_values[index]:.6f}s, Cores: {x_values[index]}')

    # 5. Add descriptive labels and title
    plt.xticks(x_values)
    plt.xlabel('X - Logical Cores')
    plt.ylabel('Y - Time Taken (s)')
    plt.title(f"Visualization of Cores Vs. Time,\nCalculation of Prime Numbers in the Range [1, {upper_bound}]")

    # 6. Add a grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 7. Save and display
    plt.savefig('./outputs/line_chart.png')