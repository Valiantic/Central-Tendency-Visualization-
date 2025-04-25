import statistics
import matplotlib.pyplot as plt

def get_numbers():
    numbers = []
    count = int(input("How many numbers would you like to enter? "))
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers

def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    
    try: 
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "No unique mode found"

    if len(numbers) > 1:
       std_dev = statistics.stdev(numbers)
       variance = statistics.variance(numbers)
    else:
         std_dev = 0
         variance = 0

    return mean, median, mode, std_dev, variance

def display_statistics(mean, median, mode, std_dev, variance):
    print(f"\nMean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode:.2f}")
    
    if isinstance(mode, (int, float)):
        print(f"Mode: {mean:.2f}")
    else: 
        print(f"Mode: {mode}")
        
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Variance: {variance:.2f}")

def plot_numbers(numbers):
    print("\nChoose the type of chart:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Pie Chart")
    choice = int(input("Enter your choice (1/2/3): "))

    x = range(1, len(numbers) + 1)
    if choice == 1:
        plt.bar(x, numbers, color='skyblue')
        plt.title('Bar Chart of Entered Numbers')
    elif choice == 2:
        plt.plot(x, numbers, marker='o', color='skyblue')
        plt.title('Line Chart of Entered Numbers')
    elif choice == 3:
        colors = plt.cm.tab10.colors  # Use a colormap for multiple colors
        plt.pie(numbers, labels=[f"Number {i}" for i in x], colors=colors, autopct='%1.1f%%')
        plt.title('Pie Chart of Entered Numbers')
    else:
        print("Invalid choice. Defaulting to Bar Chart.")
        plt.bar(x, numbers, color='skyblue')
        plt.title('Bar Chart of Entered Numbers')

    plt.xlabel('Number Position')
    plt.ylabel('Value')
    plt.show()
    
def plot_central_tendency(numbers, mean, median, mode):
    plt.figure(figsize=(10, 6))
    
    x = range(1, len(numbers) + 1)  
    plt.bar(x, numbers, color='skyblue', alpha=0.7, label='Numbers')
    
    plt.axhline(y=mean, color='red', linestyle='--', label=f"Mean: {mean:.2f}")
    plt.axhline(y=median, color='green', linestyle='--', label=f'Median: {median:.2f}')
    
    if isinstance(mode, (int, float)):
        plt.axhline(y=mode, color='purple', linestyle='--', label=f'Mode: {mode:.2f}')
    
    plt.title('Data Points with Central Tendency Measures')
    plt.xlabel('Data Points')
    plt.ylabel('Value')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_dispersion(std_dev, variance):
    plt.figure(figsize=(8, 6))
    stats = ['Standard Deviation', 'Variance']  
    values = [std_dev, variance]
    plt.bar(stats, values, color=['coral', 'lightgreen'])
    
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, f"{v:.2f}", ha='center')
        
    plt.title('Dispersion Measures')
    plt.tight_layout()
    plt.show()

def plot_statistics(numbers, mean, median, mode, std_dev, variance):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    
    x = range(1, len(numbers) + 1)  
    plt.bar(x, numbers, color='skyblue', alpha=0.7, label='Numbers')
    
    plt.axhline(y=mean, color='red', linestyle='--', label=f"Mean: {mean:.2f}")
    
    plt.axhline(y=median, color='green', linestyle='--', label=f'Median: {median:.2f}')
    
    plt.axhspan(mean - std_dev, mean + std_dev, alpha=0.2, color='red', 
                label=f'Standard Deviation: {std_dev:.2f}')
    
    plt.title('Data Points with Statistics')  # Fixed the typo here (was plt.title*)
    plt.xlabel('Data Points')
    plt.ylabel('Value')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    stats = ['Standard Deviation', 'Variance']  
    values = [std_dev, variance]
    plt.bar(stats, values, color=['coral', 'lightgreen'])
    
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, f"{v:.2f}", ha='center')
        
    plt.title('Dispersion Measures')
    plt.tight_layout()
    plt.show()

def main():
    numbers = get_numbers()
    mean, median, mode, std_dev, variance = calculate_statistics(numbers)
    display_statistics(mean, median, mode, std_dev, variance)
    
    # Directly ask for visualization type for mean, median, and mode
    print("\nChoose type of graph for visualizing mean, median, and mode:")
    print("1. Bar Chart")
    print("2. Line Chart") 
    print("3. Combined Chart")
    viz_type = int(input("Enter your choice (1/2/3): "))
    
    # Visualize central tendency
    plot_central_tendency(numbers, mean, median, mode)
    
    # Ask about visualizing standard deviation and variance
    print("\nWould you like to visualize standard deviation and variance?")
    dispersion_choice = input("Enter (y/n): ").lower()
    
    if dispersion_choice == 'y' or dispersion_choice == 'yes':
        plot_dispersion(std_dev, variance)

if __name__ == "__main__":
    main()
