import mysql.connector
from db_config import get_connection

def criar_banco_e_tabelas():
    conn_inicial = mysql.connector.connect(host="localhost", user="root", password="crud")
    cursor_inicial = conn_inicial.cursor()
    cursor_inicial.execute("CREATE DATABASE IF NOT EXISTS empresa_flores;")
    cursor_inicial.close()
    conn_inicial.close()

    conn = get_connection()
    cursor = conn.cursor()
    
    tabelas = [
        """
        CREATE TABLE IF NOT EXISTS Clien (
            idIdentClien INT PRIMARY KEY AUTO_INCREMENT,
            numCNPJClien VARCHAR(14),
            dscRzSocClien VARCHAR(100),
            dscNomFanClien VARCHAR(100),
            numTelefClien VARCHAR(15),
            dscTipLogClien VARCHAR(20),
            dscNomLogClien VARCHAR(100),
            numLograClien VARCHAR(10),
            dscComplClien VARCHAR(50),
            dscBairroClien VARCHAR(50),
            numCEPClien VARCHAR(8),
            dscCidadClien VARCHAR(50),
            dscEstadClien VARCHAR(2)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Funci (
            idIdentFunci INT PRIMARY KEY AUTO_INCREMENT,
            numMatriFunci VARCHAR(20),
            numCPFFunci VARCHAR(11),
            nomPessoFunci VARCHAR(100),
            numTelefFunci VARCHAR(15),
            dscTurnoFunci VARCHAR(20),
            dscTipLogFunci VARCHAR(20),
            dscNomLogFunci VARCHAR(100),
            numLograFunci VARCHAR(10),
            dscComplFunci VARCHAR(50),
            dscBairroFunci VARCHAR(50),
            numCEPFunci VARCHAR(8),
            dscCidadFunci VARCHAR(50),
            dscEstadFunci VARCHAR(2)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Forne (
            idIdentForne INT PRIMARY KEY AUTO_INCREMENT,
            numCNPJForne VARCHAR(14),
            dscRzSocForne VARCHAR(100),
            dscNomFanForne VARCHAR(100),
            numTelefForne VARCHAR(15),
            dscTipLogForne VARCHAR(20),
            dscNomLogForne VARCHAR(100),
            numLograForne VARCHAR(10),
            dscComplForne VARCHAR(50),
            dscBairroForne VARCHAR(50),
            numCEPForne VARCHAR(8),
            dscCidadForne VARCHAR(50),
            dscEstadForne VARCHAR(2),
            dscListaForne TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Mater (
            idIdentMater INT PRIMARY KEY AUTO_INCREMENT,
            codIdentMater VARCHAR(10),
            nomPessoMater VARCHAR(100),
            valUnitMater DECIMAL(10,2),
            dscUnidaMater VARCHAR(10),
            valDescMater DECIMAL(10,2),
            qtdMinimMater INT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Espec (
            idIdentEspec INT PRIMARY KEY AUTO_INCREMENT,
            codIdentEspec VARCHAR(10),
            nomPessoEspec VARCHAR(100),
            valHoraEspec DECIMAL(10,2)
        );
        """
    ]
    
    for instrucao_sql in tabelas:
        cursor.execute(instrucao_sql)
        
    conn.commit()
    cursor.close()
    conn.close()
    print("Banco e tabelas criados com sucesso.")

if __name__ == "__main__":
    criar_banco_e_tabelas()