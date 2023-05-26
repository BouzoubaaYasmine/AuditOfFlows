import os
import re
import datetime
import random
import string

pattern = r'^[a-zA-Z]+_\d{6}\.txt$'

date = datetime.datetime.now().strftime("%y%m%d")


files = []
for i in range(20):
    # Generate a random filename
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    # Generate a random date in the past year
    date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365))
    # Combine the filename, date, and extension to form the full filename
    filename = f"{name}_{date.strftime('%y%m%d')}.txt"
    files.append(filename)

    # Add some incorrect filenames for testing
    if i % 5 == 0:
        files.append(f"{name}_{date.strftime('%m%d%y')}.txt")
        files.append(f"{name}_{date.strftime('%d%m%y')}.txt")
        files.append(f"{name}_{date.strftime('%m%y%d')}.txt")
        files.append(f"{name}_{date.strftime('%d%y%m')}.txt")
        files.append(f"{name}.txt")
        files.append(f"{name}.txt")

for filename in files:
    if not re.match(pattern, filename):
        name, ext = os.path.splitext(filename)
        if re.search(r'\d{6}', name):
            old_date = re.search(r'\d{6}', name).group(0)
            new_name = re.sub(rf'_', f"", name)
            new_filename = f"{new_name}_{old_date}.txt"
        else:
            # Construct the new filename using the specified format
            new_name = name
            new_filename = f"{new_name}_{date.strftime('%y%m%d')}{ext}"


        new_filename = re.sub('/', '', new_filename)
        # Rename the file (in this case, just print a message indicating the new name)
        print(f"Renaming file '{filename}' to '{new_filename}'")
    else:
        # Print a message indicating that the file name is correct
        print(f"File '{filename}' is correctly named")
