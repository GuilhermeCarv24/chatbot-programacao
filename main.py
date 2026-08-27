from chatbot import mensagem_area, responder_ia


print("=" * 55)
print("        Assistente Jurídico Educacional")
print("=" * 55)

print("\nOlá! Eu sou seu assistente jurídico.")

nome = input("Qual seu nome? ").strip()

if nome:
    print(f"Prazer em te conhecer, {nome}!")
else:
    print("Prazer em te conhecer!")


area = input("\nQual área de Direito você está estudando? ").strip().lower()

print()

mensagem = mensagem_area(area)

print(mensagem)

print("\nComandos disponíveis:")
print("- sair: encerra o programa")
print("- limpar: limpa o histórico da conversa")
print("- area: mostra a área atual")
print()

historico = []


while True:

    pergunta = input("Você: ").strip()

    if not pergunta:
        continue

    pergunta_lower = pergunta.lower()

    if pergunta_lower == "sair":

        print("\nObrigado por usar o Assistente Jurídico! Até a próxima!")
        break

    elif pergunta_lower == "limpar":

        historico.clear()

        print("\nHistórico da conversa apagado.")
        print("Podemos começar uma nova conversa.\n")

    elif pergunta_lower == "area":

        print(f"\nÁrea atual: {area}\n")

    else:

        responder_ia(pergunta, area, historico)