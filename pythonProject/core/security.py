from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated = 'auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """"
    Função para verificar se a senha esta correta comparando com o texto
    e o hash da senha que está salvo no bd durante a criação da conta
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """"
    Função que gera o retorno da senha
    """
    return CRIPTO.hash(senha)