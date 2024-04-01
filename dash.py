import matplotlib.pyplot as plt
import seaborn as sns
# Let's first load and examine the uploaded CSV file to understand its structure and content.
import pandas as pd

# Load the CSV file
df = pd.read_csv('/mnt/data/data.csv')

# Display the first few rows of the dataframe to understand its structure and content
df.head()


# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a figure to hold the dashboard subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Title for the dashboard
fig.suptitle('Data Visualization Dashboard', fontsize=20)

# Plot for distribution of individuals across states
sns.countplot(ax=axes[0, 0], data=df, x='state')
axes[0, 0].set_title('State Distribution')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot for gender distribution
sns.countplot(ax=axes[0, 1], data=df, x='gender')
axes[0, 1].set_title('Gender Distribution')

# Plot for age group distribution
sns.countplot(ax=axes[1, 0], data=df, x='age_group', order=sorted(df['age_group'].unique()))
axes[1, 0].set_title('Age Group Distribution')
axes[1, 0].tick_params(axis='x', rotation=45)

# Plot for distribution of years of job experience
sns.histplot(ax=axes[1, 1], data=df, x='yearsJob', bins=10, kde=True)
axes[1, 1].set_title('Years of Job Experience Distribution')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the dashboard
plt.show()
