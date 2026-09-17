# 🔒 Meus Estudos de Criptografia Simétrica em Python

Este repositório centraliza meus estudos fundamentais em **Segurança da Informação e Programação**. Aqui, implemento e analiso algoritmos de criptografia clássica para entender a manipulação de dados em baixo nível e a evolução da segurança de dados.

## 🛠️ Tecnologias Utilizadas
- **Python 3**: Utilização de laços de repetição (`for`), condicionais (`if/elif/else`), tratamento de strings e funções nativas como `ord()` e `chr()`.
- **Git & GitHub**: Controle de versão, alinhamento de ramificações e gerenciamento de portfólio técnico.

---

## 🧮 Projetos Implementados

### 1. Cifra de César (`cifra_de_cesar.py`)
O algoritmo recebe uma mensagem e aplica um "salto" matemático numérico fixo e estático em todo o alfabeto.
* **Exemplo**: A mensagem `REI` com chave `3` desloca as letras gerando o texto cifrado `UHL`.

### 2. Cifra de Vigenère (`cifra_de_vigenere.py`)
Uma evolução direta da Cifra de César. Em vez de usar um número fixo, utiliza uma **palavra-chave secreta** onde cada letra dita um salto dinâmico diferente para a mensagem, utilizando a fórmula matemática do resto da divisão (`%`) com base no tamanho da chave (`len`).
* **Exemplo**: A mensagem `REI` combinada com a palavra-chave `FOGO` altera a lógica do salto a cada caractere processado.

---

## ⚠️ Nota de Segurança (Análise Crítica de Vulnerabilidades)
Como estudante de **Segurança da Informação**, tenho total consciência de que ambos os métodos criptográficos são **obsoletos e inseguros** para os padrões atuais (2026). 
- A Cifra de César é facilmente quebrada em milissegundos por **Ataques de Força Bruta (Brute Force)**.
- A Cifra de Vigenère, embora mascare a análise de frequência simples, é vulnerável a análises estatísticas avançadas (como o Exame de Kasiski) caso o texto cifrado seja longo.

*Estes scripts possuem objetivos estritamente educacionais para consolidar conceitos de criptografia clássica antes do avanço para algoritmos modernos de mercado, como o AES (Advanced Encryption Standard).*
