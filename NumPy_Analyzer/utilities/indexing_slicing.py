import numpy as np


def indexing_slicing_menu(array):
    while True:
        print("\nChoose an operation:")
        print("1. 1D Indexing")
        print("2. 2D Indexing")
        print("3. 3D Indexing")
        print("4. Slicing")
        print("5. Go Back")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                try:
                    print("\nOriginal Array:")
                    print(array)

                    index = int(input("Enter index: "))

                    print("Selected element:")
                    print(array[index])

                except ValueError:
                    print("Invalid input. Please enter a number.")

                except IndexError:
                    print("Invalid index. Please enter a valid index.")

            elif choice == 2:
                try:
                    if array.ndim != 2:
                        print("\nThe selected array is not a 2D array.")
                        continue

                    print("\nOriginal Array:")
                    print(array)

                    row = int(input("Enter row index: "))
                    column = int(input("Enter column index: "))

                    print("Selected element:")
                    print(array[row, column])

                except ValueError:
                    print("Invalid input. Please enter numbers.")

                except IndexError:
                    print("Invalid row or column index.")

            elif choice == 3:
                try:
                    if array.ndim != 3:
                        print("\nThe selected array is not a 3D array.")
                        continue

                    print("\nOriginal Array:")
                    print(array)

                    layer = int(input("Enter layer index: "))
                    row = int(input("Enter row index: "))
                    column = int(input("Enter column index: "))

                    print("Selected element:")
                    print(array[layer, row, column])

                except ValueError:
                    print("Invalid input. Please enter numbers.")

                except IndexError:
                    print("Invalid layer, row, or column index.")

            elif choice == 4:
                try:
                    print("\nOriginal Array:")
                    print(array)

                    if array.ndim == 1:
                        start = int(input("Enter start index: "))
                        end = int(input("Enter end index: "))

                        sliced_array = array[start:end]

                    elif array.ndim == 2:
                        row_range = input("Enter row range (start:end): ")
                        column_range = input("Enter column range (start:end): ")

                        row_start, row_end = map(int, row_range.split(":"))
                        column_start, column_end = map(int, column_range.split(":"))

                        sliced_array = array[row_start:row_end, column_start:column_end]

                    elif array.ndim == 3:
                        layer_range = input("Enter layer range (start:end): ")
                        row_range = input("Enter row range (start:end): ")
                        column_range = input("Enter column range (start:end): ")

                        layer_start, layer_end = map(int, layer_range.split(":"))
                        row_start, row_end = map(int, row_range.split(":"))
                        column_start, column_end = map(int, column_range.split(":"))

                        sliced_array = array[
                            layer_start:layer_end,
                            row_start:row_end,
                            column_start:column_end
                        ]

                    print("\nSliced Array:")
                    print(sliced_array)

                except ValueError:
                    print("Invalid input. Please enter valid numbers or ranges.")

                except IndexError:
                    print("Invalid slicing range.")

            elif choice == 5:
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")