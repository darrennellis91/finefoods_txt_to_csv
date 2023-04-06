# finefoods_txt_to_csv
Text File to CSV Converter
The purpose of this Python script is to convert the food.txt file found at http://snap.stanford.edu/data/web-FineFoods.html.

Input Format
The script expects the input file to follow this format:

<code>
  product/productId: B001E4KFG0
  review/userId: A3SGXH7AUHU8GW
  review/profileName: delmartian
  review/helpfulness: 1/1
  review/score: 5.0
  review/time: 1303862400
  review/summary: Good Quality Dog Food
  review/text: I have bought several of the Vitality canned dog food products and have found them all to be of good quality...
  Each product review entry should be separated by a blank line.
</code>

Usage
<ul>
  <li>Ensure you have **Python** installed on your machine.</li>
 <li>Save the Python script (**text_to_csv.py**) to a local directory.</li>
 <li>Save your input text file containing the product review data in the same directory as the script.</li>
 <li>Update the input_file variable in the script with the name of your input text file.</li>
 <li>Update the output_file variable in the script with the desired name for your output CSV file.</li>
 <li>Run the Python script using the command: python text_to_csv.py</li>
 <li>The script will generate a CSV file with the extracted fields from the input text file.</li>
</ul>

Output
The output CSV file will contain the following columns:

- product/productId
- review/userId
- review/profileName
- review/helpfulness
- review/score
- review/time
- review/summary
- review/text
- Troubleshooting

