import csv

def column_list_string(header_list):
    return ', '.join(header_list)


def row_values_string(row):
    row_string = ''
    for value in row:
        if value == 'NULL' or value.replace(".", "").isnumeric():
            row_string += value
        else: 
            value_quotes_escaped = value.replace("'", "''")
            # Values that are not NULL or numeric should be wrapped in single quotes
            row_string += f"\'{value_quotes_escaped}\'"
        
        row_string += ', '
    return row_string[:-2]


def insert_row_command(tablename, columns_string, values_string):
    return f"INSERT INTO {tablename}\n({columns_string})\nVALUES\n({values_string});"


def insert_script_text(sql_tablename, csv_lines):
    header, data = csv_lines[0], csv_lines[1:]
    sql_string = ''
    column_list = column_list_string(header)

    for row in data:
        values_string = row_values_string(row)
        sql_string += insert_row_command(sql_tablename, column_list, values_string) + '\n\n'

    return sql_string


def generate_insert_script(sql_tablename, csv_filepath, sql_filepath):
    with open(csv_filepath, 'r') as f:
        lines = list(csv.reader(f))

    with open(sql_filepath, 'w') as f:
        f.write(insert_script_text(sql_tablename, lines))