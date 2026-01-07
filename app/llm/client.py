import requests

class OllamaClient:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3"

    def ask(self, contexto: str, pergunta: str, referencias: list):
        prompt = f"""
Você é um assistente que responde EXCLUSIVAMENTE com base no texto fornecido.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

INSTRUÇÕES:
- Responda apenas com base no contexto
- Seja claro e direto
- NÃO invente informações
"""

        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()
            data = response.json()

            return {
                "resposta": data.get("response", "").strip(),
                "fonte": referencias[0] if referencias else None,
                "confianca": "alta" if referencias else "baixa"
            }

        except requests.exceptions.Timeout:
            return {
                "resposta": "Tempo excedido ao consultar o modelo.",
                "fonte": referencias[0] if referencias else None,
                "confianca": "baixa"
            }

        except Exception as e:
            return {
                "resposta": f"Erro ao consultar o modelo: {str(e)}",
                "fonte": None,
                "confianca": "baixa"
            }
