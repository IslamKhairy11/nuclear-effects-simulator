# data.py (Updated with possessing country)

# Data structure:
# Key: Bomb Name
#   "yield_kt": Kilotons of TNT equivalent.
#   "possessing_country": The primary state possessing the weapon.
#   "effects": Dictionary of impact types.
#       "radius_m": The radius of the effect in meters, based on NUKEMAP models for airbursts.
#       "color": RGBA color for the map visualization.
#       "description": A brief, scientific description of the effect at this range.

BOMB_DATA = {
    "W-87 (Modern US Warhead)": {
        "yield_kt": 300,
        "possessing_country": "United States",
        "effects": {
            "Fireball": {"radius_m": 750, "color": [255, 255, 0, 150], "description": "Vaporization of materials."},
            "Heavy Blast Damage": {"radius_m": 4300, "color": [255, 0, 0, 120], "description": "Most concrete buildings destroyed."},
            "Thermal Radiation": {"radius_m": 10500, "color": [255, 165, 0, 90], "description": "Widespread 3rd-degree burns."},
            "Moderate Blast Damage": {"radius_m": 11500, "color": [0, 0, 255, 70], "description": "Residential structures collapse."},
        }
    },
    "B-61-12 (Modern US Tactical Bomb)": {
        "yield_kt": 50,
        "possessing_country": "United States",
        "effects": {
            "Fireball": {"radius_m": 350, "color": [255, 255, 0, 150], "description": "Vaporization of materials."},
            "Heavy Blast Damage": {"radius_m": 2000, "color": [255, 0, 0, 120], "description": "Most concrete buildings destroyed."},
            "Thermal Radiation": {"radius_m": 5100, "color": [255, 165, 0, 90], "description": "Widespread 3rd-degree burns."},
            "Moderate Blast Damage": {"radius_m": 6000, "color": [0, 0, 255, 70], "description": "Residential structures collapse."},
        }
    },
    "Topol-M SS-27 (Modern Russian ICBM)": {
        "yield_kt": 800,
        "possessing_country": "Russia",
        "effects": {
            "Fireball": {"radius_m": 1100, "color": [255, 255, 0, 150], "description": "Vaporization of materials."},
            "Heavy Blast Damage": {"radius_m": 7000, "color": [255, 0, 0, 120], "description": "Most concrete buildings destroyed."},
            "Thermal Radiation": {"radius_m": 16000, "color": [255, 165, 0, 90], "description": "Widespread 3rd-degree burns."},
            "Moderate Blast Damage": {"radius_m": 18000, "color": [0, 0, 255, 70], "description": "Residential structures collapse."},
        }
    },
    "DF-5 (Modern Chinese ICBM)": {
        "yield_kt": 5000, # 5 Megatons
        "possessing_country": "China",
        "effects": {
            "Fireball": {"radius_m": 2800, "color": [255, 255, 0, 150], "description": "Vaporization of materials."},
            "Heavy Blast Damage": {"radius_m": 18000, "color": [255, 0, 0, 120], "description": "Most concrete buildings destroyed."},
            "Thermal Radiation": {"radius_m": 38000, "color": [255, 165, 0, 90], "description": "Widespread 3rd-degree burns."},
            "Moderate Blast Damage": {"radius_m": 45000, "color": [0, 0, 255, 70], "description": "Residential structures collapse."},
        }
    },
    "Tsar Bomba (Largest Tested)": {
        "yield_kt": 50000, # 50 Megatons
        "possessing_country": "Soviet Union (Former)",
        "effects": {
            "Fireball": {"radius_m": 4600, "color": [255, 255, 0, 150], "description": "Vaporization of materials."},
            "Heavy Blast Damage": {"radius_m": 32000, "color": [255, 0, 0, 120], "description": "Most concrete buildings destroyed."},
            "Thermal Radiation": {"radius_m": 65000, "color": [255, 165, 0, 90], "description": "Widespread 3rd-degree burns."},
            "Moderate Blast Damage": {"radius_m": 90000, "color": [0, 0, 255, 70], "description": "Residential structures collapse."},
        }
    },
    "Little Boy (Hiroshima)": {
        "yield_kt": 15,
        "possessing_country": "United States",
        "effects": {
            "Fireball": {"radius_m": 200, "color": [255, 255, 0, 150], "description": "Vaporization of materials."},
            "Heavy Blast Damage": {"radius_m": 1600, "color": [255, 0, 0, 120], "description": "Most concrete buildings destroyed."},
            "Thermal Radiation": {"radius_m": 2500, "color": [255, 165, 0, 90], "description": "Widespread 3rd-degree burns."},
            "Moderate Blast Damage": {"radius_m": 3200, "color": [0, 0, 255, 70], "description": "Residential structures collapse."},
        }
    },
}