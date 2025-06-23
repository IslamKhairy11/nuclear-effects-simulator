# app.py (Final Version with Theme-Aware Styling)

import streamlit as st
import pandas as pd
import folium
import requests
from streamlit_folium import st_folium
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Import data and LLM function from other files
from data import BOMB_DATA
from llm import get_safety_recommendations

# --- 1. APP CONFIGURATION & INITIALIZATION ---
st.set_page_config(
    page_title="Nuclear Bomb Visualizer",
    page_icon="☢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Autocomplete & Session State Management ---
if 'GEOAPIFY_API_KEY' not in st.secrets:
    st.error("Geoapify API key not found! Please add it to your .streamlit/secrets.toml file.")
    st.stop()
API_KEY = st.secrets["GEOAPIFY_API_KEY"]

geolocator = Nominatim(user_agent="nuclear_bomb_visualizer_app_v8")

# Initialize session state
if 'target_lat' not in st.session_state:
    st.session_state.update({
        'target_lat': 40.7128, 'target_lon': -74.0060,
        'user_lat': 40.7580, 'user_lon': -73.9855,
        'map_center': [40.7128, -74.0060], 'map_zoom': 10,
        'det_suggestions': [], 'user_suggestions': [],
        'det_query': "", 'user_query': ""
    })

# --- Helper Functions for Autocomplete ---
def fetch_suggestions(location_type):
    query_key = f"{location_type}_query"
    suggestions_key = f"{location_type}_suggestions"
    query = st.session_state[query_key]
    if len(query) < 3:
        st.session_state[suggestions_key] = []
        return
    url = f"https://api.geoapify.com/v1/geocode/autocomplete?text={query}&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.session_state[suggestions_key] = response.json().get('features', [])
        else:
            st.session_state[suggestions_key] = []
    except requests.RequestException:
        st.session_state[suggestions_key] = []

def on_suggestion_click(suggestion, location_type):
    coords = suggestion['geometry']['coordinates']
    if location_type == 'det':
        st.session_state.target_lon, st.session_state.target_lat = coords[0], coords[1]
        st.session_state.map_center = [coords[1], coords[0]]
        st.session_state.det_suggestions = []
        st.session_state.det_query = ""
    else:
        st.session_state.user_lon, st.session_state.user_lat = coords[0], coords[1]
        st.session_state.user_suggestions = []
        st.session_state.user_query = ""

# --- 2. SIDEBAR (USER INPUTS) ---
st.sidebar.title("Simulation Controls 🕹️")
st.sidebar.markdown("Set the detonation scenario using the options below.")
selected_bomb = st.sidebar.selectbox("Select Bomb Type:", list(BOMB_DATA.keys()))

st.sidebar.subheader("📍 Set Detonation Point")
st.sidebar.text_input("Search for a location", key="det_query", on_change=fetch_suggestions, args=("det",))
det_suggestions_container = st.sidebar.container()
for suggestion in st.session_state.det_suggestions:
    det_suggestions_container.button(
        suggestion['properties']['formatted'], key=f"det_{suggestion['properties']['place_id']}",
        on_click=on_suggestion_click, args=(suggestion, "det"), use_container_width=True
    )

st.sidebar.subheader("👤 Set Your Location")
st.sidebar.text_input("Search for your location", key="user_query", on_change=fetch_suggestions, args=("user",))
user_suggestions_container = st.sidebar.container()
for suggestion in st.session_state.user_suggestions:
    user_suggestions_container.button(
        suggestion['properties']['formatted'], key=f"user_{suggestion['properties']['place_id']}",
        on_click=on_suggestion_click, args=(suggestion, "user"), use_container_width=True
    )

st.sidebar.info("💡 **Pro Tip:** You can also click and drag markers on the map.")
st.sidebar.divider()
st.sidebar.markdown(
    "<a href='/Information' target='_blank' style='text-decoration: none; color: var(--primary);'>ℹ️ Learn about Terminology & Bombs</a>",
    unsafe_allow_html=True
)


# --- 3. DATA PROCESSING & ANALYSIS ---
bomb_info = BOMB_DATA[selected_bomb]
effects = bomb_info['effects']
sorted_effects = sorted(effects.items(), key=lambda item: item[1]['radius_m'], reverse=True)
detonation_point = (st.session_state.target_lat, st.session_state.target_lon)
user_point = (st.session_state.user_lat, st.session_state.user_lon)
user_distance_m = geodesic(detonation_point, user_point).meters
user_effect_zone = "Outside all immediate impact radii"
for effect_name, details in sorted(effects.items(), key=lambda item: item[1]['radius_m']):
    if user_distance_m <= details['radius_m']:
        user_effect_zone = effect_name
        break
recommendations = get_safety_recommendations(user_effect_zone)

# --- 4. MAIN PAGE LAYOUT ---
st.title(f"☢️ Nuclear Detonation Effects: {selected_bomb}")
st.markdown(f"Visualizing a **{bomb_info['yield_kt']} kiloton** yield detonation.")

# --- MAP (FULL WIDTH) ---
m = folium.Map(location=st.session_state.map_center, zoom_start=st.session_state.map_zoom, tiles="CartoDB dark_matter")
for name, details in sorted_effects:
    folium.Circle(location=detonation_point, radius=details['radius_m'],
                  color=f"#{details['color'][0]:02x}{details['color'][1]:02x}{details['color'][2]:02x}",
                  fill=True, fill_opacity=0.3).add_to(m)
folium.Marker(location=detonation_point, popup="Ground Zero", tooltip="Ground Zero (Drag Me!)",
              icon=folium.Icon(color="red", icon="radiation", prefix='fa'), draggable=True).add_to(m)
folium.Marker(location=user_point, popup="Your Location", tooltip="Your Location (Drag Me!)",
              icon=folium.Icon(color="green", icon="user", prefix='fa'), draggable=True).add_to(m)

map_key = f"{selected_bomb}-{st.session_state.target_lat}-{st.session_state.target_lon}"
map_data = st_folium(m, key=map_key, width='100%', height=600, returned_objects=["all_drawings", "center", "zoom"])

if map_data:
    st.session_state.map_center = [map_data["center"]["lat"], map_data["center"]["lng"]]
    st.session_state.map_zoom = map_data["zoom"]
    if map_data.get("all_drawings"):
        needs_rerun = False
        for feature in map_data["all_drawings"]:
            lon, lat = feature["geometry"]["coordinates"]
            popup_text = feature.get("properties", {}).get("popup", "")
            if popup_text == "Ground Zero" and (abs(st.session_state.target_lat - lat) > 1e-6 or abs(st.session_state.target_lon - lon) > 1e-6):
                st.session_state.target_lat, st.session_state.target_lon = lat, lon
                needs_rerun = True
            elif popup_text == "Your Location" and (abs(st.session_state.user_lat - lat) > 1e-6 or abs(st.session_state.user_lon - lon) > 1e-6):
                st.session_state.user_lat, st.session_state.user_lon = lat, lon
                needs_rerun = True
        if needs_rerun:
            st.rerun()

# --- HORIZONTAL LEGEND (BELOW MAP) ---
st.divider()
st.header("💥 Effect Legend")
st.markdown("Radii shown are for an airburst. Effects vary based on terrain and weather.")
legend_cols = st.columns(len(sorted_effects))
for i, (name, details) in enumerate(sorted_effects):
    with legend_cols[i]:
        color_hex = f"#{details['color'][0]:02x}{details['color'][1]:02x}{details['color'][2]:02x}"
        radius_km = details['radius_m'] / 1000
        description = BOMB_DATA[selected_bomb]['effects'][name]['description']
        # --- THEME-AWARE FIX IS HERE ---
        st.markdown(f"""
        <div style="color: var(--text-color); border-left: 10px solid {color_hex}; padding-left: 10px; height: 100%;">
            <strong style="font-size: 1.1em;">{name}</strong><br>
            <span style="font-size: 0.9em;">Radius: <strong>{radius_km:.2f} km</strong></span><br>
            <small>{description}</small>
        </div>
        """, unsafe_allow_html=True)

# --- INFORMATION SECTION (BELOW LEGEND) ---
st.divider()
info_col1, info_col2 = st.columns(2, gap="large")
with info_col1:
    st.header("📍 Selected Locations")
    try:
        det_loc_name = geolocator.reverse(detonation_point, exactly_one=True, timeout=10)
        # --- THEME-AWARE FIX IS HERE ---
        st.markdown(f"<div style='color: var(--text-color);'><strong>Detonation Point:</strong><br>{det_loc_name.address}</div>", unsafe_allow_html=True)
    except Exception:
        st.markdown(f"<div style='color: var(--text-color);'><strong>Detonation Point:</strong><br>{st.session_state.target_lat:.4f}, {st.session_state.target_lon:.4f}</div>", unsafe_allow_html=True)
    st.markdown("") # Vertical space
    try:
        user_loc_name = geolocator.reverse(user_point, exactly_one=True, timeout=10)
        # --- THEME-AWARE FIX IS HERE ---
        st.markdown(f"<div style='color: var(--text-color);'><strong>Your Location:</strong><br>{user_loc_name.address}</div>", unsafe_allow_html=True)
    except Exception:
        st.markdown(f"<div style='color: var(--text-color);'><strong>Your Location:</strong><br>{st.session_state.user_lat:.4f}, {st.session_state.user_lon:.4f}</div>", unsafe_allow_html=True)
with info_col2:
    st.header("👤 Your Situation")
    st.metric("Distance from Ground Zero", f"{user_distance_m / 1000:.2f} km")
    st.subheader(f"Impact Zone: `{user_effect_zone}`")
    with st.expander("**Click here for safety recommendations**"):
        st.markdown(recommendations)

# --- FOOTER ---
st.divider()
linkedin_url = "https://www.linkedin.com/in/ikhairy11/"
# --- THEME-AWARE FIX IS HERE ---
footer_html = f"""
<div style="text-align: center; padding: 1rem 0;">
    <p>Built by Islam Khairy | <a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: var(--primary);">:linkedin: View my LinkedIn Profile</a></p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)