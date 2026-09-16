def cifra_de_cesar(texto, salto):
    resultado = ""
    for caractere in texto:
        if caractere.isupper():
            codigo_ascii = ord(caractere)
            novo_codigo = (codigo_ascii - 65 + salto) % 26 + 65
            resultado += chr(novo_codigo)
        elif caractere.islower():
            codigo_ascii = ord(caractere)
            novo_codigo = (codigo_ascii - 97 + salto) % 26 + 97
            resultado += chr(novo_codigo)
        else:
            resultado += caractere
    return resultado         

print("---SISTEMA DE CRIPTOGRAFIA---")
texto_usuario = input("Digite a sua mensagem: ")
salto_usuario = int(input("Digite o número de salto: "))
texto_criptografado = cifra_de_cesar (texto_usuario, salto_usuario)
print(f"Mensagem Protegida: {texto_criptografado}")