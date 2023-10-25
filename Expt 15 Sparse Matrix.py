class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.sparse_matrix = {}

    def set_element(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if value != 0:
                self.sparse_matrix[(row, col)] = value
            elif (row, col) in self.sparse_matrix:
                del self.sparse_matrix[(row, col)]
        else:
            print("Invalid row or column index.")

    def get_element(self, row, col):
        if (row, col) in self.sparse_matrix:
            return self.sparse_matrix[(row, col)]
        return 0

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.get_element(row, col), end=" ")
            print()

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = SparseMatrix(rows, cols)

for row in range(rows):
    for col in range(cols):
        value = int(input(f"Enter element at row {row}, column {col}: "))
        matrix.set_element(row, col, value)

print("Sparse Matrix:")
matrix.display()
