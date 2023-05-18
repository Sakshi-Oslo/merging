from flask import Flask, request, send_file, render_template
from PyPDF2 import PdfMerger

app= Flask(__name__, template_folder="templates", static_folder="static")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        target_list = ['design_records.pdf', 'Process_FMEA.pdf', 'control_plan.pdf', 'CAVIS.pdf']
        files= request.files.getlist('files')
        ordered_files = [file for file in files if file.filename in target_list]
        merger = PdfMerger()
        for filename in target_list:
            for file in ordered_files:
                if file.filename == filename:
                    merger.prepend(file)
                    ordered_files.remove(file)
                    break #Exit the inner loop once a file has been appended
        merger.write("merged-pdf.pdf")
        merger.close()
        return send_file("merged-pdf.pdf", as_attachment= True)
if __name__ == '__main__':
    app.run(debug=True)