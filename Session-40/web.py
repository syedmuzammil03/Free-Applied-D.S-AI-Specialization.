
import streamlit as st

def about_us():
    st.header("About Us")
    col1, col2 = st.columns(2)
    with col1:
        st.image("WAM.png")
        st.header("Waqas Ali")
        st.write("Executive Director (ED)")
    
    with col2:
        st.image("FAN.png")
        st.header("Farough Ali")
        st.write("Chief Executive Officer (CEO)")
        
def faqs():
    tab1, tab2 = st.tabs(["General", "AI & Data Specialization"])
    with tab1:
        faq1 = st.expander("Why AI is imporant for Everyone?")
        with faq1:
            st.write("AI is widely used in all domains that is why it is important for Everyone")
            
        faq2 = st.expander("Where is AI used?")
        with faq2:
            st.write("AI is used in variety of task. Such as;")
            st.markdown("""
            - Automation
            - Decision Making
            - Problem solving
            - etc;
            """)
    with tab2:
        st.write("Coming Soon ----")
        
def feedback():
    st.write("Please provide your feedback below!")

    name = st.text_input("Please write your name")

    st.write(f"Welcome {name}")

    enjoy = st.radio("Do you enjoy our training?",["Yes", "No"])

    if enjoy == "Yes":
        st.write("Glad to hear that!")
    elif enjoy == "No":
        st.write("Sorry to hear that. We'll strive to improve.")

    rating = st.slider("How do you rate our training",1,10,5)
    training = st.selectbox("What training do you like most?", ["Data Analytics","Generative AI", "Application Development"])

    st.write(f"You have rated our training {rating} and you like {training} training")

    message = st.text_area("Comments", "Please provide your comments to improve our service further")

    st.checkbox("Please confirm all above information is correct")

st.image("DS.png")
st.title("DigiTech Synergy Pvt. Ltd")

st.sidebar.title("Navigation")
options = st.sidebar.selectbox("Choose a section", ["About Us", "FAQs", "Feedback Form"])

if options == "About Us":
    about_us()
    
elif options == "FAQs":
    faqs()
    
elif options == "Feedback Form":
    feedback()
    
