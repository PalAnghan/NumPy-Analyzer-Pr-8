import numpy as np


def mathematical_operations_menu():
    while True:
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        print("7. Go Back")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # 1. Addition
        if choice == 1:
            try:
                array1 = np.array([
                    [10, 20, 30],
                    [40, 50, 60]
                ])

                elements = input(
                    "Enter 6 elements for second array separated by space: "
                ).split()

                array2 = np.array(elements, dtype=int).reshape(2, 3)

                print("\nOriginal Array:")
                print(array1)

                print("\nSecond Array:")
                print(array2)

                result = array1 + array2

                print("\nResult of Addition:")
                print(result)

            except ValueError:
                print("Invalid input. Please enter exactly 6 integer values.")

        # 2. Subtraction
        elif choice == 2:
            try:
                array1 = np.array([
                    [10, 20, 30],
                    [40, 50, 60]
                ])

                elements = input(
                    "Enter 6 elements for second array separated by space: "
                ).split()

                array2 = np.array(elements, dtype=int).reshape(2, 3)

                print("\nOriginal Array:")
                print(array1)

                print("\nSecond Array:")
                print(array2)

                result = array1 - array2

                print("\nResult of Subtraction:")
                print(result)

            except ValueError:
                print("Invalid input. Please enter exactly 6 integer values.")

        # 3. Multiplication
        elif choice == 3:
            try:
                array1 = np.array([
                    [10, 20, 30],
                    [40, 50, 60]
                ])

                elements = input(
                    "Enter 6 elements for second array separated by space: "
                ).split()

                array2 = np.array(elements, dtype=int).reshape(2, 3)

                print("\nOriginal Array:")
                print(array1)

                print("\nSecond Array:")
                print(array2)

                result = array1 * array2

                print("\nResult of Multiplication:")
                print(result)

            except ValueError:
                print("Invalid input. Please enter exactly 6 integer values.")

        # 4. Division
        elif choice == 4:
            try:
                array1 = np.array([
                    [10, 20, 30],
                    [40, 50, 60]
                ])

                elements = input(
                    "Enter 6 elements for second array separated by space: "
                ).split()

                array2 = np.array(elements, dtype=int).reshape(2, 3)

                print("\nOriginal Array:")
                print(array1)

                print("\nSecond Array:")
                print(array2)

                if np.any(array2 == 0):
                    print("\nDivision by zero is not allowed.")
                else:
                    result = array1 / array2

                    print("\nResult of Division:")
                    print(result)

            except ValueError:
                print("Invalid input. Please enter exactly 6 integer values.")

        # 5. Dot Product
        elif choice == 5:
            array1 = np.array([1, 2, 3])
            array2 = np.array([4, 5, 6])

            result = np.dot(array1, array2)

            print("\nFirst Array:")
            print(array1)

            print("\nSecond Array:")
            print(array2)

            print("\nResult of Dot Product:")
            print(result)

        # 6. Matrix Multiplication
        elif choice == 6:
            array1 = np.array([
                [1, 2],
                [3, 4]
            ])

            array2 = np.array([
                [5, 6],
                [7, 8]
            ])

            result = np.matmul(array1, array2)

            print("\nFirst Matrix:")
            print(array1)

            print("\nSecond Matrix:")
            print(array2)

            print("\nResult of Matrix Multiplication:")
            print(result)

        # 7. Go Back
        elif choice == 7:
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


#mathematical_operations_menu()