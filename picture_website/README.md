# This creates a website based om pyflask #

The website takes an folder_path as an argument and displays all the pictures in that folder on the website for everyone on the network to see. Set your path in:

## FOLDER_PATH=XXXXXX ##

* Port = 5000
* IP = same IP as host computer
* It will display where the container can be reached in the terminal when it have built the website

You need to have docker & compose installed on your system

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
