# export.py
from pandas import DataFrame
from flask import app, request, extract_text


def export_to_excel(data, output_path):
    df = DataFrame(data)
    df.to_excel(output_path, index=False)

# Integrate with Flask


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = f'uploads/{file.filename}'
    file.save(file_path)
    text = extract_text(file_path)
    data = {'Extracted Text': [text]}
    export_to_excel(data, 'output.xlsx')
    return 'Data exported to Excel successfully'
