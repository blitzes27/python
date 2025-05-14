#This creates a website based om pyflask#

The website takes an folderpath as an argument and displays all the pictures in that folder on the website for everyone on the network to see.

* Port = 5000
* IP = same IP as host computer
```bash
git clone --depth=1 --filter=blob:none --sparse https://github.com/blitzes27/python.git && \
cd python && \
git sparse-checkout set picture_website && \
cd picture_website && \
echo 'FOLDER-PATH="PUT-YOUR-PATH"' > .env && \
docker compose up --build -d web ipcheck
