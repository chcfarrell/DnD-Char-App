import streamlit as st

st.title("Bogart")

st.badge("The Hard Hitter", color="red")


st.subheader("Dwarf Fighter")
st.subheader("*Rune Knight*")

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
            st.markdown("<h3 style='text align:center; '>18</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPELL DC</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>?</h1", unsafe_allow_html=True)

    with col5:
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>SPEED</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>30</h1", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text align:center; '>PERCEPTION</div", unsafe_allow_html=True)
            st.markdown("<h3 style='text align:left; '>11</h1", unsafe_allow_html=True)
            
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SKILLS</h1", unsafe_allow_html=True)
        
        col8, col9, col10, col11, col12, col13 = st.columns(6)
        
        with col8:
            st.metric(label="Acrobatics", value="", delta="+2")
            st.metric(label="Animal Handling", value="", delta="+1")
            st.metric(label="Arcana", value="", delta="+0", delta_color="off")
            
        with col9:
            st.metric(label="Athletics", value="", delta="+7")
            st.metric(label="Deception", value="", delta="+0", delta_color="off")
            st.metric(label="History", value="", delta="+0", delta_color="off")
            
        with col10:
            st.metric(label="Insight", value="", delta="+1")
            st.metric(label="Intimidation", value="", delta="+2")
            st.metric(label="Investigation", value="", delta="+0", delta_color="off")
            
        with col11:
            st.metric(label="Medicine", value="", delta="+1")
            st.metric(label="Nature", value="", delta="+0", delta_color="off")
            st.metric(label="Perception", value="", delta="+1")
            
        with col12:
            st.metric(label="Performance", value="", delta="+0", delta_color="off")
            st.metric(label="Persuasion", value="", delta="+0", delta_color="off")
            st.metric(label="Religion", value="", delta="+0", delta_color="off")
            
        with col13:
            st.metric(label="Sleight of Hand", value="", delta="+2")
            st.metric(label="Stealth", value="", delta="+2")
            st.metric(label="Survival", value="", delta="+3")



if selection == 1:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="STR", value=20, delta="+5", border=True)
        st.metric(label="INT", value=10, delta="+0", delta_color="off", border=True)
        
    with col2:
        st.metric(label="DEX", value=15, delta="+2", border=True)
        st.metric(label="WIS", value=12, delta="+1", border=True)
        
    with col3:
        st.metric(label="CON", value=17, delta="+3", border=True)
        st.metric(label="CHR", value=11, delta="+0", delta_color="off", border=True)
    
    st.space()
    
    with st.container(border=True):
        
        st.markdown("<h3 style='text align:left; '>SAVING THROWS</h1", unsafe_allow_html=True)
        
        col14, col15, col16 = st.columns(3)
        
        with col14:
            st.metric(label="STR", value="", delta="+7")
            st.metric(label="INT", value="", delta="+0", delta_color="off")
        
        with col15:
            st.metric(label="DEX", value="", delta="+2")
            st.metric(label="WIS", value="", delta="+1")
            
        with col16:
            st.metric(label="CON", value="", delta="+2")
            st.metric(label="CHR", value="", delta="+0", delta_color="off")

if selection == 2:
    
    with st.container(border=True, width=150):
        st.write("INITIATIVE:")
        st.write("+2")
        
    
    col6, col7 = st.columns(2)

    with col6:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Chop Down</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:center; '>+7 to hit, 1d6 slash dmg +5</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Hammer Bash</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+7 to hit, 1d8 bludg dmg +5</div", unsafe_allow_html=True)
            st.space("small")
    
    with col7:
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Shank</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>+7 to hit, 1d4 pierc dmg +5</div", unsafe_allow_html=True)
            st.space("small")
        with st.container(border=True):
            st.markdown("<h3 style='text align:center; '>Sword Burst</h1", unsafe_allow_html=True)
            st.markdown("<div style='text align:left; '>Once per day, 1d6</div", unsafe_allow_html=True)
            st.space("small")
    
    with st.container(border=True):
        st.write("*2 Weapon Fighting* --- can engage in 2 weapon fighting, "
                 "add ability modifier to dmg of 2nd atk."
        )
        
        st.write("*2nd Wind* --- use bonus action to regain HP = to Fighter lvl.")
        
        st.write("*Action Surge* --- can make one additional action.")
        
        st.write("*Giant's Might* --- lasts one minute. Become large. On each turn, "
                 "1 attack can deal 1d6 extra dmg on hit."
        )
      
    with st.container(border=True):
        st.subheader("Rune Knight")
        st.write("*Fire Rune* --- double prof bonus with inscribed tools. On hit with inscribed weapon, "
                 "invoke **Fiery Shackles**: target takes extra 2d6 fire dmg and must succeed STR save "
                 "or be restrained for 1 min. While restrained, target takes 2d6 fire dmg at start of "
                 "each of its turns."
        )
        
        st.write("*Cloud Rune* --- advantage on DEX(sleight of hand) and CHR(deception) checks. "
                 "Additionally, when you or a creature you can see within 30 ft is hit by an "
                 "an attack roll, you can use your reaction to invoke the rune and choose a "
                 "different creature to become the target instead. This rune can only be invoked "
                 "once per short or long rest."
        )
    


if selection == 3:
    
    with st.container(border=True, width=200):
        st.write("Spellcasting Ability:")
        st.write("**NONE**")