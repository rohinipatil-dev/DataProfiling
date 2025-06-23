import json
import pandas as pd
from ydata_profiling import ProfileReport  # pip install ydata-profiling

# CONFIG - Set JSON Date File name
FILE_NAME = "TestDataSet.json"

# Load JSON
with open(FILE_NAME) as f:
    raw_data = json.load(f)

# Parse records into dicts
parsed_data = []
for record in raw_data:
    row = {}
    for item in record:
        key, val = item.split(": ")
        # Clean and convert values
        if "%" in val:
            val = val.replace("%", "")
        if "°C" in val:
            val = val.replace("°C", "")
        try:
            val = float(val)
        except ValueError:
            pass
        row[key.strip()] = val
    parsed_data.append(row)

# Convert to DataFrame
df = pd.DataFrame(parsed_data)

# Generate profiling report
profile = ProfileReport(df, title="Sensor Data Profiling Report", explorative=True)
profile.to_file("sensor_profiling_report.html")
