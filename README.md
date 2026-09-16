#Cifra de César em Python
Este projeto implementa a clássica **Cifra de César** utilizando a linguagem Pyhton. Desenvolvido como parte dos meus estudos fundamentais em **Segurança da Informação**, o script demonstra como funciona a manipulação de dados em baixo nivel através da tabela ASCII.
##Tecnologias Utilizadas:
-**Python 3** (Lógica de programação,laços de repetição e condicionais)
-**Git e GitHub** (Controle de versão e portfólio)
##Como Funciona
O algoritmo recebe uma mensagem do usuário e aplica um "salto" matemático fixo no alfabeto:
- Se o usuário digitar `REI` com uma chave de salto `3`, o sistema deslocará as letras gerando o texto cifrado `UHL`.
- O código foi projetado para diferenciar letras maiúsculas de minúsculas e preservar espaços, números e símbolos especiais.
## ⚠️ Nota de Segurança (Análise Crítica)
Como estudante de Segurança da Informação, tenho total consciência de que a Cifra de César é um método criptográfico **antigo e vulnerável**. Ele pode ser facilmente quebrado em milissegundos por um hacker utilizando **Ataques de Força Bruta (Brute Force)** ou **Análise de Frequência**. Este projeto possui fins estritamente educacionais para consolidar conceitos de criptografia simétrica clássica.