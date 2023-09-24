import os
from sql_insert_csv import generate_insert_script

csv_filename = "example.csv"
output_filename = "example_insert.sql"
sql_tablename = "[schema].[tablename]"

def main():
    cwd = os.getcwd()
    csv_filepath = os.path.join(cwd, csv_filename)
    sql_filepath = os.path.join(cwd, output_filename)
    generate_insert_script(sql_tablename, csv_filepath, sql_filepath)

if __name__ == "__main__":
    main()