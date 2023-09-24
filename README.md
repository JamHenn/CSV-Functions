# CSV Functions
Some python scripts that I used, while working as a data engineer, to perform repetitive tasks with CSV files.


## Merge CSVs
This is used to take multiple tabular CSVs with the same format/schema, and merge them into one file.

I used this while working as a data engineer to merge months worth of daily source files into one.
Usually the files would automatically go through an ETL pipeline, but there were times when historic data loads were needed.
Merging the CSVs allowed all the historic data to be loaded in a single pipeline run, which saved a lot of time.


## SQL Insert CSV
This is used to take a CSV file, which has the same column names as a SQL table, and generate an insert script.
The insert script allows the data contained in the CSV to be loaded into the corresponding SQL table.

The SQL database I used at the time didn't support the multi-row `VALUES(),()` syntax, so it generates one `INSERT` command per line in the CSV.
