# pages/02_ℹ️_Information.py (Updated to use use_container_width)

import streamlit as st
from data import BOMB_DATA
from PIL import Image

st.set_page_config(page_title="Information", page_icon="ℹ️", layout="wide")

st.title("ℹ️ Information & Terminology")
st.markdown("This page provides definitions for the terms used in the simulation and details about the nuclear devices.")

# --- Language Selection ---
selected_language = st.radio(
    "Select Language:",
    ["English", "العربية (Arabic)"],
    horizontal=True,
)

# --- Define Content in Both Languages ---

# Bomb name to image file mapping
IMAGE_MAP = {
    "W-87 (Modern US Warhead)": "w87.jpg",
    "B-61-12 (Modern US Tactical Bomb)": "b61.jpg",
    "Topol-M SS-27 (Modern Russian ICBM)": "topol_m.jpg",
    "DF-5 (Modern Chinese ICBM)": "df5.jpg",
    "Tsar Bomba (Largest Tested)": "tsar_bomba.jpg",
    "Little Boy (Hiroshima)": "little_boy.jpg"
}

# --- ENGLISH CONTENT ---
if selected_language == "English":
    st.header("Effect Terminology")
    
    st.subheader("🔥 Fireball")
    st.markdown("The initial, extremely hot, and luminous sphere of plasma created by a nuclear explosion. Temperatures inside the fireball can reach tens of millions of degrees Celsius, similar to the core of the sun. Everything within this radius is effectively vaporized.")

    st.subheader("💥 Heavy Blast Damage (5 psi)")
    st.markdown("This ring represents the area affected by a high-pressure blast wave of at least 5 pounds per square inch (psi). This pressure is sufficient to destroy most residential buildings and heavily damage reinforced concrete structures. Fatalities are near-universal in this zone.")

    st.subheader("🌡️ Thermal Radiation (3rd-Degree Burns)")
    st.markdown("An intense wave of heat that travels at the speed of light from the explosion. This thermal pulse can last for several seconds. At this range, it's powerful enough to cause spontaneous ignition of flammable materials (like wood, cloth, and fuel) and inflict third-degree burns on exposed skin.")

    st.subheader("💨 Moderate Blast Damage (1 psi)")
    st.markdown("The area affected by a 1 psi blast wave. While not enough to destroy most buildings, this pressure can shatter all windows, which become high-velocity projectiles. It can also cause significant damage to residential roofs and non-load-bearing walls.")

    st.divider()
    st.header("Nuclear Device Information")

    for bomb_name, details in BOMB_DATA.items():
        st.subheader(bomb_name)
        col1, col2 = st.columns([1, 3])
        
        try:
            image_path = f"assets/{IMAGE_MAP.get(bomb_name, 'default.jpg')}"
            image = Image.open(image_path)
            # --- THE FIX IS HERE ---
            col1.image(image, use_container_width=True, caption=f"Image of {bomb_name}")
        except FileNotFoundError:
            col1.warning(f"Image not found for {bomb_name}")

        col2.metric("Explosive Yield", f"{details['yield_kt']:,} kilotons")
        col2.markdown(f"**Possessing Country:** {details['possessing_country']}")
        col2.markdown(f"Equivalent to **{details['yield_kt'] * 1000:,} tons** of TNT.")
        st.divider()


# --- ARABIC CONTENT (العربية) with FULL RTL LAYOUT ---
elif selected_language == "العربية (Arabic)":
    country_translation = {
        "United States": "الولايات المتحدة", "Russia": "روسيا", "China": "الصين",
        "Soviet Union (Former)": "الاتحاد السوفيتي (سابقًا)"
    }
    
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: right;'>مصطلحات التأثير</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>🔥 كرة النار</h3>", unsafe_allow_html=True)
    st.markdown("<p>الكرة الأولية شديدة الحرارة والمضيئة من البلازما الناتجة عن انفجار نووي. يمكن أن تصل درجات الحرارة داخل كرة النار إلى عشرات الملايين من الدرجات المئوية، على غرار قلب الشمس. كل شيء داخل هذا النطاق يتبخر فعليًا.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>💥 دمار انفجاري شديد (5 رطل/بوصة مربعة)</h3>", unsafe_allow_html=True)
    st.markdown("<p>تمثل هذه الدائرة المنطقة المتأثرة بموجة انفجار عالية الضغط لا تقل عن 5 رطل لكل بوصة مربعة (psi). هذا الضغط كافٍ لتدمير معظم المباني السكنية وإلحاق أضرار جسيمة بالهياكل الخرسانية المسلحة. الوفيات شبه مؤكدة في هذه المنطقة.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>🌡️ الإشعاع الحراري (حروق من الدرجة الثالثة)</h3>", unsafe_allow_html=True)
    st.markdown("<p>موجة شديدة من الحرارة تنتقل بسرعة الضوء من الانفجار. يمكن أن تستمر هذه النبضة الحرارية لعدة ثوانٍ. في هذا النطاق، تكون قوية بما يكفي لإحداث اشتعال تلقائي للمواد القابلة للاشتعال (مثل الخشب والقماش والوقود) والتسبب في حروق من الدرجة الثالثة للجلد المكشوف.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right;'>💨 دمار انفجاري معتدل (1 رطل/بوصة مربعة)</h3>", unsafe_allow_html=True)
    st.markdown("<p>المنطقة المتأثرة بموجة انفجار بقوة 1 رطل لكل بوصة مربعة. في حين أنها ليست كافية لتدمير معظم المباني، يمكن لهذا الضغط تحطيم جميع النوافذ، التي تصبح مقذوفات عالية السرعة. كما يمكن أن يتسبب في أضرار كبيرة لأسطح المنازل والجدران غير الحاملة.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("<h2 style='direction: rtl; text-align: right;'>معلومات عن الأجهزة النووية</h2>", unsafe_allow_html=True)

    for bomb_name, details in BOMB_DATA.items():
        st.markdown(f"<h3 style='direction: rtl; text-align: right;'>{bomb_name}</h3>", unsafe_allow_html=True)
        
        text_col, image_col = st.columns([3, 1])
        
        with image_col:
            try:
                image_path = f"assets/{IMAGE_MAP.get(bomb_name, 'default.jpg')}"
                image = Image.open(image_path)
                # --- THE FIX IS HERE ---
                st.image(image, use_container_width=True, caption=f"صورة لـ {bomb_name}")
            except FileNotFoundError:
                st.warning(f"لم يتم العثور على صورة لـ {bomb_name}")

        with text_col:
            country_en = details['possessing_country']
            country_ar = country_translation.get(country_en, country_en)
            yield_kt_formatted = f"{details['yield_kt']:,}"
            tnt_equiv_formatted = f"{details['yield_kt'] * 1000:,}"

            rtl_details_html = f"""
            <div style='direction: rtl; text-align: right; height: 100%;'>
                <div style='margin-bottom: 1rem;'>
                    <p style='font-size: 0.9em; color: #666;'>القوة التفجيرية</p>
                    <p style='font-size: 1.75em; font-weight: bold; line-height: 1; margin:0;'>{yield_kt_formatted} كيلو طن</p>
                </div>
                <p><b>الدولة المالكة:</b> {country_ar}</p>
                <p>ما يعادل <b>{tnt_equiv_formatted} طن</b> من مادة تي إن تي.</p>
            </div>
            """
            st.markdown(rtl_details_html, unsafe_allow_html=True)
            
        st.divider()