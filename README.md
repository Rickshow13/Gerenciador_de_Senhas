# 🔒 Gerador e Validador de Senhas Seguras

Um aplicativo em linha de comando (CLI) desenvolvido em Python que gera senhas aleatórias altamente customizáveis e analisa em tempo real a força da senha gerada de acordo com as melhores práticas de segurança da informação.

## 🚀 Funcionalidades

- **Customização Total:** Escolha o tamanho da senha e quais tipos de caracteres incluir (Maiúsculas, Números e Símbolos).
- **Validador de Força:** Algoritmo integrado que analisa e classifica a senha em `Fraca`, `Moderada` ou `Forte`.
- **Análise Detalhada:** Exibe um checklist dos critérios de segurança atendidos pela senha gerada.
- **Persistência de Dados:** Opção para exportar a senha gerada de forma segura para um arquivo de texto local (`senhas_geradas.txt`).

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Biblioteca `random` (Geração pseudoaleatória)
- Biblioteca `re` (Expressões regulares para validação de segurança)
- Biblioteca `string` (Manipulação de blocos de caracteres padrão)

## 📦 Como Executar o Projeto

### Pré-requisitos
Você precisa ter o Python instalado na sua máquina. Caso não tenha, faça o download em [python.org](https://www.python.org/).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   ```

2. **Navegue até a pasta do projeto:**
   ```bash
   cd NOME-DO-REPOSITORIO
   ```

3. **Execute o script:**
   ```bash
   python Senha_Segura.py
   ```

## 📝 Exemplo de Uso

```text
========================================
🔒 GERADOR E VALIDADOR DE SENHAS SEGURAS 🔒
========================================
Digite o tamanho da senha (mínimo 4): 14
Incluir letras maiúsculas? (S/n): s
Incluir números? (S/n): s
Incluir caracteres especiais? (S/n): s

========================================
🔑 Senha Gerada: K9#mP!2sWq\$9tB
📊 Força da Senha: Forte 🟢
========================================
Análise de Segurança:
 ✅ Comprimento (8+ caracteres)
 ✅ Possui letras minúsculas
 ✅ Possui letras maiúsculas
 ✅ Possui números
 ✅ Possui caracteres especiais
========================================

Deseja salvar esta senha em um arquivo de texto? (S/n): s
💾 Senha salva com sucesso em 'senhas_geradas.txt'!
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido por [Seu Nome](https://github.com/SEU-USUARIO) 😊
