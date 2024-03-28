import os
import tabula
import pandas as pd
import zipfile

file_path = 'Anexo.pdf'

#Extraindo os dados das páginas com tabelas
all_tables = tabula.read_pdf(file_path, pages='3-180', lattice=True) 

#É necessário concatenar as tabelas pois elas vem separadas (uma tabela por página)
full_table = pd.concat(all_tables, ignore_index=True)

#Renomeando as colunas 'OD' e 'AMB' para seus respectivos valores e a coluna RN (alteração) para tirar a quebra de liinha
last_table = full_table.rename(columns={'RN\r(alteração)': 'RN (alteração)', 'OD': 'Seg. Odontologico', 'AMB': 'Seg. Ambulatorial'})

#Salvando a tabela completa em CSV e passando o separador de tabulação
last_table.to_csv('Anexo.csv', index=False)

csv_name = 'Anexo.csv'
zip_name = 'Teste_Leonam_Nunes.zip'

#Compactando a tabela zip
with zipfile.ZipFile(zip_name, 'w') as zp:
    zp.write(csv_name, os.path.basename(csv_name))
