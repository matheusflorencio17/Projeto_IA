import pdfplumber
import os

class FileLoader:
    def load_documents(self):
        documentos = []
        pdf_path = os.path.join("dados", "codigo_etica_sbk_2025.pdf")

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF não encontrado em: {pdf_path}")

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                texto = page.extract_text()
                if texto:
                    documentos.append({
                        "pagina": i + 1,
                        "conteudo": texto.strip()
                    })

        return documentos
