import streamlit as st

st.title("Dank Bungalo")

st.badge("The Farm Boy", color="green")


st.subheader("Halfling Paladin")
st.subheader("*Oath of the Harvest*")

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
            st.markdown("<h3 style='text align:left; '>17</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPELL DC</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>12</h1", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPEED</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>25</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>PERCEPTION</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>10</h1", unsafe_allow_html=True)
            
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SKILLS</h1", unsafe_allow_html=True)
        
        col8, col9, col10, col11, col12, col13 = st.columns(6)
        
        with col8:
            st.metric(label="Acrobatics", value="", delta="+0", delta_color="off")
            st.metric(label="Animal Handling", value="", delta="+2")
            st.metric(label="Arcana", value="", delta="+3")
            
        with col9:
            st.metric(label="Athletics", value="", delta="+4")
            st.metric(label="Deception", value="", delta="+2")
            st.metric(label="History", value="", delta="+3")
            
        with col10:
            st.metric(label="Insight", value="", delta="+0", delta_color="off")
            st.metric(label="Intimidation", value="", delta="+4")
            st.metric(label="Investigation", value="", delta="+3")
            
        with col11:
            st.metric(label="Medicine", value="", delta="+0", delta_color="off")
            st.metric(label="Nature", value="", delta="+3")
            st.metric(label="Perception", value="", delta="+0", delta_color="off")
            
        with col12:
            st.metric(label="Performance", value="", delta="+2")
            st.metric(label="Persuasion", value="", delta="+2")
            st.metric(label="Religion", value="", delta="+3")
            
        with col13:
            st.metric(label="Sleight of Hand", value="", delta="+0", delta_color="off")
            st.metric(label="Stealth", value="", delta="+0", delta_color="off")
            st.metric(label="Survival", value="", delta="+2")

if selection == 1:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="STR", value=15, delta="+2", border=True)
        st.metric(label="INT", value=17, delta="+3", border=True)
        
    with col2:
        st.metric(label="DEX", value=11, delta="+0", delta_color="off", border=True)
        st.metric(label="WIS", value=10, delta="+0", delta_color="off", border=True)
        
    with col3:
        st.metric(label="CON", value=9, delta="-1", border=True)
        st.metric(label="CHR", value=14, delta="+2", border=True)
    
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SAVING THROWS</h1", unsafe_allow_html=True)
        
        col14, col15, col16 = st.columns(3)
        
        with col14:
            st.metric(label="STR", value="", delta="+4")
            st.metric(label="INT", value="", delta="+3")
        
        with col15:
            st.metric(label="DEX", value="", delta="+0", delta_color="off")
            st.metric(label="WIS", value="", delta="+2")
            
        with col16:
            st.metric(label="CON", value="", delta="-1")
            st.metric(label="CHR", value="", delta="+2")


if selection == 2:
    
    with st.container(border=True, width=150):
        st.write("INITIATIVE:")
        st.write("+0")
    
    col6, col7 = st.columns(2)

    with col6:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Scythe</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:center; '>+6 to hit, 1d4 slash dmg +2</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Longbow</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+2 to hit, 1d4 pierce dmg +0</div", unsafe_allow_html=True)
            st.space("small")
    
    with col7:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Whip</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+2 to hit, 1d4 slash dmg +0</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Shield</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>When equipped, +2 to AC</div", unsafe_allow_html=True)
            st.space("small")
    
if selection == 3:
    
    col7, col8, col9 = st.columns(3)
    
    with col7:
        with st.container(border=True, width=200):
            st.write("Spellcasting Ability:")
            st.write("**CHARISMA**")
            st.space("small")
            st.link_button("Paldin Spell List", "https://www.dndbeyond.com/spells"
                           "/class/4-paladin?filter-search=&filter-verbal=&filter-"
                           "somatic=&filter-material=&filter-concentration=&filter-"
                           "ritual=&filter-sub-class=&filter-partnered-content=f")
    with col8:
        with st.container(border=True, width=200):
            st.write("Spell Save DC:")
            st.write("**12**")
            st.write("Spell Atk Bonus:")
            st.write("**+2**")
            
    with col9:
        with st.container(border=True, width=200):
            st.write("Divine Health:")
            st.write("**immune to disease**")
            st.space("small")
            st.space("medium")
        
    with st.container(border=True):
        st.write("*Divine Sense* --- until next turn, know the location of "
                 "any celestial, fiend, or undead within 60 ft that is not "
                 "behind total cover. You know the type, but not the identity."
        )
        
        st.write("*Divine Smite* --- when you hit a creature with a melee "
                 "weapon attack, you can expend one spell slot to deal radiant "
                 "dmg to the target in addition to the weapon's dmg. Extra dmg "
                 "is 2d8 for 1st level spell slot, plus 1d8 for each spell slot "
                 "level higher than 1st. Dmg increases by 1d8 if target is undead"
                 " or fiend."
        )
        
        st.write("*Lay on Hands* --- access to pool of healing that replenishes "
                 "after a long rest. With this pool, you can restore total HP of "
                 "Paladin lvl * 5 (20 HP). As an action, touch a creature to restore "
                 "number of HP from the pool. Alternatively, you can use 5 HP from the "
                 "pool to cure a target of one disease or neutralize on poison effecting it,"
        )
        
        st.write("*Channel Divinity: Reaper's Curse* --- as an action, wreath a target "
                 "within 30 ft in shadowy, tree-like forms. The target must succeed CON "
                 "save or take 1d8 necrotic dmg and be **cursed** for 1 min. While target is "
                 "**cursed**, gain the following benefits: bonus to dmg rolls = to "
                 "prof bonus. Resistance to dmg dealt by target. If target dies, regain "
                 "HP = to Paladin lvl."
        )