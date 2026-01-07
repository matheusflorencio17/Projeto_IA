Extrator de Insights e Suporte Técnico

## Objetivo
Criar um script em Python que processe um conjunto de documentos e responda a perguntas específicas, garantindo que a resposta seja estruturada e baseada estritamente nos dados fornecidos.

## Requisitos Obrigatórios
1. **Processamento de Contexto:** O script deve ler os arquivos da pasta `/dados`.
2. **Interface de Pergunta:** O utilizador deve poder fazer uma pergunta via terminal ou script.
3. **Prompt Engineering:** O modelo deve ser instruído a:
   - Responder apenas com base nos documentos.
   - Retornar a resposta num formato JSON estruturado (ex: `{"resposta": "...", "fonte": "nome_do_arquivo.pdf", "confianca": "alta/baixa"}`).
4. **Tratamento de Erros:** Lidar com casos onde o texto é grande demais para o modelo (truncagem ou seleção de trechos).

## Diferenciais
- Implementar uma busca vetorial local (ChromaDB/FAISS).
- Criar um pequeno front-end em Streamlit.
- Implementar "Chain of Thought" no prompt para explicar o raciocínio.