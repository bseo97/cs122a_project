import sys
from create_tables import create_tables
from import_data import import_csv_data

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("NO COMMAND PASSED")
    else:
        if sys.argv[1] == "import" and len(sys.argv) == 3:
            create_tables()
            import_csv_data(sys.argv[2])
        else:
            print("Invalid input")
