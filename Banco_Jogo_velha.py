import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        conexao = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conexao
    except Exception as erro:
        print("Erro ao conectar:", erro)
        return None


def salvar_partida(vencedor, modo_jogo, qtd_jogadas):
    conexao = conectar()
    
    if conexao is None:
        return
    
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO partidas (vencedor, horario, modo_jogo, qtde_jogadas)
            VALUES (%s, NOW(), %s, %s)
        """, (vencedor, modo_jogo, qtd_jogadas))
        
        conexao.commit()
        print("Partida salva com sucesso!")
    
    except Exception as erro:
        print("Erro ao salvar partida:", erro)
    
    finally:
        cursor.close()
        conexao.close()


def listar_partidas():
    conexao = conectar()
    
    if conexao is None:
        print("\n(Histórico indisponível - banco de dados não configurado)")
        return
    
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
            SELECT id, vencedor, modo_jogo, qtde_jogadas, horario
            FROM partidas
            ORDER BY horario DESC
            LIMIT 5
        """)
        
        partidas = cursor.fetchall()
        
        print("\n --- HISTÓRICO --- ")
        
        if not partidas:
            print("Nenhuma partida registrada.")
        else:
            for p in partidas:
                data_formatada = p[4].strftime("%d/%m/%Y %H:%M")
                print(f"Partida {p[0]} | Vencedor: {p[1]} | Modo: {p[2]} | Jogadas: {p[3]} | Data: {data_formatada}")
    
    except Exception as erro:
        print("Erro ao buscar partidas:", erro)
    
    finally:
        cursor.close()
        conexao.close()




