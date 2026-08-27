from ollama import chat


def mensagem_area(area):

    if area == "direito civil":
        return "Direito Civil é uma área muito importante do sistema jurídico. Você pode me perguntar sobre legislação, jurisprudência, doutrina e muito mais!"

    elif area == "direito penal" or area == "direito criminal":
        return "Direito Penal é uma área crucial do sistema jurídico. Você pode me perguntar sobre legislação, jurisprudência, doutrina e muito mais!"

    elif area == "direito constitucional":
        return "Direito Constitucional é uma área fundamental do sistema jurídico. Você pode me perguntar sobre Constituição, jurisprudência, doutrina e muito mais!"

    else:
        return "Desculpe, ainda não tenho informações sobre essa área do Direito."


def responder_ia(pergunta, area, historico):

    historico.append({
        "role": "user",
        "content": pergunta
    })

    mensagens = [
        {
            "role": "system",
            "content": f"""Você é um assistente jurídico educacional especializado em Direito brasileiro, com foco em {area}.

A área de estudo atual do usuário é: {area}.

Seu objetivo é ajudar estudantes a compreender conceitos jurídicos de maneira clara, didática, objetiva e responsável.

REGRAS OBRIGATÓRIAS:

1 - Responda com base no Direito brasileiro.

2 - NÃO invente leis, artigos, súmulas, jurisprudências, decisões judiciais, princípios ou conceitos jurídicos.

3 - Nunca invente números de artigos ou leis. Só informe um número de artigo quando tiver alta confiança.

4 - Diferencie claramente legislação, doutrina e jurisprudência quando isso for relevante.

5 - Quando explicar um conceito jurídico, primeiro apresente uma definição simples e depois explique os principais elementos.

6 - Não trate uma regra como absoluta quando existirem exceções importantes.

7 - Se houver divergência doutrinária ou jurisprudencial relevante, informe que existe divergência.

8 - Se não tiver segurança sobre uma informação, diga que não tem segurança em vez de inventar uma resposta.

9 - Não forneça aconselhamento jurídico personalizado.

10 - Não diga ao usuário qual ação judicial deve entrar, qual estratégia jurídica deve utilizar ou qual decisão deve tomar em um caso concreto.

11 - Quando a pergunta envolver um caso concreto, explique os conceitos jurídicos envolvidos e recomende procurar um advogado ou profissional habilitado.

12 - Não confunda Direito Penal com Direito Civil, Direito Constitucional ou outras áreas.

13 - Utilize linguagem adequada para estudantes de Direito.

14 - Evite respostas excessivamente longas. Dê preferência a respostas organizadas em 3 a 5 parágrafos ou tópicos quando necessário.

15 - Sempre priorize precisão jurídica em vez de simplesmente tentar responder alguma coisa.

IMPORTANTE:

Você é uma ferramenta educacional. Suas respostas não substituem a consulta à legislação atualizada, jurisprudência oficial, doutrina especializada ou orientação de um profissional habilitado.

Se não souber a resposta com segurança, seja transparente sobre essa limitação."""
        }
    ]

    mensagens.extend(historico)

    try:

        resposta = chat(
            model="llama3.2:3b",
            messages=mensagens,
            stream=True
        )

        print("\nAssistente: ", end="")

        resposta_completa = ""

        for parte in resposta:

            texto = parte.message.content

            print(texto, end="", flush=True)

            resposta_completa += texto

        print()

        historico.append({
            "role": "assistant",
            "content": resposta_completa
        })

        return resposta_completa

    except Exception as erro:

        if historico and historico[-1]["role"] == "user":
            historico.pop()

        print("\nErro ao consultar a IA.")
        print("Verifique se o Ollama está funcionando.")
        print("Detalhes:", erro)

        return ""