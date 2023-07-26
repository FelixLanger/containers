# 📦 Containers
## 🚀 Quickly Build Your Containers with GitHub Actions
### 📋 Prerequisites

   - Python3 🐍
   - GitHub Account 🐱
   - DockerHub Account 🐳

### 🛠️ Setup

1. Fork this Repository 🍴

2. Create DockerHub Secrets 🔑  
    - Log in to your DockerHub account.
    - Go to your account settings.
    - Find the security section where you can manage your access tokens.
    - Click on **New Access Token**.
    - Give your token a descriptive name and click **Create**.
    - DockerHub will generate a new token for you. Remember to copy this token and keep it safe, as you won't be able to see it again.

3. Add Secrets to GitHub Repository 🕵️‍♀️
    - Go to the GitHub repository where you want to add the secrets.
    - Click on the **Settings** tab of the repository.
    - Select **Actions** under **Secrets and Variables** from the left sidebar.
    - Click on the **New repository secret** button.
    - Add two secrets: ``DOCKERHUB_USERNAME`` and ``DOCKERHUB_TOKEN``  
        - For ``DOCKERHUB_USERNAME`` use your DockerHub username.
        - For ``DOCKERHUB_TOKEN`` use the access token you generated on DockerHub.
    - Click on **Add secret** to save each secret.

### 📚 Usage

Run the ``./new_container.py`` command. You will be prompted to name your container.  
After this, you'll find a directory that includes an empty Dockerfile.  
Fill the Dockerfile with your Docker recipe.  
Once you're finished, use ``git add`` for the container directory and the .github directory, then ``git commit`` and ``git push`` it to GitHub.  
Your container will now be built on GitHub and pushed to your DockerHub once it's finished. 🎉