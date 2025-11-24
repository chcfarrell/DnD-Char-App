import streamlit as st

st.title("Grob Greedfeets")

st.badge("The Sneakiest Feet", color="violet")


st.subheader("Goblin Rogue")
st.subheader("*Arcane Trickster*")

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
            st.markdown("<h3 style='text align:left; '>14</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPELL DC</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>12</h1", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPEED</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>30</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>PERCEPTION</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>13</h1", unsafe_allow_html=True)
   
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SKILLS</h1", unsafe_allow_html=True)
        
        col8, col9, col10, col11, col12, col13 = st.columns(6)
        
        with col8:
            st.metric(label="Acrobatics", value="", delta="+6")
            st.metric(label="Animal Handling", value="", delta="+0", delta_color="off")
            st.metric(label="Arcana", value="", delta="-1")
            
        with col9:
            st.metric(label="Athletics", value="", delta="+2")
            st.metric(label="Deception", value="", delta="-1")
            st.metric(label="History", value="", delta="-1")
            
        with col10:
            st.metric(label="Insight", value="", delta="+2")
            st.metric(label="Intimidation", value="", delta="-3")
            st.metric(label="Investigation", value="", delta="-1")
            
        with col11:
            st.metric(label="Medicine", value="", delta="+0", delta_color="off")
            st.metric(label="Nature", value="", delta="-1")
            st.metric(label="Perception", value="", delta="+0", delta_color="off")
            
        with col12:
            st.metric(label="Performance", value="", delta="-3")
            st.metric(label="Persuasion", value="", delta="-3")
            st.metric(label="Religion", value="", delta="-1")
            
        with col13:
            st.metric(label="Sleight of Hand", value="", delta="+8")
            st.metric(label="Stealth", value="", delta="+8")
            st.metric(label="Survival", value="", delta="+0", delta_color="off")
            
            
if selection == 1:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="STR", value=14, delta="+2", border=True)
        st.metric(label="INT", value=12, delta="+1", border=True)
        
    with col2:
        st.metric(label="DEX", value=18, delta="+4", border=True)
        st.metric(label="WIS", value=11, delta="+0", delta_color="off", border=True)
        
    with col3:
        st.metric(label="CON", value=16, delta="+3", border=True)
        st.metric(label="CHR", value=4, delta="-3", border=True)

    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SAVING THROWS</h1", unsafe_allow_html=True)
        
        col14, col15, col16 = st.columns(3)
        
        with col14:
            st.metric(label="STR", value="", delta="+2")
            st.metric(label="INT", value="", delta="+0", delta_color="off")
        
        with col15:
            st.metric(label="DEX", value="", delta="+6")
            st.metric(label="WIS", value="", delta="+0", delta_color="off")
            
        with col16:
            st.metric(label="CON", value="", delta="+3")
            st.metric(label="CHR", value="", delta="-3")


if selection == 2:

    with st.container(border=True, width=150):
        st.write("INITIATIVE:")
        st.write("+4")
        
    col6, col7 = st.columns(2)

    with col6:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Shortsword</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:center; '>+6 to hit, 1d6 pierce dmg +4</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Dagger</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+6 to hit, 1d4 pierce dmg +4</div", unsafe_allow_html=True)
            st.space("small")
    
    with col7:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Whip</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+6 to hit, 1d4 slash dmg +4</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Dragon Priest Dagger</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+6 to hit, 1d4 pierce +4 & 1d4 poison dmg +4 </div", unsafe_allow_html=True)
            st.space("small")

    with st.container(border=True):
        st.write("*Fury of the Small* --- once per short or long rest, deal extra dmg equal to Rogue level if "
                 "target is larger then you"
        )
        st.write("*Sneak Attack* --- once per turn, deal extra 2d6 dmg to a target hit with an attack if you "
                 "attack with ranged or finesse weapons & have advantage or target is within 5ft of an ally"
        )
        st.write("*Cunning Action / Nimble Escape* --- may take a bonus action each turn to dash, disengage, hide, "
                 "or control mage hand"
        )


if selection == 3:
    
    col7, col8, col9 = st.columns(3)
    
    with col7:
        with st.container(border=True, width=200):
            st.write("Spellcasting Ability:")
            st.write("**INTELLIGENCE**")
            st.space("small")
            st.link_button("Wizard Spell List", "https://www.dndbeyond.com/spells"
                           "/class/4-paladin?filter-search=&filter-verbal=&filter-"
                           "somatic=&filter-material=&filter-concentration=&filter-"
                           "ritual=&filter-sub-class=&filter-partnered-content=f"
            )
            
    with col8:
        with st.container(border=True, width=200):
           st.write("Spell Save DC:")
           st.write("**12**")
           st.write("Spell ATK Bonus:")
           st.write("**+3**")
           
    with col9:
        with st.container(border=True, width=200):
            st.write("Mage Hand Legerdemain:")
            st.write("**Stow items, retrieve items, or use thieves' tools with mage hand**")
            
    
        
    with st.container(border=True):
        st.write("**Cantrips**")
        st.write("Mage Hand --- ")
        st.write("Infestation ---")
        st.write("Toll the dead ---")
        
    with st.container(border=True):
        st.write("**1st Level** (2 spell slots)")
        st.write("Disguise self ---")
        st.write("Silvery barbs ---")
        st.write("Catapult ---")