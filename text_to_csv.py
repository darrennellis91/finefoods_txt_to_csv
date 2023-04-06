import csv

input_file = 'foods.txt'  # Replace with your input text file name
output_file = 'foods.csv'  # Replace with your desired output CSV file name

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['product/productId', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score', 'review/time', 'review/summary', 'review/text']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    current_record = {}
    for line in infile:
        if line.strip() == '':
            if current_record:
                writer.writerow(current_record)
                current_record = {}
        else:
            try:
                key, value = line.strip().split(': ', 1)
                current_record[key] = value
            except ValueError:
                print(f'Skipping malformed line: {line.strip()}')


    if current_record:
        writer.writerow(current_record)
