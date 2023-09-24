from glob import glob
import os

def create_directory_if_not_exists(directory_fullpath):
    try:
        os.mkdir(directory_fullpath)
    except FileExistsError:
        pass


def find_files(folder, file_pattern):
    files = glob(folder + '\\' + file_pattern)
    print(f"{len(files)} files found with pattern {file_pattern}.")
    return files


def merge_csvs(csv_list, merged_csv_filepath):
    if (len(csv_list) == 0): raise ValueError("CSV list is empty.")
    total_row_count = 0

    create_directory_if_not_exists(os.path.dirname(merged_csv_filepath))
    with open(merged_csv_filepath, 'w') as merged_csv:
        # Write header
        with open(csv_list[0], 'r') as csv:
            merged_csv.writelines(csv.readlines()[0])

        # Write data from each CSV
        for csv in csv_list:
            with open(csv, 'r') as current_csv:
                data = current_csv.readlines()[1:] # Exclude the header row
                if not data[-1].endswith('\n'):
                    data[-1] += '\n' # Add newline if necessary

                merged_csv.writelines(data)
                total_row_count += len(data)

    print(f"Merged CSVs into a file with {total_row_count} records.")


def merge_csvs_with_pattern(file_pattern, merged_csv_name, csv_directory):
    csv_list = find_files(csv_directory, file_pattern)
    merge_csvs(csv_list, merged_csv_name)