import pandas as pd
import sys
from os.path import exists 

def PARQreader():
    print("CSV -> CSV to parquet\nP -> Read parquet")
    while True:
        mode = input("Enter mode: ").lower()

        if mode == "csv":
            while True:
                csv_file = input("CSV file name: ")
                new_file_name = input("New parquet file name: ")

                csv_file += ".csv"
                new_file_name += ".parquet"

                if exists(new_file_name):
                    print("Answer with y or n.")
                    u_sure = input("Are you sure you would like to replace an existing file?: ")
                    if u_sure == "y":
                        break
                    elif u_sure == "n":
                        print("Please fill out the file names carefully.\n")
                        continue
                
                break


            readcsv = pd.read_csv(csv_file)
            readcsv.to_parquet(new_file_name)
            new = pd.read_parquet(new_file_name)

            print("\nHT -> Head and Tail\nR -> Read")
            
            while True:
                rmode = input("Enter read mode: ").lower()

                if rmode == "ht":
                    headcount = int(input("Enter head rows: "))
                    tailcount = int(input("Enter tail rows: "))
                    print(f"First {headcount} rows:\n{new.head(headcount)}")
                    print(f"Last {tailcount} rows:\n{new.tail(tailcount)}")
                    return True
                
                elif rmode == "r":
                    new = pd.read_parquet(new_file_name)
                    print(f"Content of {new_file_name} rows:\n{new}")
                    return True
                
                else:
                    print("Please enter a read mode.\n")
                    continue

        elif mode == "p":
            new_file_name = input("Enter parquet: ")

            new_file_name += ".parquet"
            new = pd.read_parquet(new_file_name)

            print("HT -> Head and Tail\nR -> Read")
            
            while True:
                rmode = input("Enter read mode: ").lower()

                if rmode == "ht":
                    headcount = int(input("Enter head rows: "))
                    tailcount = int(input("Enter tail rows: "))
                    print(f"First {headcount} rows:\n{new.head(headcount)}")
                    print(f"Last {tailcount} rows:\n{new.tail(tailcount)}")
                    return True
                
                elif rmode == "r":
                    new = pd.read_parquet(new_file_name)
                    print(f"Content of {new_file_name} rows:\n{new}")
                    return True
                
                else:
                    print("Please enter a read mode.\n")
                    continue
            
        elif mode == "i":
            if __name__ == "__main__":

                print(f"\nPARQreader")
                print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                print(f"MADE WITH PANDAS 2.3.1 | Current Pandas version: {pd.__version__}")
                print(f"Being imported: No\nFile path: {__file__}")
            else:

                print(f"\nPARQreader")
                print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                print(f"MADE WITH PANDAS 2.3.1 | Current Pandas version: {pd.__version__}")
                print(f"Being imported: Yes\nFile path: {__file__}")

        else:
            print("Please choose a mode.\n")
            continue

PARQreader() # Do you know how easy this was? For some reason, really easy.