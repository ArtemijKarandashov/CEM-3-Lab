import urllib
import urllib.request
import bs4
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt
# ./env/bin/python ./env/html_parse.py

data = urllib.request.urlopen("https://wttr.in/st-petersburg").read().decode('utf-8')

soup = BeautifulSoup(data,"html.parser")

body_content = soup.body
ef050 = body_content.findAll("span",class_ = "ef050")
ef049 = body_content.findAll("span",class_ = "ef049")
ef048 = body_content.findAll("span",class_ = "ef048")

#day1 = [int(ef050[0].text),int(ef049[0].text),int(ef050[1].text),int(ef050[2].text)]
#day2 = [int(ef049[1].text),int(ef048[0].text),int(ef048[1].text),int(ef048[2].text)]

#print(day1)
#print(day2)

day1 = [0,2,0,0]
day2 = [2,4,4,4]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a figure with two subplots
fig, axs = plt.subplots(1,2, figsize=(12, 6))

# Create histograms for each day
axs[0].bar(['Morning', 'Day', 'Evening', 'Night'], day1)
axs[0].set_title('Temperature Histogram - Day 1')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Temperature')

axs[1].bar(['Morning', 'Day', 'Evening', 'Night'], day2)
axs[1].set_title('Temperature Histogram - Day 2')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Temperature')

# Layout so plots do not overlap
fig.tight_layout()

# Save the plot to a file
plt.savefig('temperature_histograms.png')