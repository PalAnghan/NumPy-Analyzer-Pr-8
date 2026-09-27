import numpy as np


class DataAnalytics:

    # Constructor
    def __init__(self, array):
        self.array = np.array(array)

    # Normal method
    def show_array(self):
        print("Array:")
        print(self.array)

    # Encapsulation: private method
    def __calculate_sum(self):
        return np.sum(self.array)

    # Public method using private method
    def calculate_sum(self):
        return self.__calculate_sum()

    # Class method
    @classmethod
    def from_list(cls, data):
        return cls(data)

    # Static method
    @staticmethod
    def calculate_average(array):
        return np.mean(array)
    
    import numpy as np


def data_analytics_menu():
    while True:
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Go Back")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 6:
            break

        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        # Array required for the statistical operations
        array = np.array([
            [10, 20, 30],
            [40, 50, 60]
        ])

        print("\nOriginal Array:")
        print(array)

        if choice == 1:
            result = np.sum(array)
            print("\nSum of Array:", result)

        elif choice == 2:
            result = np.mean(array)
            print("\nMean of Array:", result)

        elif choice == 3:
            result = np.median(array)
            print("\nMedian of Array:", result)

        elif choice == 4:
            result = np.std(array)
            print("\nStandard Deviation of Array:", result)

        elif choice == 5:
            result = np.var(array)
            print("\nVariance of Array:", result)


#data_analytics_menu()
