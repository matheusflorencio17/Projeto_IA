from app.utils.loader import FileLoader
from app.llm.client import OllamaClient

class QuestionService:
    def execute(self, pergunta: str):
        documentos = FileLoader().load_documents()

        # 🔍 Filtra páginas relevantes pela pergunta
        palavras = pergunta.lower().split()
        relevantes = []

        for doc in documentos:
            texto_lower = doc["conteudo"].lower()
            if any(p in texto_lower for p in palavras):
                relevantes.append(doc)

        # Se nada bater, pega a primeira página como fallback
        if not relevantes:
            relevantes = documentos[:1]

        # ⚠️ Limite de segurança (performance)
        relevantes = relevantes[:2]

        contexto = "\n\n".join(
            f"(Página {d['pagina']})\n{d['conteudo']}"
            for d in relevantes
        )

        referencias = [{
            "pagina": d["pagina"],
            "trecho": d["conteudo"][:500]
        } for d in relevantes]

        return OllamaClient().ask(contexto, pergunta, referencias)
