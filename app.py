import PyPDF2

def unir_pdfs(lista_de_pdfs, salida):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in lista_de_pdfs:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for pagina in range(len(pdf_reader.pages)):
            pagina_actual = pdf_reader.pages[pagina]
            pdf_writer.add_page(pagina_actual)

    with open(salida, 'wb') as archivo_de_salida:
        pdf_writer.write(archivo_de_salida)

# Lista de archivos PDF que quieres unir
archivos_pdf = ['Documento_10.pdf', 'Documento_2.pdf', 'Documento_3.pdf']
# Nombre del archivo PDF resultante
archivo_salida = 'archivo_unido.pdf'

unir_pdfs(archivos_pdf, archivo_salida)
