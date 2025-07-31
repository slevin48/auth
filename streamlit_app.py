import streamlit as st
from st_paywall import add_auth

# Set page configuration
st.set_page_config(page_title="My super SaaS ", page_icon="🚀")

st.title("My super SaaS 🚀")

if not st.user.is_logged_in:
    st.button("Login with Google", on_click=st.login,type="primary")
else:
    # Add subscription check for logged-in users
    add_auth()
    
    # User is logged in
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Welcome, {st.user.name}! 👋")
        st.image(st.user.picture, width=50)
    with col2:
        st.button("Logout", on_click=st.logout)
    
    # Your app code here - only runs for subscribed users
    st.header("Premium content🔐")
    st.write("This content is only visible to subscribers.")

    if st.toggle("Show User Info"):
        # Display user info
        with st.sidebar:
            st.subheader("Your Profile")
            st.json(dict(st.user))