# Extração e Manipulação de Dados de Livros

Este projeto realiza a extração de dados de livros de um site de exemplo, utilizando a biblioteca `requests` para fazer requisições HTTP e `BeautifulSoup` para parsear o HTML.

## Requisitos

Antes de executar o código, certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar as bibliotecas necessárias. Você pode fazer isso usando o `pip`:

```bash
pip install requests beautifulsoup4
Descrição
O código realiza as seguintes operações:

Faz uma requisição para o site Books to Scrape.
Extrai o título e o preço de cada livro disponível na página.
Armazena as informações em um dicionário e as adiciona a uma lista.
Imprime a quantidade total de livros e seus detalhes.
Como Usar
Clone este repositório ou copie o código em um arquivo Python.
Execute o script:
bash
Copiar código
python nome_do_arquivo.py
O script imprimirá a quantidade de livros e a lista com os títulos e preços.
Exemplo de Saída
makefile
Copiar código
Quantidade de livros: 20
Título: A Light in the Attic, Preço: £51.77
Título: Tipping the Velvet, Preço: £53.74
...
Contribuição
Sinta-se à vontade para fazer fork deste repositório e enviar pull requests para melhorias.

import requests
from bs4 import BeautifulSoup

# Desabilitar avisos de segurança
requests.packages.urllib3.disable_warnings()

# URL do site
url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

# Extrair o conteúdo da página
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Inicializar variáveis
contar_livros = 0
catalogo = []

# Encontrar todas as tags <article> que contêm os livros
for artigo in extracao.find_all('article'):
    livro = {}

    # Encontrar o título do livro extraindo o texto da tag <a>
    titulo = artigo.find('h3').find('a').text
    livro['Título'] = titulo  # Armazenar o título completo

    # Encontrar o preço do livro
    preco = artigo.find('p', class_='price_color').text
    livro['Preço'] = preco

    # Adicionar o livro ao catálogo
    catalogo.append(livro)

    # Incrementar a contagem de livros
    contar_livros += 1

# Imprimir a quantidade de livros
print(f'Quantidade de livros: {contar_livros}')

# Mostrar os livros
for livro in catalogo:
    print(f'Título: {livro["Título"]}, Preço: {livro["Preço"]}')

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Copiar código

Sinta-se à vontade para modificar qualquer parte que deseje!
