def print_operation_table(operation, table_rows=9, table_column=9):
    for i in range(1, table_column + 1):
        for j in range(1, table_rows + 1):
            if i == 1:
                print(j, end="\t")
            else:
                if j == 1:
                    print(i, end="\t")
                else:
                    print(operation(i, j), end="\t")
        print()


print_operation_table(lambda x, y: x + y, 5, 5)
