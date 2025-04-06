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
    mode = statistics.mode(numbers)
    return mean, median, mode

def display_statistics(mean, median, mode):
    print(f"\nMean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode:.2f}")

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

def main():
    numbers = get_numbers()
    mean, median, mode = calculate_statistics(numbers)
    display_statistics(mean, median, mode)
    plot_numbers(numbers)

if __name__ == "__main__":
    main()
