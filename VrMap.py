import plotly.express as px
import pandas as pd

# Mapping of state names to abbreviations
state_abbr = {
    "California": "CA", "Texas": "TX", "New York": "NY", "Florida": "FL",
    "Illinois": "IL", "Pennsylvania": "PA", "Ohio": "OH", "Georgia": "GA",
    "North Carolina": "NC", "Michigan": "MI"
}

# VR adoption dataset with socioeconomic factors
data = {
    "State": ["California", "Texas", "New York", "Florida", "Illinois", 
              "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan"],
    "State Abbreviation": ["CA", "TX", "NY", "FL", "IL", "PA", "OH", "GA", "NC", "MI"],
    "Total VR Adoption (%)": [20, 18, 19, 15, 14, 13, 12, 11, 10, 9],
    "16-24 (%)": [34, 32, 33, 30, 29, 27, 25, 23, 22, 20],
    "25-34 (%)": [35, 33, 34, 31, 30, 28, 26, 24, 23, 21],
    "35-44 (%)": [26, 24, 25, 22, 21, 19, 17, 15, 14, 12],
    "45-54 (%)": [12, 11, 11, 10, 9, 8, 7, 6, 6, 5],
    "55+ (%)": [6, 5, 5, 4, 4, 3, 3, 2, 2, 1],
    "Median Income ($)": [80000, 75000, 78000, 70000, 72000, 68000, 65000, 62000, 60000, 58000],
    "Urbanization (%)": [95, 90, 92, 85, 88, 80, 75, 70, 68, 65],
    "Male Ownership (%)": [74, 73, 75, 72, 71, 70, 69, 68, 67, 66]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create an interactive heatmap for VR adoption with socioeconomic data
fig = px.choropleth(
    df,
    locations="State Abbreviation",  # Now using state abbreviations
    locationmode="USA-states",
    color="Total VR Adoption (%)",
    hover_data={
        "State": True,
        "Total VR Adoption (%)": True,
        "16-24 (%)": True,
        "25-34 (%)": True,
        "35-44 (%)": True,
        "45-54 (%)": True,
        "55+ (%)": True,
        "Median Income ($)": True,
        "Urbanization (%)": True,
        "Male Ownership (%)": True
    },
    color_continuous_scale="Blues",
    scope="usa",
    title="VR Headset Adoption in the United States (with Socioeconomic Data)"
)

# Show the map
fig.show()
