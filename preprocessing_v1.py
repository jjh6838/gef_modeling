import pycountry
import pandas as pd

# 1. Data Preprocessing with ISO3 Country Codes
# Initialize a set to store country names that could not be converted
unconverted_countries = set()

# Custom mappings for special cases
custom_country_mappings = {
    "Republic Of Korea": "KOR",
    "St. Vincent and Grenadines": "VCT",
    "Bosnia-Herzegovina": "BIH",
    "Palestinian Authority": "PSE",
    "Kosovo": "XKX",  # Not officially an ISO code, but commonly used
    "Global": "N/A",  # No ISO code, as it represents the entire world
    "Latin America and Caribbean": "N/A",  # No specific ISO code for the entire region
    "Regional": "N/A",  # No specific ISO code, as it is too general
    "Asia/Pacific": "N/A",  # No specific ISO code for the entire region
    "Europe and Central Asia": "N/A",  # No specific ISO code for the entire region
    "Cote d'Ivoire": "CIV",
    "Lao PDR": "LAO",
    "Korea DPR": "PRK",
    "Africa": "N/A",  # No specific ISO code for the entire continent
    "Micronesia": "FSM",
    "Brunei": "BRN",
    "Congo DR": "COD",
    "St. Lucia": "LCA",
    "Timor Leste": "TLS",
    "Serbia and Montenegro": "N/A",  # No current ISO code as the country has split
    "Yugoslavia": "N/A",  # No current ISO code as the country no longer exists
    "St. Kitts and Nevis": "KNA"
}

# Modified function to convert country names to ISO3 codes and collect unconverted names
def country_to_iso3(country_name):
    # Check if the country name is in the custom mappings first
    if country_name in custom_country_mappings:
        return custom_country_mappings[country_name]
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except LookupError:
        # Add the unconverted country name to the set
        unconverted_countries.add(country_name)
        return "N/A"  # Return "N/A" if the country name is not found or not mapped

# Function to handle cells with multiple country names
def process_countries(cell, delimiter=','):
	# Split the cell by the delimiter to handle multiple countries
	countries = cell.split(delimiter)
	# Convert each country name to its ISO3 code
	iso3_countries = [country_to_iso3(country.strip()) for country in countries]
	# Filter out any None values in case some country names couldn't be converted
	iso3_countries = filter(None, iso3_countries)
	# Join the ISO3 codes back into a single string
	return delimiter.join(iso3_countries)

# Read the CSV file
df = pd.read_csv('export.csv')

# Apply the conversion to the "Country Name List" column
df['Country Name List ISO3'] = df['Country Name List'].apply(lambda x: process_countries(x))

# Optionally, save the modified DataFrame back to a new CSV
df.to_csv('export_with_iso3.csv', index=False)

print("Data preprocessing is completed.")