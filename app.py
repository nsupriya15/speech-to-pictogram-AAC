from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Load mapping from Picto.txt
mapping = {}
with open('Picto.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if '->' in line:
            word, img = line.strip().split('->')
            word = word.strip().lower()   # make lowercase to avoid case mismatch
            img = img.strip()
            mapping[word] = img

@app.route('/Pictogram', methods=['GET', 'POST'])
def index():
    image_files = []
    if request.method == 'POST':
        sentence = request.form['sentence']
        words = sentence.strip().split()

        for word in words:
            word_lower = word.lower()  # Convert input to lowercase
            img_file = mapping.get(word_lower)
            if img_file:
                image_path = os.path.join('pic', img_file)
                if os.path.isfile(os.path.join('static', image_path)):
                    image_files.append(image_path)

    return render_template('display.html', images=image_files)

if __name__ == '__main__':
    app.run(debug=True)
