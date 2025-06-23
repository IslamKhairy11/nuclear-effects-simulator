# llm.py

import streamlit as st

def get_safety_recommendations(effect_name: str) -> str:
    """
    This function simulates an LLM call.
    It returns detailed, actionable safety recommendations based on the impact zone.
    """
    if effect_name == "Fireball":
        return """
        ### Zone: Fireball
        - **Impact:** Complete vaporization.
        - **Survival Chance:** Zero.
        - **Recommendation:** There are no protective actions possible within this zone.
        """
    elif effect_name == "Heavy Blast Damage":
        return """
        ### Zone: Heavy Blast Damage (5 psi)
        - **Impact:** Most buildings are demolished. A high-pressure blast wave moves faster than sound.
        - **Survival Chance:** Very low.
        - **Recommendations:**
            - **If indoors:** Do not stand near windows. Seek shelter in a basement or a structurally sound, interior room. The primary goal is to shield yourself from the collapsing structure and flying debris.
            - **If outdoors:** Immediately **drop to the ground, face down**, with your head and neck covered by your arms. If possible, get behind any solid object that might offer protection from the blast pressure.
            - **After the blast wave:** Be aware of falling structures and fires.
        """
    elif effect_name == "Thermal Radiation":
        return """
        ### Zone: Thermal Radiation (3rd-Degree Burns)
        - **Impact:** Intense heat flash lasting several seconds causes severe burns to exposed skin and can ignite fires.
        - **Survival Chance:** Moderate, if immediate action is taken.
        - **Recommendations:**
            - **IMMEDIATELY TAKE COVER.** The thermal flash travels at the speed of light. You have only a second or two.
            - **"Duck and Cover":** Drop to the ground and get behind any object that casts a shadow. A wall, a ditch, a vehicle—anything that can block the direct line of sight to the detonation will protect you from the heat.
            - **Do not look at the flash:** It will cause temporary or permanent blindness.
            - **After the flash:** Be prepared for the arrival of the blast wave, which travels slower than light.
        """
    elif effect_name == "Moderate Blast Damage":
        return """
        ### Zone: Moderate Blast Damage (1 psi)
        - **Impact:** Windows will shatter with extreme force, creating high-velocity projectiles. Some structural damage to homes is possible.
        - **Survival Chance:** High, but risk of serious injury.
        - **Recommendations:**
            - **Stay away from windows.** This is the single most important rule. The majority of injuries in this zone are from flying glass.
            - **Move to an interior room or hallway** without windows.
            - **Get under a sturdy piece of furniture** like a heavy desk or table to protect from falling debris from the ceiling.
            - **After the blast:** Be cautious of damaged structures and broken glass.
        """
    else: # Outside all radii
        return """
        ### Zone: Outside Immediate Impact Radii
        - **Impact:** You are outside the immediate zones for severe blast, thermal, and fireball effects. However, risks remain.
        - **Survival Chance:** Very high.
        - **Recommendations:**
            - **Expect Fallout:** The most significant danger at this distance is radioactive fallout, which is carried by wind and can arrive hours after the detonation.
            - **Go Indoors:** Find the most robust shelter possible. Brick or concrete buildings are best. Basements are ideal.
            - **Seal the Shelter:** Close all windows, doors, and fireplace dampers. Turn off ventilation systems.
            - **Tune In:** Use a battery-powered or hand-crank radio to listen for instructions from emergency services.
            - **Shelter in Place:** Plan to stay in your shelter for at least 24-48 hours unless told otherwise by authorities.
        """