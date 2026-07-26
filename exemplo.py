class ContextoSimples:
    def __enter__(self):
        print('iniciar conexao')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando conexao com segurança!')


with ContextoSimples() as cs:
    print('execuções em banco de dados')