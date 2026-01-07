Este projeto permite fazer perguntas sobre um documento em PDF e receber respostas baseadas apenas no conteúdo desse documento. Ele foi criado para facilitar a consulta de textos longos, como códigos de ética, normas internas e políticas corporativas, sem a necessidade de ler o arquivo inteiro.

- O que este projeto faz
    O sistema lê um documento em PDF e permite que o usuário faça perguntas pelo computador. A resposta será gerada somente com base no texto do próprio documento, indicando a página e o trecho de onde a informação foi retirada.

- O que é necessário para usar
    É preciso ter um computador com Windows e o programa Python instalado (versão 3.12 ou superior). Também é necessário ter o Ollama instalado, que é o programa responsável por executar a inteligência artificial localmente no computador.

- Instalação do Ollama
    Para instalar o Ollama, acesse o site https://ollama.com e siga as instruções de instalação. Após instalar, o Ollama deve estar aberto ou em execução antes de utilizar o projeto.

- Preparação do projeto
    Faça o download do projeto e salve em uma pasta de sua preferência no computador. Em seguida, abra o prompt de comando dentro da pasta do projeto.

- Instalação dos componentes necessários
    Dentro da pasta do projeto, execute o comando abaixo para instalar tudo o que o sistema precisa para funcionar. Aguarde até o processo finalizar antes de continuar.
    pip install -r requirements.txt

- Organização do documento PDF
    O documento que será consultado deve estar dentro da pasta chamada “dados”, lembrando que deve ser anexado o documento:
    Caminho na qual deve anexar o documento:
    Projeto_IA\dados\
    **Documento não anexado por questões de ética.**
    
    **Esse documento precisa ser um PDF com texto selecionável. PDFs escaneados não funcionam.**

- Execução do projeto
    Após concluir todos os passos anteriores, o projeto pode ser executado utilizando o comando a seguir:
            python main_api.py

- Como usar o sistema
    Com tudo pronto, execute o projeto. O sistema irá pedir que você digite uma pergunta. Basta escrever a pergunta e pressionar Enter.

- Como o sistema responde
    A resposta será exibida na tela e incluirá:
    A explicação encontrada no documento
    A página do PDF onde a informação está
    Um trecho exato do texto usado como base
    Uma indicação se a resposta é confiável ou não

- O que o sistema não faz
    O sistema não inventa respostas, não utiliza a internet e não usa informações fora do documento fornecido. Se algo não estiver no PDF, ele informará que não encontrou a resposta.

- Possíveis mensagens de erro
    Caso a resposta demore muito, o sistema pode informar que o tempo foi excedido. Se a informação não existir no documento, a resposta indicará baixa confiança.

- Para que esse projeto é indicado
    Consulta rápida a código de ética
    Leitura orientada de normas internas
    Apoio a compliance e auditoria
    Consulta de regulamentos e políticas