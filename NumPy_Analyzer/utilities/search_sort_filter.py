import numpy as np


def search_sort_filter():
    while True:
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        print("4. Go Back")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice:

            # 1. Search a value
            case 1:
                try:
                    array = np.array([10, 20, 30, 40, 50, 60])

                    print("\nArray:")
                    print(array)

                    value = int(
                        input("Enter the value to search: ")
                    )

                    result = np.where(array == value)

                    if len(result[0]) > 0:
                        print("Value found at index:", result[0][0])
                    else:
                        print("Value not found.")

                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # 2. Sort the array
            case 2:
                try:
                    array = np.array([40, 10, 60, 20, 50, 30])

                    print("\nOriginal Array:")
                    print(array)

                    print("\n1. Ascending")
                    print("2. Descending")

                    order = int(
                        input("Enter your choice: ")
                    )

                    if order == 1:
                        result = np.sort(array)

                        print("\nSorted Array (Ascending):")
                        print(result)

                    elif order == 2:
                        result = np.sort(array)[::-1]

                        print("\nSorted Array (Descending):")
                        print(result)

                    else:
                        print(
                            "Invalid choice. Please enter 1 or 2."
                        )

                except ValueError:
                    print("Invalid input. Please enter a number.")

            # 3. Filter values
            case 3:
                try:
                    array = np.array([10, 20, 30, 40, 50, 60])

                    print("\nOriginal Array:")
                    print(array)

                    print("\n1. Greater than")
                    print("2. Less than")
                    print("3. Equal to")

                    condition = int(
                        input("Enter your choice: ")
                    )

                    value = int(
                        input("Enter the value: ")
                    )

                    if condition == 1:
                        result = array[array > value]

                        print("\nFiltered Array:")
                        print(result)

                    elif condition == 2:
                        result = array[array < value]

                        print("\nFiltered Array:")
                        print(result)

                    elif condition == 3:
                        result = array[array == value]

                        print("\nFiltered Array:")
                        print(result)

                    else:
                        print(
                            "Invalid choice. Please enter 1, 2, or 3."
                        )

                except ValueError:
                    print("Invalid input. Please enter integers.")

            # 4. Go Back
            case 4:
                break

            case _:
                print(
                    "Invalid choice. Please enter a number between 1 and 4."
                )


#search_sort_filter()