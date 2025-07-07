import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load dataset
df = pd.read_csv('world-happiness-report-2021.csv')

# Create 2x2 subplots with increased spacing
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Happiness Score vs GDP per Capita", "Happiness Score by Region",
                    "Happiness Score vs Life Expectancy", "Happiness Score vs Corruption"),
    horizontal_spacing=0.25,  # Increased horizontal spacing
    vertical_spacing=0.2     # Increased vertical spacing
)

# Scatter: Happiness vs GDP
fig.add_trace(
    go.Scatter(
        x=df['Logged GDP per capita'], y=df['Ladder score'], mode='markers',
        text=df['Country name'], marker=dict(size=10, color=df['Ladder score'], colorscale='Viridis')
    ),
    row=1, col=1
)

# Bar: Happiness by Region (remove text labels, use hover instead)
region_avg = df.groupby('Regional indicator')['Ladder score'].mean().sort_values()
fig.add_trace(
    go.Bar(x=region_avg.values, y=region_avg.index, orientation='h', textposition='none',
           hovertemplate='Region: %{y}<br>Happiness Score: %{x:.2f}<extra></extra>'),
    row=1, col=2
)

# Scatter: Life Expectancy vs Happiness
fig.add_trace(
    go.Scatter(
        x=df['Healthy life expectancy'], y=df['Ladder score'], mode='markers',
        text=df['Country name'], marker=dict(size=10, color=df['Ladder score'], colorscale='Viridis')
    ),
    row=2, col=1
)

# Scatter: Corruption vs Happiness
fig.add_trace(
    go.Scatter(
        x=df['Perceptions of corruption'], y=df['Ladder score'], mode='markers',
        text=df['Country name'], marker=dict(size=10, color=df['Ladder score'], colorscale='Viridis')
    ),
    row=2, col=2
)

# Update layout with adjusted margins and size
fig.update_layout(
    title_text="World Happiness Dashboard 2021",
    showlegend=False,
    height=900, width=1300,  # Increased size for better spacing
    margin=dict(l=80, r=80, t=120, b=80)  # Increased margins for separation
)
fig.update_xaxes(title_text="GDP per Capita", row=1, col=1)
fig.update_xaxes(title_text="Healthy Life Expectancy", row=2, col=1)
fig.update_xaxes(title_text="Perceptions of Corruption", row=2, col=2)
fig.update_yaxes(title_text="Happiness Score", row=1, col=1)
fig.update_yaxes(title_text="Happiness Score", row=2, col=1)
fig.update_yaxes(title_text="Happiness Score", row=2, col=2)

# Save and show
fig.write_html('happiness_dashboard.html')
fig.show()