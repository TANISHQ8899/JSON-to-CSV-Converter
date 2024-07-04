import json
import csv
import logging
import sys

def json_to_csv(json_file, csv_file):
    try:
        # Load JSON data
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        if not data:
            raise ValueError("JSON data is empty")
        
        # Get the header from the first dictionary keys
        header = list(data[0].keys())
        
        # Open CSV file for writing
        with open(csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Write header
            csvwriter.writerow(header)
            
            # Write data rows
            for obj in data:
                row = [obj.get(key, '') for key in header]
                csvwriter.writerow(row)
        
        logging.info(f"Successfully converted {json_file} to {csv_file}")

        # Print the result
        print("\nCSV file created successfully. Here are the contents:")
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(", ".join(row))

    except FileNotFoundError as fnf_error:
        logging.error(f"File not found: {fnf_error}")
    except json.JSONDecodeError as json_error:
        logging.error(f"Error decoding JSON: {json_error}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json_to_csv.py <input_json_file> <output_csv_file>")
        sys.exit(1)

    input_json_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    logging.basicConfig(level=logging.INFO)
    json_to_csv(input_json_file, output_csv_file)
