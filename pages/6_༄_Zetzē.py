import streamlit as st

st.title("Zetzē")

st.badge("The Windy Bear Man", color="orange")


st.subheader("Genasi Druid")
st.subheader("*Circle of the Moon*")

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
            st.markdown("<h3 style='text align:left; '>13</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPELL DC</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>13</h1", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPEED</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>35</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>PERCEPTION</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>15</h1", unsafe_allow_html=True)

    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SKILLS</h1", unsafe_allow_html=True)
        
        col8, col9, col10, col11, col12, col13 = st.columns(6)
        
        with col8:
            st.metric(label="Acrobatics", value="", delta="-1")
            st.metric(label="Animal Handling", value="", delta="+3")
            st.metric(label="Arcana", value="", delta="+2")
            
        with col9:
            st.metric(label="Athletics", value="", delta="-1")
            st.metric(label="Deception", value="", delta="+1")
            st.metric(label="History", value="", delta="+2")
            
        with col10:
            st.metric(label="Insight", value="", delta="+5")
            st.metric(label="Intimidation", value="", delta="+1")
            st.metric(label="Investigation", value="", delta="+2")
            
        with col11:
            st.metric(label="Medicine", value="", delta="+3")
            st.metric(label="Nature", value="", delta="+4")
            st.metric(label="Perception", value="", delta="+5")
            
        with col12:
            st.metric(label="Performance", value="", delta="+1")
            st.metric(label="Persuasion", value="", delta="+1")
            st.metric(label="Religion", value="", delta="+4")
            
        with col13:
            st.metric(label="Sleight of Hand", value="", delta="-2")
            st.metric(label="Stealth", value="", delta="-2")
            st.metric(label="Survival", value="", delta="+3")
            


if selection == 1:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="STR", value=9, delta="-1", border=True)
        st.metric(label="INT", value=14, delta="+2", border=True)
        
    with col2:
        st.metric(label="DEX", value=6, delta="-2", border=True)
        st.metric(label="WIS", value=16, delta="+3", border=True)
        
    with col3:
        st.metric(label="CON", value=7, delta="-2", border=True)
        st.metric(label="CHR", value=12, delta="+1", border=True)
    
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SAVING THROWS</h1", unsafe_allow_html=True)
        
        col14, col15, col16 = st.columns(3)
        
        with col14:
            st.metric(label="STR", value="", delta="-1")
            st.metric(label="INT", value="", delta="+4")
        
        with col15:
            st.metric(label="DEX", value="", delta="-2")
            st.metric(label="WIS", value="", delta="+5")
            
        with col16:
            st.metric(label="CON", value="", delta="-2")
            st.metric(label="CHR", value="", delta="+1")
   


if selection == 2:

    with st.container(border=True, width=150):
        st.write("INITIATIVE:")
        st.write("-2")
        
    col6, col7 = st.columns(2)

    with col6:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Cane</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:center; '>-1 to hit, 1d6 bludgeon dmg -1</div", unsafe_allow_html=True)
            st.space("small")
   
    
    with col7:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Shield</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+When equipped, AC +2</div", unsafe_allow_html=True)
            st.space("small")
    
    st.space("small")
    
    col01, col02 , col03 = st.columns(3)
    
    with col01:
        st.space("medium")
        st.write("Black Bear")
        st.write("AC: 11   HP: 19")
        st.write("Speed: 40ft, Climb: 30ft")
        st.write("Multiattack:" + "\n" + " - Bite +3 to hit, 1d6+2 pierce dmg" + "\n" + " - Claws +3 to hit, "
                 "2d4+2 slash dmg"
        )
      
    with col02:
        with st.container(border=True, width=180):
            st.markdown("<h3 style='text align:center; '>Wild Shape</h1", unsafe_allow_html=True)
            
    with col03:
        st.space("medium")
        st.write("Blink Dog")
        st.write("AC: 13   HP: 22")
        st.write("Speed: 40ft")
        st.write(" - Bite +3 to hit, 1d6+1 pierce dmg" + "\n" + " - Teleport(recharge 4-6) blink dog magically "
                 "teleports up to 40ft to an unoccupied space it can see. Before teleporting, can make "
                 "one bite attack"
        )
    
if selection == 3:
    
    col7, col8, col9 = st.columns(3)
    
    with col7:
        with st.container(border=True, width=200):
            st.write("Spellcasting Ability:")
            st.write("**WISDOM**")
            st.space("small")
            st.link_button("Druid Spell List", "https://www.dndbeyond.com/spells/class/"
                           "3-druid?srsltid=AfmBOopP5q91Q7LXRwYaotW0vIamPQmTAq5Of90wMoqw"
                           "Xk8yUXYLn_i-"
            )
            
    with col8:
        with st.container(border=True, width=200):
           st.write("Spell Save DC:")
           st.write("**13**")
           st.write("Spell ATK Bonus:")
           st.write("**+5**")
        
    with col9:
        with st.container(border=True, width=200):
            st.write("Unending Breath")
            st.write("Lightning Resistance")
            st.write("Wild Shape:")
            st.write("**2 uses per long rest**")
     
    with st.container(border=True):
        st.write("**Cantrips**")
        st.write("Create Bonfire --- ")
        st.write("Gust ---")
        st.write("Shocking Grasp ---")
        st.write("Magic Stone ---")
        
    with st.container(border=True):
        st.write("**1st Level** (4 spell slots)")
        st.write("Fog Cloud ---")
        st.write("Detect Magic ---")
        st.write("Entangle ---")
        st.write("Animal Friendship ---")
        st.write("Cure Wounds ---")
        
    with st.container(border=True):
        st.write("**2nd Level** (3 spell slots)")
        st.write("Heat Metal ---")
        st.write("Spike Growth ---")