# This creates a website based om pyflask #

The website takes an folder_path as an argument and displays all the pictures in that folder on the website for everyone on the network to see. Set your path in:

## FOLDER_PATH=XXXXXX ##

* Port = 5000
* IP = same IP as host computer
* It will display where the container can be reached in the terminal when it have built the website

```bash
git clone --depth=1 --filter=blob:none --sparse https://github.com/blitzes27/python.git && \
cd python && \
git sparse-checkout set picture_website && \
cd picture_website && \
echo "FOLDER_PATH=${HOME}/HDR" > .env && \
docker compose up --build -d
curl -fsSL "https://raw.githubusercontent.com/blitzes27/linux/main/Random_stuff/grep_internal_ip.sh"
echo "use the ip above and put the ending ':5000' at the end to connect"
