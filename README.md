<!DOCTYPE html>
<html>
  <body>
    <h1>Check URLs Status</h1>
    <p>This Python script checks if a list of URLs are online by sending a HEAD request and returns the status of the request ('Yes' for success and 'No' for failure), and saves the updated DataFrame with the status of each URL to a new Excel file without an index column.</p>
    <h2>Instructions</h2>
    <ol>
      <li>Make sure you have Python 3 installed on your computer.</li>
      <li>Install the necessary Python modules by running the following command in your terminal: <code>pip install requests pandas</code></li>
      <li>Save your list of URLs in an Excel file named 'list.xlsx' in the same directory as the Python script.</li>
      <li>Run the script by running the following command in your terminal: <code>python check_urls_status.py</code></li>
      <li>The script will print the progress as a percentage and the current URL being checked.</li>
      <li>Once the script is finished, it will save the updated DataFrame with the status of each URL to a new Excel file named 'checkedlist.xlsx' in the same directory as the Python script.</li>
    </ol>
  </body>
</html>
