import random
import re
import string


def gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_simbolos):
    """Gera uma senha aleatória com base nos critérios escolhidos."""
    caracteres = string.ascii_lowercase

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Garante que a senha use apenas os caracteres selecionados
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def avaliar_forca(senha):
    """Avalia a força da senha de 0 a 5 com base em critérios de segurança."""
    pontuacao = 0
    regras = {
        "Comprimento (8+ caracteres)": len(senha) >= 8,
        "Possui letras minúsculas": bool(re.search(r"[a-z]", senha)),
        "Possui letras maiúsculas": bool(re.search(r"[A-Z]", senha)),
        "Possui números": bool(re.search(r"[0-9]", senha)),
        "Possui caracteres especiais": bool(re.search(r"[{}]".format(re.escape(string.punctuation)), senha)),
    }

    pontuacao = sum(regras.values())

    if pontuacao <= 2:
        nivel = "Fraca 🔴"
    elif pontuacao <= 4:
        nivel = "Moderada 🟡"
    else:
        nivel = "Forte 🟢"

    return nivel, regras


def salvar_em_arquivo(senha):
    """Salva a senha gerada em um arquivo local txt."""
    try:
        with open("senhas_geradas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{senha}\n")
        print("💾 Senha salva com sucesso em 'senhas_geradas.txt'!")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


def obter_resposta_booleana(mensagem):
    """Valida entradas do usuário para sim/não."""
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["s", "sim", ""]:
            return True
        if resposta in ["n", "nao", "não"]:
            return False
        print("❌ Resposta inválida. Digite 'S' para Sim ou 'N' para Não.")


def main():
    print("=" * 40)
    print("🔒 GERADOR E VALIDADOR DE SENHAS SEGURAS 🔒")
    print("=" * 40)

    # Entrada e validação do tamanho
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
            if tamanho >= 4:
                break
            print("❌ A senha deve ter pelo menos 4 caracteres para garantir a estrutura.")
        except ValueError:
            print("❌ Por favor, digite um número inteiro válido.")

    # Opções de customização
    maiusculas = obter_resposta_booleana("Incluir letras maiúsculas? (S/n): ")
    numeros = obter_resposta_booleana("Incluir números? (S/n): ")
    simbolos = obter_resposta_booleana("Incluir caracteres especiais? (S/n): ")

    # Geração
    senha_final = gerar_senha(tamanho, maiusculas, numeros, simbolos)

    # Avaliação
    forca, checklist = avaliar_forca(senha_final)

    # Exibição dos resultados
    print("\n" + "=" * 40)
    print(f"🔑 Senha Gerada: {senha_final}")
    print(f"📊 Força da Senha: {forca}")
    print("=" * 40)
    print("Análise de Segurança:")
    for criterio, passou in checklist.items():
        status = "✅" if passou else "❌"
        print(f" {status} {criterio}")
    print("=" * 40)

    # Opção de salvamento
    if obter_resposta_booleana("\nDeseja salvar esta senha em um arquivo de texto? (S/n): "):
        salvar_em_arquivo(senha_final)

    print("\nObrigado por usar o Gerador de Senhas! Cuidado com a sua segurança digital. 👋")


if __name__ == "__main__":
    main()
