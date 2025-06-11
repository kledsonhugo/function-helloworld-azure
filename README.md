# function-helloworld-azure

Projeto de exemplo de Azure Functions em Python
==============================================

Este projeto demonstra como criar e executar uma Azure Function HTTP Trigger utilizando Python, seguindo as melhores práticas recomendadas pela Microsoft e pela comunidade Azure.

## Estrutura do Projeto
- `function_app.py`: Código principal da Azure Function.
- `requirements.txt`: Dependências do projeto.
- `local.settings.json`: Configurações locais para desenvolvimento.
- `host.json`: Configurações do host das Functions.
- `.vscode/`: Configurações para desenvolvimento no VS Code.
- `.venv/`: Ambiente virtual Python (não versionado).

## Pré-requisitos
- Python 3.11+
- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local) (v4+)
- [VS Code](https://code.visualstudio.com/) com a extensão [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) (opcional, mas recomendado)

## Como rodar o projeto localmente
1. **Clone o repositório:**
   ```zsh
   git clone <url-do-repositorio>
   cd function-helloworld-azure
   ```
2. **Crie o ambiente virtual:**
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Instale as dependências:**
   ```zsh
   pip install -r requirements.txt
   ```
4. **Inicie a Azure Function localmente:**
   ```zsh
   func start
   ```
5. **Acesse a função:**
   - Endpoint: `http://localhost:7071/api/v1?name=SeuNome`
   - Você pode passar o parâmetro `name` via query string ou no corpo da requisição (JSON).

## Como contribuir
1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção:
   ```zsh
   git checkout -b minha-contribuicao
   ```
3. Implemente sua alteração seguindo as melhores práticas de Python e Azure Functions.
4. Garanta que todos os testes e a execução local estejam funcionando.
5. Abra um Pull Request detalhando sua contribuição.

## Licença
Este projeto está licenciado sob a [GNU GPL v3](LICENSE).

## Observações e Boas Práticas
- Nunca inclua segredos ou credenciais no código ou no repositório.
- Use sempre o arquivo `local.settings.json` para configurações locais e nunca faça commit deste arquivo.
- Utilize sempre o modelo de programação mais recente (v2 para Python).
- Prefira autenticação via Managed Identity para recursos Azure.
- Consulte a [documentação oficial do Azure Functions](https://docs.microsoft.com/azure/azure-functions/) para mais detalhes.