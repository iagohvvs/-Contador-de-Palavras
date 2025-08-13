def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

if __name__ == "__main__":
    texto_usuario = input("Digite um texto: ")
    quantidade = contar_palavras(texto_usuario)
    print(f"O texto contém {quantidade} palavras.")