from csv_merge import merge_csvs_with_pattern
import os

csv_dir = 'CSVs'
output_dir = 'CSVs\\Merged'
file_pattern = 'file*.csv'
merged_csv_name = 'merged.csv'

def main():
    merged_csv_filepath = os.path.join(os.getcwd(), output_dir, merged_csv_name)
    merge_csvs_with_pattern(file_pattern, merged_csv_filepath, csv_dir)

if __name__ == '__main__':
    main()