import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
from gef_branding import PRIMARY_GREEN, MUSEO_WEIGHTS

# Set the default font family for Matplotlib
# mpl.rcParams['font.family'] = 'Museo 300'

# Read the CSV file
df = pd.read_csv('export_with_iso3.csv')

# Exclude rows where 'Lead Agency Name' is 'GEFSEC'
df = df[df['Lead Agency Name'] != 'GEFSEC']

# Path to the world shapefile (Column name: ISO_A3)
world_shapefile_path = r'ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp'

# Load the shapefile into a GeoDataFrame
world = gpd.read_file(world_shapefile_path)

# Exclude Antarctica
world = world[world['ISO_A3'] != 'ATA']

# Create the 'Counts' column by aggregating data
df_aggregated = df.groupby(['Country Name List ISO3', 'Lead Agency Name']).size().reset_index(name='Counts')

# Merge your data with the world geometries based on ISO3 codes
df_geo = world.merge(df_aggregated, left_on='ISO_A3', right_on='Country Name List ISO3', how='right')

# Exclude rows with multiple countries or 'N/A' in 'Country Name List ISO3'
df_geo = df_geo[~df_geo['Country Name List ISO3'].str.contains('N/A')]

# List unique agencies
agencies = df_geo['Lead Agency Name'].unique()

# Determine the global min and max counts
vmin = df_geo['Counts'].min()
vmax = df_geo['Counts'].max()

# Calculate the total number of unique countries covered in the overall dataset
total_countries_covered = df_geo['Country Name List ISO3'].nunique()

# Calculate the total number of projects in the overall dataset
total_projects = df_geo['Counts'].sum()

# Calculate the number of countries covered per agency
countries_per_agency = df_geo.groupby('Lead Agency Name')['Country Name List ISO3'].nunique()

# Calculate the total counts per agency
counts_per_agency = df_geo.groupby('Lead Agency Name')['Counts'].sum()

# Set up a figure with subplots
cols = 6
rows = 3

fig = plt.figure(figsize=(20, 15))
gs = GridSpec(rows + 1, cols, figure=fig)
# Plot the overall coverage map first
ax = fig.add_subplot(gs[0, :])
overall_data = df_geo.groupby('Country Name List ISO3').agg({'Counts': 'sum'}).reset_index()
overall_data = world.merge(overall_data, left_on='ISO_A3', right_on='Country Name List ISO3', how='right')
world.boundary.plot(ax=ax, linewidth=0.2, color='gray')
overall_data.plot(column='Counts', ax=ax, legend=False,
                  cmap='coolwarm',
                  vmin=vmin, vmax=vmax)
ax.set_title(f'Overall Coverage\nCountries: {total_countries_covered}, Projects: {total_projects}', fontsize=10)
ax.set_axis_off() 
ax.set_aspect('equal')

# Plot each agency's coverage
for i, agency in enumerate(agencies): 
    row = (i // cols) + 1 
    col = i % cols
    ax = fig.add_subplot(gs[row, col])
    agency_data = df_geo[df_geo['Lead Agency Name'] == agency]
    world.boundary.plot(ax=ax, linewidth=0.2, color='gray')
    agency_data.plot(column='Counts', ax=ax, legend=False,
                     cmap='coolwarm',
                     vmin=vmin, vmax=vmax)
    num_countries = countries_per_agency[agency]
    total_counts = counts_per_agency[agency]
    ax.set_title(f'{agency}\nCountries: {num_countries}, Projects: {total_counts}', fontsize=8)
    ax.set_axis_off()
    ax.set_aspect('equal')

# Add a colorbar that applies to all subplots
cbar_ax = fig.add_axes([0.02, 0.9, 0.2, 0.02])  # Adjust the position and size as needed
sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
sm._A = []  # This line may be used to avoid a warning in some Matplotlib versions
cbar = fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')  # Set orientation to horizontal
cbar.set_label('Number of Projects', fontsize=10)

# Adjust layout to reduce whitespace
plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, top=.96, bottom=0)
plt.suptitle('Agencies Concentration Analysis (Ver 0.1)', fontsize=16, x=0.02, y=.98, ha='left')
plt.show()