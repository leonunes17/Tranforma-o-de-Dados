# Transformação de Dados

Este script em Python visa extrair tabelas de um arquivo PDF fornecido, consolidá-las e salvá-las em um arquivo CSV. Além disso, ele compacta o arquivo CSV em um arquivo ZIP para facilitar o armazenamento e transporte.

## Requisitos

- Python 3.x
- Bibliotecas Python: `os`, `tabula`, `pandas`, `zipfile`

## Instalação de Dependências

Para executar este script, é necessário instalar as dependências do Python. Você pode instalá-las executando o seguinte comando:

```
pip install tabula-py pandas
```

## Uso

1. Certifique-se de ter o arquivo PDF (`Anexo.pdf`) no mesmo diretório que este script.
2. Execute o script Python.

```bash
python extrair_tabelas_pdf.py
```

O script irá realizar as seguintes operações:

1. Extrair tabelas das páginas 3 a 180 do arquivo PDF fornecido usando a biblioteca Tabula.
2. Concatenar as tabelas extraídas em uma única tabela.
3. Renomear as colunas para melhor legibilidade.
4. Salvar a tabela consolidada em um arquivo CSV (`Anexo.csv`) com separação de tabulação.
5. Compactar o arquivo CSV em um arquivo ZIP (`Teste_Leonam_Nunes.zip`).

## Personalização

- O nome do arquivo PDF fornecido está definido na variável `file_path`.
- As páginas a serem extraídas estão definidas em `pages='3-180'`, você pode ajustar conforme necessário.
- O nome do arquivo CSV e do arquivo ZIP compactado pode ser alterado nas variáveis `csv_name` e `zip_name`, respectivamente.

## Observações

- Certifique-se de que o arquivo PDF fornecido contenha tabelas nas páginas especificadas.
- Este script foi projetado para lidar com tabelas que estão organizadas em formato tabular nas páginas do PDF.
- Se as tabelas estiverem em um formato diferente ou houver variações significativas na estrutura das tabelas em diferentes páginas, podem ser necessários ajustes adicionais no código.

**Nota:** Este script é fornecido como está, e o autor não se responsabiliza por quaisquer problemas decorrentes de seu uso inadequado ou de modificações. É recomendável testar o script com diferentes tipos de arquivos PDF e revisar os resultados gerados para garantir a precisão e integridade dos dados extraídos.
```
