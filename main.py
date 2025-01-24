from flask import Flask, request, render_template

app = Flask(__name__,template_folder="PDFREADER")

@app.route('/')
def upload_file():
    return render_template("upload.html")

@app.route('/upload.html', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'uploads/{file.filename}')
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
