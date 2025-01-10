import requests
import matplotlib.pyplot as plt
import seaborn as sns

# API setup
API_KEY = "de6b916e10ea0b9b21ecf8f1ef16381b"
city_Name = "Pune"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_Name}&appid={API_KEY}&units=metric"

# API request
response = requests.get(url)

# Check if request successfull
if response.status_code == 200:
  print("Data fetched successfully!")
  wheather_data = response.json()
else:
  print("Failed to fetch data. Check your API key or city name.")
  exit()

# Process the data
timestamp = []
temperatures = []

for entry in wheather_data['list']:
  timestamp.append(entry['dt_txt']) # Time of forecast
  temperatures.append(entry['main']['temp']) #Temperature in celsius

# Print the preview of data
print("Timestamps: ",timestamp[:5])
print("Temperatures :",temperatures[:5])

# Visualize the data
plt.figure(figsize=(12,6)) # size of plot

sns.lineplot(x=timestamp,y=temperatures,markers='o',color='b')

# Improvment of visualization
plt.title(f'Temperature forecast for {city_Name}',fontsize=16)
plt.xlabel('Timestamp',fontsize=12)
plt.ylabel('Temperature (°C)',fontsize=12)
plt.xticks(rotation=45, fontsize=10)  # Rotate x-axis labels
plt.tight_layout()  # Adjust layout to fit everything

plt.show()
