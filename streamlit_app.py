import streamlit as st

# Set page configuration
st.set_page_config(page_title="Authentication", page_icon="🔒")

st.title("Authentication 🔒")

if not st.user.is_logged_in:
    st.button("Login with Google", on_click=st.login,type="primary")
else:
    # User is logged in
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Welcome, {st.user.name}! 👋")
        st.image(st.user.picture, width=50)
    with col2:
        st.button("Logout", on_click=st.logout)
        
    # Your app content goes here
    st.header("Protected Content")
    st.write("This content is only visible to logged-in users.")
    
    # Display user info
    with st.sidebar:
        st.subheader("Your Profile")
        st.json(dict(st.user))