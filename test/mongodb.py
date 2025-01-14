from backend.connection.MongoDB import connect
import pytest

def test_mongodb_connection():
    # Teste se consegue criar conexão
    client = connect()
    assert client is not None
    
    # Verifica se conexão está ativa
    try:
        client.admin.command('ping')
        connection_ok = True
    except:
        connection_ok = False
    
    assert connection_ok == True
    
    # Fecha conexão
    client.close()
    
def test_mongodb_close_connection():
    client = connect()
    client.close()
    
    # Verifica se conexão foi fechada
    try:
        client.admin.command('ping')
        connection_closed = False
    except:
        connection_closed = True
        
    assert connection_closed == True