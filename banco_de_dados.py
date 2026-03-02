import sqlite3

def salvar_dados_no_banco(dados_novos):
    try:
        conexao = sqlite3.connect('precos_contabilizei.db')

        cursor = conexao.cursor()#cursor faz vc fazer comando sql, no python    

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS precos (
                horario TEXT,
                plano TEXT,
                preco REAL
            )
        ''')

        cursor.executemany('INSER   T INTO precos VALUES (?, ?, ?)', dados_novos) 
        # O executemany é usado para inserir vários dados de uma vez, ele recebe o comando sql e a lista de dados_novos, onde cada item da lista é uma tupla com os valores a serem inseridos. O ? é um placeholder que será substituído pelos valores da tupla.

        conexao.commit()# commit salva as alterações no banco
        conexao.close()# close fecha a conexão com o banco

        print("Dados salvos no banco de dados com sucesso!")
        
    except Exception as e:
        print(f"Erro ao salvar dados no banco: {e}")