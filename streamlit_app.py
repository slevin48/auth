import streamlit as st

# if not st.experimental_user.is_logged_in:
#     if st.button("Log in"):
#         st.login()
# else:
#     if st.button("Log out"):
#         st.logout()
#     st.write(f"Hello, {st.experimental_user.name}!")


# Set page configuration
st.set_page_config(page_title="Authentication Demo", page_icon="🔒")

# Create the login/logout UI
def create_login_ui():
    st.title("Welcome to the App 🔒")
    
    if not st.experimental_user.is_logged_in:
        st.write("Please log in to continue")
        st.button("Login with Google", on_click=st.login,type="primary")
        st.stop()  # Stop execution for non-logged-in users
    
    # User is logged in
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Welcome, {st.experimental_user.name}! 👋")
    with col2:
        st.button("Logout", on_click=st.logout)
    
    return True

# Main app logic
def main():
    # Ensure user is logged in
    if create_login_ui():
        # Your app content goes here
        st.header("Protected Content")
        st.write("This content is only visible to logged-in users.")
        
        # Display user info
        st.subheader("Your Profile")
        st.json(dict(st.experimental_user))

if __name__ == "__main__":
    main()

