# Moon Mission Streamlit App

This is a Streamlit version of the Moon Mission documentation project, ready for deployment.

## Local Development

To run the app locally:

1. Make sure you have Python installed (Python 3.7+ recommended)
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```
4. The app will open in your default web browser at `http://localhost:8501`

## Deployment Options

### Streamlit Cloud

The easiest way to deploy this app is using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this repository to GitHub
2. Sign in to Streamlit Cloud with your GitHub account
3. Create a new app and select this repository
4. Choose the `streamlit_app.py` file as the main file
5. Click "Deploy"

### Heroku

To deploy to Heroku:

1. Create a `Procfile` with the following content:
   ```
   web: sh setup.sh && streamlit run streamlit_app.py
   ```

2. Create a `setup.sh` file with:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   " > ~/.streamlit/config.toml
   ```

3. Deploy to Heroku:
   ```
   heroku create
   git push heroku main
   ```

### Docker

To containerize the app:

1. Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "streamlit_app.py"]
   ```

2. Build and run the Docker container:
   ```
   docker build -t moon-mission-app .
   docker run -p 8501:8501 moon-mission-app
   ```

## Notes

- The app is designed to work with the existing HTML and audio files in the repository
- Make sure all audio files are in the same directory as the Streamlit app for the audio player to work correctly 