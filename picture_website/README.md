# This builds a Docker container from the repository and runs it to host a PyFlask-based website #

The website accepts a folder path as an argument, displaying all pictures from the specified folder for everyone on your local network to access. Set your image folder path by modifying:

## FOLDER_PATH=XXXXXX ##

* Port = 5000
* IP = same IP as host computer
* Once the container is built and running, the terminal will display the URL where the website can be reached.

![alt text](pictures/picture2.png)
![alt text](pictures/picture3.png)

### You need to have docker & compose installed on your system

Run the website buy running script below. Dont forget to set your FOLDER_PATH variable

```bash
git clone --depth=1 --filter=blob:none --sparse https://github.com/blitzes27/python.git && \
cd python && \
git sparse-checkout set picture_website && \
cd picture_website && \
echo "FOLDER_PATH=${HOME}/HDR" > .env && \
docker compose up --build -d
curl -fsSL "https://raw.githubusercontent.com/blitzes27/linux/main/Random_stuff/grep_internal_ip.sh" | bash | \
awk -F': ' '{print "http://"$2":5000"}'
echo "use the ip above to see page"
```

### Brief description of each file

- **app.py**  
  Defines and runs a Flask app on port 5000. Provides routes for the landing page and the results page.

- **docker-compose.yml**  
  - Builds the Docker image using `dockerfile`  
  - Exposes container port 5000 to the host  
  - Loads environment variables (e.g. `FOLDER_PATH`) from a `.env` file  

- **dockerfile**  
  1. Uses an official Python base image  
  2. Creates and activates a virtual environment  
  3. Installs dependencies from `requirements.txt`  
  4. Copies the application code and sets the container’s startup command  

- **requirements.txt**  
  Lists all Python packages required by the application (for example, Flask and Pillow).

- **pictures/**  
  Contains example images used for demonstration or testing purposes.

- **static/index.css**  
  CSS rules for the landing page, including button styles and layout.

- **static/result.css**  
  CSS rules for the results page, including gallery and image layout.

- **static/mango-owl.jpeg**  
  Logo (an owl) displayed on the landing page for branding.

- **templates/index.html**  
  Jinja2 template for the landing page, containing an upload form or folder selection.

- **templates/result.html**  
  Jinja2 template for the results page, which displays processed images in a gallery.