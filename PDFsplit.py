import PyPDF2, os
import pandas as ps

os.chdir("C:/path/to/project/") #change this to your PDF location.

pdfFileObj=open("file.pdf",'rb') #swap 'file' for the name of the PDF you want to split.
ftable = ps.read_excel('filenames_list.xlsx',engine='openpyxl') 
#optional, a list of names, IDs or something unique to name your files by.
#works if the names/pages match (e.g. First name in a list corresponds to receipt for name on the first page of a PDF)

pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
for pgnum in range(pdfReader.numPages):
    pdfwrt=PyPDF2.PdfFileWriter()
    pdfwrt.addPage(pdfReader.getPage(pgnum))
    lname=ftable['col_name'].iloc[pgnum].replace(" ","") #replace 'header_name' with
    file_name = 'prefix_'+lname+'.pdf' #change prefix to fixed part of PDF name.
    pdfout=open(file_name,'wb')
    pdfwrt.write(pdfout)
    pdfout.close()

pdfFileObj.close()
