import requests
import pandas as pd

# Define a function to check if a site is online
def site_is_online(url, timeout=2):
    try:
        # Send a HEAD request to the URL with a timeout
        r = requests.head(url, timeout=timeout)
        # Check the response status code for success
        r.raise_for_status()
        return True
    except:
        return False

# Load the list of URLs from an Excel file into a DataFrame
df = pd.read_excel('list.xlsx')

# Iterate over each row in the DataFrame
for i, url in df.iterrows():
    # Print progress as a percentage and the current URL being checked
    print(f"{round((i/len(df)*100), 2)}% {url[0]}")
    try:
        # Set the 'Status' column to 'Yes' if the site is online, otherwise 'No'
        df.at[i, 'Status'] = "Yes" if site_is_online(url[0]) else "No"
    except:
        df.at[i, 'Status'] = "No"

# Save the updated DataFrame to a new Excel file without an index column
df.to_excel('checkedlist.xlsx', index=False)