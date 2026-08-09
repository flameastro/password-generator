import secrets

# ! Deixar tudo em inglês.


def criptografar_senha(tamanho: int = 64, numeros: bool = True, especiais: bool = True):
    if tamanho < 6 or tamanho > 256:
        return "O tamanho deve estar entre 6 a 256. Tente novamente"

    # Caracteres disponíveis separados por tipos
    MINUSCULOS = "abcdefghijklmnopqrstuvwxyz"
    MAIUSCULOS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMEROS = "0123456789"
    ESPECIAIS = "!@#$%^&*()-_=+?"

    # Adiciona os caracteres permitidos
    caracteres = MINUSCULOS + MAIUSCULOS
    if numeros:
        caracteres += NUMEROS
    if especiais:
        caracteres += ESPECIAIS

    # Gera a senha
    senha = ""
    for _ in range(tamanho):
        senha += secrets.choice(caracteres)

    return senha


ARQUIVO = "senhas.txt"
tamanho = int(input("Insira o tamanho da senha (entre 1 a 256): "))
numeros = bool(
    input(
        "Permitir números? (Digite qualquer tecla e aperte ENTER se sim ou se não deixe em branco)"
    )
)
especiais = bool(
    input(
        "Permitir caracteres especiais? Exemplo: !@#$%^&*()-_=+? (Digite qualquer tecla e aperte ENTER se sim ou se não deixe em branco)"
    )
)
quantidade = int(
    input(f"Quantas senhas deseja gerar com o tamanho de {tamanho} caracteres?: ")
)

if quantidade > 1 and quantidade < 100:
    salvar = bool(
        f"Deseja salvar as {quantidade} senhas geradas num arquivo senhas.txt? (Digite qualquer tecla e aperte ENTER se sim ou se não deixe em branco): "
    )

    for x in range(quantidade):
        senha = criptografar_senha(tamanho, numeros, especiais)
        print(senha)

        if salvar:
            with open(ARQUIVO, "a+", encoding="utf-8") as f:
                f.write(f"{senha}\n")
