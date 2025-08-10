# Streamlit Auth 🔒

**Setting Up Google Authentication**
1. Create Google Cloud Credentials:
    - Go to Google Cloud’s API & Services → Credentials.
    - Configure OAuth consent screen (app metadata, scopes).
    - Select required scopes (e.g., OpenID, email, profile, Google Calendar).
    - Verification is required if using sensitive scopes.

![credentials](img/credentials.png)
![oauth-consent-screen](img/oauth-consent-screen.png)
![oauth-consent-screen2](img/oauth-consent-screen2.png)
![scopes](img/scopes.png)
<!-- ![calendar](img/calendar.png) -->
![test-users](img/test-users.png)

2. Create OAuth Client ID:
    - Set up credentials for a web application.
    - Define a callback URL (e.g., http://localhost:8501/oauth2callback).
    - Store client ID and secret in Streamlit’s secrets file.

![Create-OAuth-client-ID](img/Create-OAuth-client-ID.png)
![callback-url](img/callback-url.png)
![client-created](img/client-created.png)


3. Create the secrets configuration file:
    - Create a file named `secrets.toml` in the `.streamlit/` directory.
    - Add the client ID and secret to the file, as well as redirect_uri.
    - Add the file to `.gitignore`.

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "YOUR_RANDOM_SECRET_KEY"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

4. *Bonus* Deploy on render.com

In Google Cloud → **Google Auth Platform** (APIs & Services → Credentials), add an **Authorized redirect URI**:
     `https://<your-render-service>.onrender.com/oauth2callback`
     (Use your custom domain if you have one.)

Modify the `redirect_uri` from `secrets.toml` with:

```toml
[auth]
redirect_uri = "https://<your-render-service>.onrender.com/oauth2callback"
...
```

Render’s **Secret Files** land at `/etc/secrets/<filename>` (or the repo root). Easiest approach:

* In your Render service → **Environment**:

  * Add a **Secret File** named `secrets.toml` containing the TOML above.
* Start command (Render → Settings → Start Command):

```bash
mkdir -p .streamlit && cp /etc/secrets/secrets.toml .streamlit/secrets.toml && exec streamlit run streamlit_app.py --server.port "$PORT" --server.address 0.0.0.0
```

(That copy step places the secret where Streamlit expects it.) ([Render][1], [Render][2], [Render][3])

[1]: https://render.com/docs/configure-environment-variables "Environment Variables and Secrets"
[2]: https://community.render.com/t/secrets-in-secret-file-env-automatically-makes-environment-variables/3598 "Secrets in secret file .env automatically makes environment ..."
[3]: https://community.render.com/t/secrets-management-for-streamlit-deployment-on-render/10467 "Secrets management for Streamlit deployment on Render"

Resources:
- [st.login](https://docs.streamlit.io/develop/api-reference/user/st.login)
- [Streamlit 1.42.0 release note](https://docs.streamlit.io/develop/quick-reference/release-notes#version-1420-latest)
- [Use the Google Auth Platform to authenticate users](https://docs.streamlit.io/develop/tutorials/authentication/google)
- [Fanilo - I Tried Adding Google Auth To a Streamlit App (It Didn't Go Well)](https://www.youtube.com/watch?v=0M4K53XBsjo&ab_channel=FaniloAndrianasolo)
- [Fanilo - Native Google and Email Authentication in Streamlit](https://youtu.be/QziGFxHM1pA?si=EE4ToG-_MlDQh_3x)
