from app.services.service import QuestionService

def main():
    pergunta = input("Digite sua pergunta: ")
    resposta = QuestionService().execute(pergunta)
    print(resposta)

if __name__ == "__main__":
    main()
