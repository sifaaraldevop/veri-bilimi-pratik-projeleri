import streamlit as st
import plotly.graph_objects as go

# Function to create spheres
def spheres(diameter, color, distance):
    return go.Scatter3d(
        x=[distance],
        y=[0],
        z=[0],
        mode='markers',
        marker=dict(size=diameter, color=color, opacity=0.8),
        name='Planet'
    )

# Function to create orbits
def orbits(distance, color='#ffffff', width=1):
    return go.Scatter3d(
        x=[distance],
        y=[0],
        z=[0],
        mode='lines',
        line=dict(color=color, width=width),
        name='Orbit'
    )

# Function to create annotations
def annot(x, y, text, xancr='center'):
    return dict(
        x=x,
        y=y,
        text=text,
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        xanchor=xancr
    )

# Diameter and distance data
diameter_km = [200000, 4878, 12104, 12756, 6787, 142796, 120660, 51118, 48600]
diameter = [((i / 12756) * 2) for i in diameter_km]
distance_from_sun = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]

# Create spheres for the Sun and planets
trace0 = spheres(diameter[0], '#ffff00', distance_from_sun[0])  # Sun
trace1 = spheres(diameter[1], '#87877d', distance_from_sun[1])  # Mercury
trace2 = spheres(diameter[2], '#d23100', distance_from_sun[2])  # Venus
trace3 = spheres(diameter[3], '#325bff', distance_from_sun[3])  # Earth
trace4 = spheres(diameter[4], '#b20000', distance_from_sun[4])  # Mars
trace5 = spheres(diameter[5], '#ebebd2', distance_from_sun[5])  # Jupiter
trace6 = spheres(diameter[6], '#ebcd82', distance_from_sun[6])  # Saturn
trace7 = spheres(diameter[7], '#37ffda', distance_from_sun[7])  # Uranus
trace8 = spheres(diameter[8], '#2500ab', distance_from_sun[8])  # Neptune

# Set up orbit traces
trace11 = orbits(distance_from_sun[1])  # Mercury
trace12 = orbits(distance_from_sun[2])  # Venus
trace13 = orbits(distance_from_sun[3])  # Earth
trace14 = orbits(distance_from_sun[4])  # Mars
trace15 = orbits(distance_from_sun[5])  # Jupiter
trace16 = orbits(distance_from_sun[6])  # Saturn
trace17 = orbits(distance_from_sun[7])  # Uranus
trace18 = orbits(distance_from_sun[8])  # Neptune

# Additional rings for Saturn
rings = [orbits(23 + i, '#827962', 3) for i in range(6)]

# Layout configuration
layout = go.Layout(
    title='Solar System',
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    scene=dict(
        xaxis=dict(
            title='Distance from the Sun',
            titlefont_color='black',
            range=[-7000, 7000],
            backgroundcolor='black',
            color='black',
            gridcolor='black'
        ),
        yaxis=dict(
            title='Distance from the Sun',
            titlefont_color='black',
            range=[-7000, 7000],
            backgroundcolor='black',
            color='black',
            gridcolor='black'
        ),
        zaxis=dict(
            title='',
            range=[-7000, 7000],
            backgroundcolor='black',
            color='white',
            gridcolor='black'
        ),
        annotations=[
            annot(distance_from_sun[0], 40, 'Sun', xancr='left'),
            annot(distance_from_sun[1], 5, 'Mercury'),
            annot(distance_from_sun[2], 9, 'Venus'),
            annot(distance_from_sun[3], 9, 'Earth'),
            annot(distance_from_sun[4], 7, 'Mars'),
            annot(distance_from_sun[5], 30, 'Jupiter'),
            annot(distance_from_sun[6], 28, 'Saturn'),
            annot(distance_from_sun[7], 20, 'Uranus'),
            annot(distance_from_sun[8], 20, 'Neptune'),
        ]
    )
)

# Create the figure
fig = go.Figure(data=[trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8,
                      trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18] + rings,
                layout=layout)

# Streamlit app layout
st.title('Solar System Visualization')
st.plotly_chart(fig, use_container_width=True)