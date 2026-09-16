# PARTE 1: DEFINIÇÃO DO MOTOR DA CRIPTOGRAFIA (A FUNÇÃO)
def cifra_de_vigenere(texto, chave): # criando uma função
    # 'resultado' nasce vazio para acumular as letras criptografadas uma por uma
    resultado = "" 
    # Transforma a palavra-chave em maiúsculas para podermos usar sempre a base -65
    chave = chave.upper() 
    # Variável manual que controla qual letra da palavra-chave usaremos no momento
    indice_chave = 0
    # O loop 'for' percorre a mensagem do usuário caractere por caractere
    for caractere in texto:
        # O sensor '.isalpha()' checa se o caractere atual é uma letra do alfabeto
        if caractere.isalpha():
            # A matemática do '%' impede o índice de estourar o tamanho da palavra-chave
            salto = ord(chave[indice_chave % len(chave)]) - 65
            
            # --- TUDO ISSO ABAIXO DEVE FICAR DENTRO DO ISALPHA (RECUADO) ---
            if caractere.isupper():
                codigo_ascii = ord(caractere)
                novo_codigo = (codigo_ascii - 65 + salto) % 26 + 65
                resultado += chr(novo_codigo)
            elif caractere.islower():
                codigo_ascii = ord(caractere)
                novo_codigo = (codigo_ascii - 97 + salto) % 26 + 97
                resultado += chr(novo_codigo)
                
            # O índice soma +1 fora do isupper/islower, mas ainda dentro do isalpha
            indice_chave += 1
            
        else:
            # O else fica alinhado com o primeiro 'if caractere.isalpha():'
            resultado += caractere
            
    return resultado        


print("----SISTEMA DE CRIPTOGRAFIA VIGENÈRE----")
texto_usuario = input("Digite a sua mensagem: ")
chave_usuario = input("Digite a chave secreta: ")
texto_criptografado = cifra_de_vigenere(texto_usuario, chave_usuario)
print(f"Mensagem protegida: {texto_criptografado}")
