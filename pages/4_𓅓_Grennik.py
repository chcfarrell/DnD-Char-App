import streamlit as st

st.title("Grennik")

st.badge("The Big Bad Bird Boss", color="blue")


st.subheader("Goliath Warlock")
st.subheader("*Pact of the Tome*")

st.space()

option_map = {
    0: "STATS & SKILLS",
    1: "ABILITY SCORES & SAVES",
    2: "WEAPONS & COMBAT",
    3: "SPELLCASTING",
}

selection = st.pills(
    "CHARACTER INFO",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)

st.space()

if selection == 0:
    
    col4, col5 = st.columns(2)

    with col4:
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>AC</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>10</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPELL DC</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>14</h1", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPEED</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>30</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>PERCEPTION</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>15</h1", unsafe_allow_html=True)
   
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SKILLS</h1", unsafe_allow_html=True)
        
        col8, col9, col10, col11, col12, col13 = st.columns(6)
        
        with col8:
            st.metric(label="Acrobatics", value="", delta="-2")
            st.metric(label="Animal Handling", value="", delta="+2")
            st.metric(label="Arcana", value="", delta="+1")
            
        with col9:
            st.metric(label="Athletics", value="", delta="+3")
            st.metric(label="Deception", value="", delta="+4")
            st.metric(label="History", value="", delta="+1")
            
        with col10:
            st.metric(label="Insight", value="", delta="+2")
            st.metric(label="Intimidation", value="", delta="+4")
            st.metric(label="Investigation", value="", delta="+1")
            
        with col11:
            st.metric(label="Medicine", value="", delta="+2")
            st.metric(label="Nature", value="", delta="+1")
            st.metric(label="Perception", value="", delta="+2")
            
        with col12:
            st.metric(label="Performance", value="", delta="+4")
            st.metric(label="Persuasion", value="", delta="+4")
            st.metric(label="Religion", value="", delta="+1")
            
        with col13:
            st.metric(label="Sleight of Hand", value="", delta="-2")
            st.metric(label="Stealth", value="", delta="-2")
            st.metric(label="Survival", value="", delta="+2")
            
            
            
if selection == 1:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="STR", value=17, delta="+3", border=True)
        st.metric(label="INT", value=12, delta="+1", border=True)
        
    with col2:
        st.metric(label="DEX", value=7, delta="-2", border=True)
        st.metric(label="WIS", value=15, delta="+2", border=True)
        
    with col3:
        st.metric(label="CON", value=13, delta="+1", border=True)
        st.metric(label="CHR", value=19, delta="+4", border=True)
    
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SAVING THROWS</h1", unsafe_allow_html=True)
        
        col14, col15, col16 = st.columns(3)
        
        with col14:
            st.metric(label="STR", value="", delta="+3")
            st.metric(label="INT", value="", delta="+1")
        
        with col15:
            st.metric(label="DEX", value="", delta="-2")
            st.metric(label="WIS", value="", delta="+2")
            
        with col16:
            st.metric(label="CON", value="", delta="+1")
            st.metric(label="CHR", value="", delta="+4")


if selection == 2:

    with st.container(border=True, width=150):
        st.write("INITIATIVE:")
        st.write("-2")
        
    col6, col7 = st.columns(2)

    with col6:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Greatbow</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:center; '>+5 to hit, 1d8 pierce dmg +3</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Eldritch Blast</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+6 to hit, 1d10 force dmg</div", unsafe_allow_html=True)
            st.space("small")
    
    with col7:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Shortsword</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+5 to hit, 1d6 pierce dmg +3</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Hurdyhurdy</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>When equipped, looks pretty cool</div", unsafe_allow_html=True)
            st.space("small")
            
    with st.container(border=True, width=150):
        st.subheader("Tarquin")
        st.write("Love that guy")
            
            
    
if selection == 3:
    
    col7, col8, col9 = st.columns(3)
    
    with col7:
        with st.container(border=True, width=200):
            st.write("Spellcasting Ability:")
            st.write("**CHARISMA**")
            st.space()
            st.link_button("Warlock Spell List", "https://www.dndbeyond.com/spells/class"
                           "/7-warlock?srsltid=AfmBOoqaW_vt-UH-DOC7_H0CYWNdT7dc_4Gjazz"
                           "B_x_xj_9eEq1wlc-T"
            )
            
    with col8:
        with st.container(border=True, width=200):
           st.write("Spell Save DC:")
           st.write("**14**")
           st.write("Spell ATK Bonus:")
           st.write("**+6**")
           
    with col9:
        with st.container(border=True, width=200):
            st.write("Tremor Sense:")
            st.write("**Vibrations within 30ft**")
            st.write("Aspect of the Moon:")
            st.write("**Light activity during rest**")
            
    with st.container(border=True):
        st.write("**Cantrips**")
        st.write("Mage Hand --- ")
        st.write("Eldritch Blast ---")
        st.write("Fire Bolt ---")
        st.write("Produce Flame ---")
        st.write("Ray of Frost ---")
        
    with st.container(border=True):
        st.write("**1st Level** (__ spell slots)")
        st.write("Comprehend Languages ---")
        st.write("Hex ---")
        
    with st.container(border=True):
        st.write("**2nd Level** (__ spell slots)")
        st.write("Cloud of Daggers ---")
        st.write("Hold Person ---")
            
    with st.container(border=True):
        st.write("*Misty Step* --- as a bonus action, teleport up to 30ft to an unoccupied "
                 "space you can see"
        )
        st.write("*Repelling Blast* --- when you hit a target with eldritch blast, you can "
                 "push the target up to 10ft away in a straight line"
        )
        st.write("*Pact of the Tome* --- access Book of Shadows from your patron ")