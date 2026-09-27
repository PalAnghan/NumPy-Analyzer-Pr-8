# NumPy Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-1.x-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/CLI-Interactive-111827?style=for-the-badge" alt="CLI">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-22C55E?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>A menu-driven Python project for learning and practicing NumPy interactively.</b>
</p>

<p align="center">
  Create arrays → manipulate data → analyze values → understand NumPy
</p>

---

## Demo

<p align="center">
  <img src="assets/demo.gif" alt="NumPy Analyzer animated demo" width="850">
</p>

> A small interactive NumPy playground built as a practical learning project.

---

## What is NumPy Analyzer?

**NumPy Analyzer** is a terminal-based Python application that brings multiple NumPy concepts into one structured program.

Instead of creating a separate Python file every time you want to practice an array operation, you can select an operation from the menu and perform it interactively.

The project focuses on practical learning of:

- NumPy arrays
- 1D, 2D and 3D arrays
- Indexing
- Slicing
- Mathematical operations
- Combining and splitting arrays
- Searching
- Sorting
- Filtering
- Aggregates
- Statistics
- Python modules and imports
- Exception handling
- Menu-driven CLI design

---

## Features

<table>
<tr>
<td width="50%">

### Array Creation

Create:

- 1D arrays
- 2D arrays
- 3D arrays
- Custom dimensions
- User-defined values

</td>
<td width="50%">

### Indexing & Slicing

Practice:

- 1D indexing
- 2D indexing
- 3D indexing
- Row/column selection
- Array slicing
- Dimension validation

</td>
</tr>

<tr>
<td>

### Mathematical Operations

Perform numerical operations on NumPy arrays through an interactive menu.

</td>
<td>

### Combine & Split

Practice combining arrays and splitting array data into smaller parts.

</td>
</tr>

<tr>
<td>

### Search / Sort / Filter

Find values, sort array elements, and filter data using NumPy operations.

</td>
<td>

### Statistics

Work with:

- Sum
- Mean
- Median
- Standard deviation
- Variance

</td>
</tr>
</table>

---

## Main Menu

```text
Welcome to the NumPy Analyzer!
==============================

Choose an option:

1. Choose a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

---

## Project Architecture

```text
                    ┌──────────────────┐
                    │     main.py      │
                    │  Application     │
                    │     Entry Point  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  interface/      │
                    │     menu.py      │
                    │   Main Menu      │
                    └────────┬─────────┘
                             │
          ┌──────────────────┼───────────────────┐
          │                  │                   │
          ▼                  ▼                   ▼
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │ Array Creation │ │ Indexing &     │ │ Mathematical   │
 │                │ │ Slicing        │ │ Operations     │
 └────────────────┘ └────────────────┘ └────────────────┘
          │                  │                   │
          └──────────────────┼───────────────────┘
                             │
          ┌──────────────────┼───────────────────┐
          ▼                  ▼                   ▼
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │ Combine /      │ │ Search / Sort  │ │ Data Analytics │
 │ Split          │ │ / Filter       │ │ & Statistics   │
 └────────────────┘ └────────────────┘ └────────────────┘
```

---

## Folder Structure

```text
NumPy-Analyzer-Pr-8/
│
├── interface/
│   └── menu.py
│
├── utilities/
│   ├── combine_split.py
│   ├── create_numpy_array.py
│   ├── data_analytics.py
│   ├── indexing_slicing.py
│   ├── mathematical_operations.py
│   └── search_sort_filter.py
│
├── assets/
│   └── demo.gif
│
├── main.py
└── README.md
```

### Module Guide

| Module | Responsibility |
|---|---|
| `main.py` | Starts the application |
| `interface/menu.py` | Controls the main menu and connects modules |
| `create_numpy_array.py` | Creates 1D, 2D and 3D arrays |
| `indexing_slicing.py` | Performs indexing and slicing |
| `mathematical_operations.py` | Performs mathematical operations |
| `combine_split.py` | Combines and splits arrays |
| `search_sort_filter.py` | Searches, sorts and filters arrays |
| `data_analytics.py` | Calculates aggregates and statistics |

---

## Example: Creating a 2D Array

```text
Select the type of array to create:

1. 1D Array
2. 2D Array
3. 3D Array
4. Go Back

Enter your choice: 2

Enter rows: 2
Enter columns: 3
Enter elements: 10 20 30 40 50 60

Array created successfully:

[[10 20 30]
 [40 50 60]]
```

---

## Example: Indexing

For:

```python
array = np.array([10, 20, 30, 40, 50])
```

You can access values using:

```python
array[0]
array[2]
array[-1]
```

Example:

```text
Enter index: 2

Selected element:
30
```

---

## Example: 2D Indexing

For:

```text
[[10 20 30]
 [40 50 60]]
```

You can select a value using:

```python
array[row, column]
```

Example:

```text
Enter row index: 1
Enter column index: 2

Selected element:
60
```

---

## Example: Slicing

```text
Original Array:

[[10 20 30]
 [40 50 60]]

Enter row range (start:end): 0:2
Enter column range (start:end): 1:3

Sliced Array:

[[20 30]
 [50 60]]
```

This demonstrates NumPy's:

```python
array[row_start:row_end, column_start:column_end]
```

---

## Example: Statistics

```text
Original Array:

[[10 20 30]
 [40 50 60]]

Choose aggregate/statistical operation:

1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance

Enter your choice: 3

Median of Array: 35.0
```

---

## Tech Stack

| Technology | Usage |
|---|---|
| Python | Application logic |
| NumPy | Array and numerical operations |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Source code hosting |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/PalAnghan/NumPy-Analyzer-Pr-8.git
```

### 2. Enter the project directory

```bash
cd NumPy-Analyzer-Pr-8
```

### 3. Install NumPy

```bash
pip install numpy
```

### 4. Run the project

```bash
python main.py
```

---

## Requirements

- Python 3.x
- NumPy
- Terminal / Command Prompt
- Git (optional, for cloning and version control)

Check your Python version:

```bash
python --version
```

Check NumPy:

```bash
python -c "import numpy; print(numpy.__version__)"
```

---

## Learning Goals

This project was built to strengthen practical understanding of:

```text
Python
  ↓
Functions
  ↓
Modules & Imports
  ↓
NumPy Arrays
  ↓
Dimensions
  ↓
Indexing & Slicing
  ↓
Array Operations
  ↓
Statistics
  ↓
Interactive CLI
```

It is especially useful for beginners who want to move from **learning NumPy syntax** to actually building something with it.

---

## Project Highlights

- Modular Python structure
- Interactive terminal interface
- Separate utility modules
- 1D / 2D / 3D array support
- Dimension-aware indexing
- Slicing support
- Statistical operations
- Input validation
- Beginner-friendly workflow
- Easy to extend with new NumPy concepts

---

## Future Improvements

Planned or possible improvements:

- Random array generation
- Matrix multiplication
- Reshaping tools
- Transpose operations
- Broadcasting demonstrations
- More advanced filtering
- CSV import/export
- Data visualization
- Unit testing
- Better error messages
- Operation history
- GUI version
- More statistical functions

---

## Author

<p align="center">
  <b>Pal Anghan</b><br>
  BCA Student • Developer • Python & AI/ML Learner
</p>

<p align="center">
  <a href="mailto:palanghan750@gmail.com">Email</a> •
  <a href="https://www.linkedin.com/in/pal-anghan-7733402b4/">LinkedIn</a> •
  <a href="https://github.com/PalAnghan">GitHub</a>
</p>

### Connect

I am interested in:

- Python
- NumPy
- AI/ML
- Web Development
- Software Projects
- Practical automation

Feel free to explore the repository and connect with me.

---

## Repository

**GitHub:**  
https://github.com/PalAnghan/NumPy-Analyzer-Pr-8

---

## License

This project is created for learning and educational purposes.

You are welcome to explore the source code, learn from the implementation, and build your own projects using the concepts demonstrated here.

---

<p align="center">
  <b>Built with Python + NumPy</b>
  <br>
  <sub>Learning by building.</sub>
</p>
