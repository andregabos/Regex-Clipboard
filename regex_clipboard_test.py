#! python3

from regex_clipboard import extract_urls, extract_phones , extract_emails, standardize_dates, remove_sensitive_info, fix_typos

def test_script():
    test_data = """
    Visite nosso site em https://www.exemplo.com.br ou http://exemplo.org
    Meu aniversário é em 14/03/2019 e o dela é 05-22-1995
    SSN: 123-45-6789 Cartão de Crédito: 1234-5678-9012-3456
    Este  é  um   teste com    múltiplos espaços e palavras palavras repetidas!!
    Contate-nos em contato@exemplo.com ou suporte@exemplo.com.br
    Ligue para (11) 98765-4321 ou +55 21 99999-9999
    """
    
    print("Teste de URLs:")
    print(extract_urls(test_data))
    
    print("\nTeste de Datas:")
    print(standardize_dates(test_data))
    
    print("\nTeste de Informações Sensíveis:")
    print(remove_sensitive_info(test_data))
    
    print("\nTeste de Correção de Erros de Digitação:")
    print(fix_typos(test_data))
    
    print("\nTeste de Extração de E-mails:")
    print(extract_emails(test_data))
    
    print("\nTeste de Extração de Telefones:")
    print(extract_phones(test_data))
    

if __name__ == "__main__":
    test_script()

