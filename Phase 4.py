import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('traffic_index.csv')
df['trafficindexdate'] = pd.to_datetime(df['trafficindexdate'])

# Bar chart: Monthly average traffic index
monthly_avg = df.resample('M', on='trafficindexdate')['average_traffic_index'].mean()
plt.bar(monthly_avg.index.strftime('%Y-%m'), monthly_avg.values, color='red')
plt.xticks(rotation=90)
plt.title('Monthly Average Traffic Index')
plt.xlabel('Month')
plt.ylabel('Average Traffic Index')
plt.tight_layout()
plt.savefig('traffic_bar_chart.png')
plt.close()

# Scatter plot: Maximum vs Average Traffic Index
plt.scatter(df['maximum_traffic_index'], df['average_traffic_index'], alpha=0.5)
plt.title('Maximum vs Average Traffic Index')
plt.xlabel('Maximum Traffic Index')
plt.ylabel('Average Traffic Index')
plt.tight_layout()
plt.savefig('traffic_scatter_plot.png')
plt.close()
