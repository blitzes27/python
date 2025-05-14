from flask import Flask, request, render_template
import sys, os, base64

app = Flask(__name__)

# get the image folder from command line argument
IMAGE_FOLDER = sys.argv[1] if len(sys.argv) > 1 else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    if not IMAGE_FOLDER:
        return "No folder specified. Start with: python app.py /path/to/folder", 400

    # List all files in the specified folder
    files = sorted(os.listdir(IMAGE_FOLDER))
    images = []
    for fname in files:
        if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            path = os.path.join(IMAGE_FOLDER, fname)
            with open(path, "rb") as img:
                b64 = base64.b64encode(img.read()).decode('utf-8')
            # Save both the base64 string and the file extension
            images.append({
                'name': fname,
                'data': b64,
                'ext': fname.rsplit('.', 1)[1].lower()
            })

    return render_template("result.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)