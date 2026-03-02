import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Global Cost of Living Dashboard",
    page_icon="🌍",
    layout="wide"
)

# --- Extended Data Source ---
def get_expanded_data():
    """
    Returns a large hardcoded dataset representing global cost of living indices.
    Base Reference: New York City = 100.
    """
    return [
        # --- North America ---
        {"City": "New York", "Country": "USA", "Region": "North America", "Cost of Living Index": 100.0, "Rent Index": 100.0, "Groceries Index": 100.0, "Restaurant Price Index": 100.0, "Local Purchasing Power": 100.0},
        {"City": "San Francisco", "Country": "USA", "Region": "North America", "Cost of Living Index": 96.5, "Rent Index": 105.3, "Groceries Index": 98.2, "Restaurant Price Index": 95.1, "Local Purchasing Power": 108.2},
        {"City": "Honolulu", "Country": "USA", "Region": "North America", "Cost of Living Index": 94.2, "Rent Index": 78.5, "Groceries Index": 102.1, "Restaurant Price Index": 88.4, "Local Purchasing Power": 85.2},
        {"City": "Los Angeles", "Country": "USA", "Region": "North America", "Cost of Living Index": 92.4, "Rent Index": 88.5, "Groceries Index": 94.1, "Restaurant Price Index": 90.2, "Local Purchasing Power": 102.5},
        {"City": "Seattle", "Country": "USA", "Region": "North America", "Cost of Living Index": 89.8, "Rent Index": 75.4, "Groceries Index": 92.1, "Restaurant Price Index": 85.2, "Local Purchasing Power": 106.5},
        {"City": "Boston", "Country": "USA", "Region": "North America", "Cost of Living Index": 90.1, "Rent Index": 85.2, "Groceries Index": 91.5, "Restaurant Price Index": 88.4, "Local Purchasing Power": 101.2},
        {"City": "Washington DC", "Country": "USA", "Region": "North America", "Cost of Living Index": 88.2, "Rent Index": 82.1, "Groceries Index": 89.5, "Restaurant Price Index": 86.2, "Local Purchasing Power": 104.1},
        {"City": "Miami", "Country": "USA", "Region": "North America", "Cost of Living Index": 88.5, "Rent Index": 82.1, "Groceries Index": 89.4, "Restaurant Price Index": 85.6, "Local Purchasing Power": 92.1},
        {"City": "Chicago", "Country": "USA", "Region": "North America", "Cost of Living Index": 86.2, "Rent Index": 70.4, "Groceries Index": 85.3, "Restaurant Price Index": 82.1, "Local Purchasing Power": 105.4},
        {"City": "Austin", "Country": "USA", "Region": "North America", "Cost of Living Index": 78.5, "Rent Index": 65.2, "Groceries Index": 75.4, "Restaurant Price Index": 72.1, "Local Purchasing Power": 110.2},
        {"City": "Vancouver", "Country": "Canada", "Region": "North America", "Cost of Living Index": 78.2, "Rent Index": 62.5, "Groceries Index": 76.4, "Restaurant Price Index": 72.1, "Local Purchasing Power": 84.2},
        {"City": "Toronto", "Country": "Canada", "Region": "North America", "Cost of Living Index": 75.4, "Rent Index": 50.2, "Groceries Index": 72.1, "Restaurant Price Index": 70.5, "Local Purchasing Power": 88.4},
        {"City": "Montreal", "Country": "Canada", "Region": "North America", "Cost of Living Index": 70.2, "Rent Index": 42.5, "Groceries Index": 68.5, "Restaurant Price Index": 65.2, "Local Purchasing Power": 85.1},
        {"City": "Mexico City", "Country": "Mexico", "Region": "North America", "Cost of Living Index": 40.5, "Rent Index": 20.5, "Groceries Index": 38.2, "Restaurant Price Index": 35.4, "Local Purchasing Power": 40.1},

        # --- Europe ---
        {"City": "Zurich", "Country": "Switzerland", "Region": "Europe", "Cost of Living Index": 128.5, "Rent Index": 68.2, "Groceries Index": 129.4, "Restaurant Price Index": 125.6, "Local Purchasing Power": 118.3},
        {"City": "Geneva", "Country": "Switzerland", "Region": "Europe", "Cost of Living Index": 124.2, "Rent Index": 72.5, "Groceries Index": 122.1, "Restaurant Price Index": 120.4, "Local Purchasing Power": 115.2},
        {"City": "Reykjavik", "Country": "Iceland", "Region": "Europe", "Cost of Living Index": 105.2, "Rent Index": 55.4, "Groceries Index": 102.1, "Restaurant Price Index": 108.5, "Local Purchasing Power": 85.2},
        {"City": "Oslo", "Country": "Norway", "Region": "Europe", "Cost of Living Index": 95.4, "Rent Index": 45.2, "Groceries Index": 90.1, "Restaurant Price Index": 92.5, "Local Purchasing Power": 95.2},
        {"City": "London", "Country": "UK", "Region": "Europe", "Cost of Living Index": 87.2, "Rent Index": 75.1, "Groceries Index": 70.5, "Restaurant Price Index": 92.1, "Local Purchasing Power": 85.4},
        {"City": "Copenhagen", "Country": "Denmark", "Region": "Europe", "Cost of Living Index": 88.5, "Rent Index": 42.1, "Groceries Index": 75.4, "Restaurant Price Index": 95.2, "Local Purchasing Power": 98.4},
        {"City": "Paris", "Country": "France", "Region": "Europe", "Cost of Living Index": 82.1, "Rent Index": 42.5, "Groceries Index": 78.3, "Restaurant Price Index": 80.2, "Local Purchasing Power": 80.5},
        {"City": "Dublin", "Country": "Ireland", "Region": "Europe", "Cost of Living Index": 80.2, "Rent Index": 65.4, "Groceries Index": 65.2, "Restaurant Price Index": 82.1, "Local Purchasing Power": 88.5},
        {"City": "Amsterdam", "Country": "Netherlands", "Region": "Europe", "Cost of Living Index": 78.5, "Rent Index": 55.2, "Groceries Index": 68.4, "Restaurant Price Index": 75.2, "Local Purchasing Power": 90.2},
        {"City": "Helsinki", "Country": "Finland", "Region": "Europe", "Cost of Living Index": 76.2, "Rent Index": 38.5, "Groceries Index": 70.1, "Restaurant Price Index": 78.2, "Local Purchasing Power": 92.5},
        {"City": "Stockholm", "Country": "Sweden", "Region": "Europe", "Cost of Living Index": 75.2, "Rent Index": 38.5, "Groceries Index": 68.2, "Restaurant Price Index": 70.4, "Local Purchasing Power": 92.1},
        {"City": "Munich", "Country": "Germany", "Region": "Europe", "Cost of Living Index": 72.4, "Rent Index": 40.2, "Groceries Index": 62.5, "Restaurant Price Index": 68.4, "Local Purchasing Power": 102.1},
        {"City": "Berlin", "Country": "Germany", "Region": "Europe", "Cost of Living Index": 68.5, "Rent Index": 35.4, "Groceries Index": 58.2, "Restaurant Price Index": 62.1, "Local Purchasing Power": 98.5},
        {"City": "Vienna", "Country": "Austria", "Region": "Europe", "Cost of Living Index": 69.2, "Rent Index": 36.5, "Groceries Index": 62.1, "Restaurant Price Index": 65.4, "Local Purchasing Power": 95.2},
        {"City": "Rome", "Country": "Italy", "Region": "Europe", "Cost of Living Index": 68.2, "Rent Index": 35.4, "Groceries Index": 60.1, "Restaurant Price Index": 65.2, "Local Purchasing Power": 62.5},
        {"City": "Milan", "Country": "Italy", "Region": "Europe", "Cost of Living Index": 70.5, "Rent Index": 40.2, "Groceries Index": 62.5, "Restaurant Price Index": 68.2, "Local Purchasing Power": 65.4},
        {"City": "Barcelona", "Country": "Spain", "Region": "Europe", "Cost of Living Index": 62.5, "Rent Index": 38.2, "Groceries Index": 54.2, "Restaurant Price Index": 60.1, "Local Purchasing Power": 72.5},
        {"City": "Madrid", "Country": "Spain", "Region": "Europe", "Cost of Living Index": 60.2, "Rent Index": 32.5, "Groceries Index": 52.1, "Restaurant Price Index": 58.4, "Local Purchasing Power": 75.2},
        {"City": "Lisbon", "Country": "Portugal", "Region": "Europe", "Cost of Living Index": 55.4, "Rent Index": 45.2, "Groceries Index": 48.5, "Restaurant Price Index": 52.1, "Local Purchasing Power": 55.2},
        {"City": "Athens", "Country": "Greece", "Region": "Europe", "Cost of Living Index": 58.2, "Rent Index": 28.5, "Groceries Index": 50.1, "Restaurant Price Index": 55.2, "Local Purchasing Power": 45.2},
        {"City": "Prague", "Country": "Czech Republic", "Region": "Europe", "Cost of Living Index": 52.1, "Rent Index": 28.5, "Groceries Index": 45.2, "Restaurant Price Index": 42.1, "Local Purchasing Power": 65.4},
        {"City": "Warsaw", "Country": "Poland", "Region": "Europe", "Cost of Living Index": 48.5, "Rent Index": 25.4, "Groceries Index": 38.2, "Restaurant Price Index": 40.5, "Local Purchasing Power": 68.2},
        {"City": "Budapest", "Country": "Hungary", "Region": "Europe", "Cost of Living Index": 45.2, "Rent Index": 22.1, "Groceries Index": 38.5, "Restaurant Price Index": 38.2, "Local Purchasing Power": 52.1},
        {"City": "Bucharest", "Country": "Romania", "Region": "Europe", "Cost of Living Index": 42.1, "Rent Index": 20.5, "Groceries Index": 36.2, "Restaurant Price Index": 35.4, "Local Purchasing Power": 48.5},

        # --- Asia ---
        {"City": "Singapore", "Country": "Singapore", "Region": "Asia", "Cost of Living Index": 85.9, "Rent Index": 90.5, "Groceries Index": 78.2, "Restaurant Price Index": 65.4, "Local Purchasing Power": 88.9},
        {"City": "Tokyo", "Country": "Japan", "Region": "Asia", "Cost of Living Index": 83.4, "Rent Index": 45.2, "Groceries Index": 88.1, "Restaurant Price Index": 60.5, "Local Purchasing Power": 87.6},
        {"City": "Hong Kong", "Country": "Hong Kong", "Region": "Asia", "Cost of Living Index": 82.5, "Rent Index": 85.4, "Groceries Index": 85.2, "Restaurant Price Index": 65.4, "Local Purchasing Power": 75.2},
        {"City": "Seoul", "Country": "South Korea", "Region": "Asia", "Cost of Living Index": 80.2, "Rent Index": 40.5, "Groceries Index": 95.2, "Restaurant Price Index": 55.4, "Local Purchasing Power": 85.2},
        {"City": "Osaka", "Country": "Japan", "Region": "Asia", "Cost of Living Index": 75.2, "Rent Index": 35.4, "Groceries Index": 78.5, "Restaurant Price Index": 52.1, "Local Purchasing Power": 82.5},
        {"City": "Taipei", "Country": "Taiwan", "Region": "Asia", "Cost of Living Index": 65.2, "Rent Index": 25.4, "Groceries Index": 70.5, "Restaurant Price Index": 40.2, "Local Purchasing Power": 90.5},
        {"City": "Shanghai", "Country": "China", "Region": "Asia", "Cost of Living Index": 55.4, "Rent Index": 35.2, "Groceries Index": 50.1, "Restaurant Price Index": 45.2, "Local Purchasing Power": 60.5},
        {"City": "Beijing", "Country": "China", "Region": "Asia", "Cost of Living Index": 52.1, "Rent Index": 38.5, "Groceries Index": 48.2, "Restaurant Price Index": 42.1, "Local Purchasing Power": 58.2},
        {"City": "Shenzhen", "Country": "China", "Region": "Asia", "Cost of Living Index": 50.5, "Rent Index": 32.1, "Groceries Index": 48.5, "Restaurant Price Index": 40.2, "Local Purchasing Power": 55.4},
        {"City": "Bangkok", "Country": "Thailand", "Region": "Asia", "Cost of Living Index": 45.2, "Rent Index": 22.1, "Groceries Index": 48.5, "Restaurant Price Index": 30.2, "Local Purchasing Power": 35.2},
        {"City": "Phuket", "Country": "Thailand", "Region": "Asia", "Cost of Living Index": 42.1, "Rent Index": 20.5, "Groceries Index": 45.2, "Restaurant Price Index": 28.5, "Local Purchasing Power": 30.2},
        {"City": "Jakarta", "Country": "Indonesia", "Region": "Asia", "Cost of Living Index": 39.2, "Rent Index": 18.5, "Groceries Index": 38.1, "Restaurant Price Index": 22.5, "Local Purchasing Power": 28.4},
        {"City": "Bali", "Country": "Indonesia", "Region": "Asia", "Cost of Living Index": 38.5, "Rent Index": 25.2, "Groceries Index": 36.4, "Restaurant Price Index": 25.1, "Local Purchasing Power": 22.5},
        {"City": "Kuala Lumpur", "Country": "Malaysia", "Region": "Asia", "Cost of Living Index": 38.5, "Rent Index": 16.2, "Groceries Index": 35.4, "Restaurant Price Index": 25.2, "Local Purchasing Power": 65.2},
        {"City": "Manila", "Country": "Philippines", "Region": "Asia", "Cost of Living Index": 37.5, "Rent Index": 19.2, "Groceries Index": 35.4, "Restaurant Price Index": 24.1, "Local Purchasing Power": 26.5},
        {"City": "Ho Chi Minh City", "Country": "Vietnam", "Region": "Asia", "Cost of Living Index": 36.2, "Rent Index": 18.5, "Groceries Index": 34.2, "Restaurant Price Index": 22.1, "Local Purchasing Power": 28.5},
        {"City": "Hanoi", "Country": "Vietnam", "Region": "Asia", "Cost of Living Index": 35.4, "Rent Index": 15.2, "Groceries Index": 32.1, "Restaurant Price Index": 20.5, "Local Purchasing Power": 25.4},
        {"City": "Bangalore", "Country": "India", "Region": "Asia", "Cost of Living Index": 29.1, "Rent Index": 14.2, "Groceries Index": 27.5, "Restaurant Price Index": 21.5, "Local Purchasing Power": 58.2},
        {"City": "Mumbai", "Country": "India", "Region": "Asia", "Cost of Living Index": 28.5, "Rent Index": 15.2, "Groceries Index": 26.4, "Restaurant Price Index": 22.1, "Local Purchasing Power": 55.4},
        {"City": "Delhi", "Country": "India", "Region": "Asia", "Cost of Living Index": 27.2, "Rent Index": 12.5, "Groceries Index": 25.1, "Restaurant Price Index": 20.5, "Local Purchasing Power": 52.1},
        {"City": "Karachi", "Country": "Pakistan", "Region": "Asia", "Cost of Living Index": 22.5, "Rent Index": 8.5, "Groceries Index": 20.1, "Restaurant Price Index": 18.5, "Local Purchasing Power": 25.4},

        # --- Middle East ---
        {"City": "Tel Aviv", "Country": "Israel", "Region": "Middle East", "Cost of Living Index": 88.5, "Rent Index": 58.2, "Groceries Index": 82.1, "Restaurant Price Index": 92.5, "Local Purchasing Power": 82.1},
        {"City": "Dubai", "Country": "UAE", "Region": "Middle East", "Cost of Living Index": 65.4, "Rent Index": 55.2, "Groceries Index": 52.1, "Restaurant Price Index": 68.4, "Local Purchasing Power": 105.2},
        {"City": "Abu Dhabi", "Country": "UAE", "Region": "Middle East", "Cost of Living Index": 62.1, "Rent Index": 48.5, "Groceries Index": 50.2, "Restaurant Price Index": 62.1, "Local Purchasing Power": 102.5},
        {"City": "Doha", "Country": "Qatar", "Region": "Middle East", "Cost of Living Index": 60.5, "Rent Index": 52.1, "Groceries Index": 55.4, "Restaurant Price Index": 65.2, "Local Purchasing Power": 108.5},
        {"City": "Riyadh", "Country": "Saudi Arabia", "Region": "Middle East", "Cost of Living Index": 52.4, "Rent Index": 25.2, "Groceries Index": 48.5, "Restaurant Price Index": 45.2, "Local Purchasing Power": 85.4},
        {"City": "Istanbul", "Country": "Turkey", "Region": "Middle East", "Cost of Living Index": 32.4, "Rent Index": 14.2, "Groceries Index": 28.5, "Restaurant Price Index": 25.4, "Local Purchasing Power": 32.1},

        # --- South America ---
        {"City": "Santiago", "Country": "Chile", "Region": "South America", "Cost of Living Index": 45.2, "Rent Index": 25.4, "Groceries Index": 42.1, "Restaurant Price Index": 40.5, "Local Purchasing Power": 42.5},
        {"City": "Sao Paulo", "Country": "Brazil", "Region": "South America", "Cost of Living Index": 42.5, "Rent Index": 22.1, "Groceries Index": 38.5, "Restaurant Price Index": 35.4, "Local Purchasing Power": 32.5},
        {"City": "Rio de Janeiro", "Country": "Brazil", "Region": "South America", "Cost of Living Index": 40.2, "Rent Index": 20.5, "Groceries Index": 36.4, "Restaurant Price Index": 32.1, "Local Purchasing Power": 30.2},
        {"City": "Buenos Aires", "Country": "Argentina", "Region": "South America", "Cost of Living Index": 35.1, "Rent Index": 12.5, "Groceries Index": 30.2, "Restaurant Price Index": 32.1, "Local Purchasing Power": 38.5},
        {"City": "Lima", "Country": "Peru", "Region": "South America", "Cost of Living Index": 34.2, "Rent Index": 18.5, "Groceries Index": 32.1, "Restaurant Price Index": 28.5, "Local Purchasing Power": 28.2},
        {"City": "Bogota", "Country": "Colombia", "Region": "South America", "Cost of Living Index": 30.5, "Rent Index": 15.2, "Groceries Index": 28.5, "Restaurant Price Index": 22.1, "Local Purchasing Power": 25.4},

        # --- Africa ---
        {"City": "Johannesburg", "Country": "South Africa", "Region": "Africa", "Cost of Living Index": 39.5, "Rent Index": 15.2, "Groceries Index": 34.5, "Restaurant Price Index": 32.1, "Local Purchasing Power": 78.2},
        {"City": "Cape Town", "Country": "South Africa", "Region": "Africa", "Cost of Living Index": 38.2, "Rent Index": 18.5, "Groceries Index": 32.1, "Restaurant Price Index": 34.2, "Local Purchasing Power": 75.4},
        {"City": "Lagos", "Country": "Nigeria", "Region": "Africa", "Cost of Living Index": 35.4, "Rent Index": 25.2, "Groceries Index": 38.5, "Restaurant Price Index": 30.2, "Local Purchasing Power": 15.2},
        {"City": "Nairobi", "Country": "Kenya", "Region": "Africa", "Cost of Living Index": 32.1, "Rent Index": 14.5, "Groceries Index": 30.2, "Restaurant Price Index": 25.4, "Local Purchasing Power": 18.5},
        {"City": "Casablanca", "Country": "Morocco", "Region": "Africa", "Cost of Living Index": 30.5, "Rent Index": 12.5, "Groceries Index": 28.5, "Restaurant Price Index": 25.2, "Local Purchasing Power": 22.5},
        {"City": "Cairo", "Country": "Egypt", "Region": "Africa", "Cost of Living Index": 28.5, "Rent Index": 10.2, "Groceries Index": 25.4, "Restaurant Price Index": 22.1, "Local Purchasing Power": 20.5},

        # --- Oceania ---
        {"City": "Sydney", "Country": "Australia", "Region": "Oceania", "Cost of Living Index": 84.3, "Rent Index": 55.4, "Groceries Index": 81.2, "Restaurant Price Index": 75.3, "Local Purchasing Power": 95.2},
        {"City": "Melbourne", "Country": "Australia", "Region": "Oceania", "Cost of Living Index": 80.5, "Rent Index": 48.2, "Groceries Index": 78.5, "Restaurant Price Index": 70.2, "Local Purchasing Power": 92.5},
        {"City": "Auckland", "Country": "New Zealand", "Region": "Oceania", "Cost of Living Index": 78.2, "Rent Index": 45.2, "Groceries Index": 75.4, "Restaurant Price Index": 72.1, "Local Purchasing Power": 85.4},
        {"City": "Brisbane", "Country": "Australia", "Region": "Oceania", "Cost of Living Index": 76.5, "Rent Index": 45.2, "Groceries Index": 75.2, "Restaurant Price Index": 68.5, "Local Purchasing Power": 90.5},
        {"City": "Perth", "Country": "Australia", "Region": "Oceania", "Cost of Living Index": 75.8, "Rent Index": 42.5, "Groceries Index": 74.1, "Restaurant Price Index": 68.2, "Local Purchasing Power": 94.2},
        {"City": "Wellington", "Country": "New Zealand", "Region": "Oceania", "Cost of Living Index": 75.2, "Rent Index": 40.5, "Groceries Index": 72.5, "Restaurant Price Index": 68.5, "Local Purchasing Power": 82.5},
    ]

# --- Main App Layout ---

st.title("🌍 Global Cost of Living Comparator")
st.markdown("Compare cost of living indices across **75+ major cities** worldwide. Base Reference: New York City = 100.")

# Load Data
df = pd.DataFrame(get_expanded_data())

# --- Sidebar Controls ---
st.sidebar.header("Filter Settings")

# 1. Region Filter
all_regions = sorted(df['Region'].unique())
selected_regions = st.sidebar.multiselect(
    "1. Select Regions",
    options=all_regions,
    default=all_regions
)

# Filter dataframe by region first
region_filtered_df = df[df['Region'].isin(selected_regions)]

# 2. City Filter
if not region_filtered_df.empty:
    all_cities = sorted(region_filtered_df['City'].unique())
    
    # Default selection logic
    default_cities = ["New York", "London", "Tokyo", "Mumbai", "Zurich", "Sydney", "Cape Town", "Buenos Aires"]
    valid_defaults = [c for c in default_cities if c in all_cities]
    
    selected_cities = st.sidebar.multiselect(
        "2. Select Cities to Compare",
        options=all_cities,
        default=valid_defaults if valid_defaults else all_cities[:5]
    )
else:
    selected_cities = []
    st.sidebar.warning("No regions selected.")

# 3. Metric Selection
metrics = [
    "Cost of Living Index", 
    "Rent Index", 
    "Groceries Index", 
    "Restaurant Price Index", 
    "Local Purchasing Power"
]
selected_metric = st.sidebar.selectbox("3. Primary Metric for Ranking", metrics)

st.sidebar.divider()
st.sidebar.info(f"Showing data for {len(selected_cities)} cities.")

# Filter dataframe based on city selection
if selected_cities:
    filtered_df = df[df['City'].isin(selected_cities)]
else:
    filtered_df = pd.DataFrame() # Empty if nothing selected

# --- Main Content ---

if not filtered_df.empty:
    # --- Key Metrics Row ---
    st.subheader("At a Glance")
    
    col1, col2, col3 = st.columns(3)
    
    # Find city with highest and lowest cost in selection
    highest_city = filtered_df.loc[filtered_df[selected_metric].idxmax()]
    lowest_city = filtered_df.loc[filtered_df[selected_metric].idxmin()]
    
    # Calculate average
    avg_val = filtered_df[selected_metric].mean()

    with col1:
        st.metric(
            label=f"Highest {selected_metric}",
            value=f"{highest_city[selected_metric]:.1f}",
            delta=highest_city['City'],
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            label=f"Lowest {selected_metric}",
            value=f"{lowest_city[selected_metric]:.1f}",
            delta=lowest_city['City']
        )
        
    with col3:
        st.metric(
            label="Average (Selected Cities)",
            value=f"{avg_val:.1f}",
            help="Mean value of the selected metric for the currently filtered cities."
        )

    st.divider()

    # --- Charts ---
    
    # 1. Bar Chart
    st.subheader(f"City Comparison: {selected_metric}")
    
    # Sort for better visualization
    sorted_df = filtered_df.sort_values(by=selected_metric, ascending=False)
    
    fig_bar = px.bar(
        sorted_df,
        x=selected_metric,
        y="City",
        orientation='h',
        color="Region",
        text=selected_metric,
        hover_data=["Country", "Region"],
        height=max(400, len(selected_cities) * 30) # Dynamic height
    )
    fig_bar.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    fig_bar.update_layout(yaxis=dict(autorange="reversed")) # Highest on top
    st.plotly_chart(fig_bar, use_container_width=True)

    # 2. Scatter Plot (Correlation)
    st.subheader("Correlation: Cost of Living vs. Purchasing Power")
    st.markdown("Does a higher cost of living imply higher local purchasing power?")
    
    fig_scatter = px.scatter(
        filtered_df,
        x="Cost of Living Index",
        y="Local Purchasing Power",
        size="Rent Index", # Bubble size based on Rent
        color="Region",
        hover_name="City",
        text="City",
        size_max=40
    )
    fig_scatter.update_traces(textposition='top center')
    st.plotly_chart(fig_scatter, use_container_width=True)

    # --- Data Table ---
    with st.expander("View Raw Data Table"):
        # Removed background_gradient to avoid matplotlib dependency
        st.dataframe(
            filtered_df,
            use_container_width=True
        )

else:
    st.info("Please select at least one city from the sidebar to view the dashboard.")