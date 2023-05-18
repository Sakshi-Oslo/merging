from flask import Flask, request, send_file, render_template
from PyPDF2 import PdfMerger

app= Flask(__name__, template_folder="templates", static_folder="static")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        target_list = ['design_records.pdf','Process flow diagram.pdf', 'dimensional results.pdf', 'functional records.pdf','records of material.pdf','FMEA.pdf', 'control plan.pdf','PSW.pdf','Authorized engineering change.pdf','Customer engineering approval.pdf','DFMEA.pdf','Measurement system analysis studies.pdf', 'Initial Process Studies.pdf','Qualified Laboratory Documentation.pdf','Checking aids.pdf','Appearance Approval report.pdf','Sample production parts.pdf', 'Master sample.pdf', 'Customer Specific requirement.pdf']
        files= request.files.getlist('files')
        ordered_files = [file for file in files if file.filename in target_list]
        merger = PdfMerger()
        for filename in target_list:
            for file in ordered_files:
                if file.filename == filename:
                    merger.append(file)
                    ordered_files.remove(file)
                    break #Exit the inner loop once a file has been appended
        merger.write("merged-pdf.pdf")
        merger.close()
        return send_file("merged-pdf.pdf", as_attachment= True)
if __name__ == '__main__':
    app.run(debug=True)