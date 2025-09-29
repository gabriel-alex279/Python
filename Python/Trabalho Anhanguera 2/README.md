# 👨‍💻Meu Trabalho Anhanguera 2

## OBJETIVOS:

✓ Capacitar o aluno a desenvolver uma aplicação web interativa utilizando o framework Flask, aplicando regras de negócio e validações. A prática permitirá ao aluno criar uma calculadora de salário líquido com base em regras simplificadas da CLT, além de reforçar a importância do tratamento de erros em aplicações web.


## SOLUÇÃO DIGITAL:

• [Flask (Python)](https://flask.palletsprojects.com/en/2.3.x/installation/)

O Flask é um microframework de desenvolvimento web em Python, conhecido pela sua simplicidade e flexibilidade. Diferente de frameworks mais robustos como o Django, o Flask foca em fornecer apenas os componentes essenciais para construir aplicações web

## PROCEDIMENTO/ATIVIDADE PROPOSTA:

Inserir o nome do experimento: Calculadora de Salário Líquido com Flask.

Desenvolver um aplicativo Android com um formulário de cadastro de produtos que armazena os dados em SQLite e os exibe em uma lista.

Criar uma aplicação Flask com formulário de entrada de dados do salário bruto e número de dependentes. A aplicação deve calcular e exibir o salário líquido com base nas seguintes regras: 

• O INSS será descontado com uma alíquota fixa de 8% sobre o salário bruto. 

• O Imposto de Renda (IR) deve ser descontado apenas se o salário bruto for superior a R$ 2.500,00, com uma alíquota de 15% sobre o valor total.
  
• Para cada dependente informado, será concedido um desconto fixo de R$ 200,00, que será adicionado ao salário líquido (ou seja, representa uma dedução da base de descontos). 

• O resultado final deve ser exibido como salário líquido, isto é: salário bruto menos o valor do INSS menos o valor do IR (se aplicável) mais o valor referente aos dependentes. 

• A aplicação deve tratar casos de erro, como: o Salário negativo o Número de dependentes negativo o Entradas não numéricas


## CHECKLIST:

● Implementar a função de cálculo do salário líquido; 

● Criar o formulário com entrada de salário e dependentes;

● Tratar entradas inválidas ou valores negativos; 

● Executar a aplicação Flask localmente; 

● Acessar via navegador e preencher com diferentes valores; 

● Registrar os dados de entrada e saída; 

● Analisar os resultados e responder às questões propostas.


Aqui eu acesso o PyCharm Community e crio um novo projeto:
<img width="1023" height="730" alt="1" src="https://github.com/user-attachments/assets/445f9e30-f6cd-45ba-8d44-54295a5a7db2" />


Instalo o Flask e suas distribuições:
<img width="1023" height="729" alt="2" src="https://github.com/user-attachments/assets/986f1fc0-45f2-4cd4-9785-9dacedd73a5c" />

Crio um diretório chamado calculadora_salario_flask e depois crio e ativo um ambiente virtual:
<img width="1023" height="731" alt="3" src="https://github.com/user-attachments/assets/010f92b3-572f-4bd3-a28f-d3bae59815d7" />

Crio o arquivo app.py e implemento o código  do cálculo do salário:
<img width="1023" height="728" alt="4" src="https://github.com/user-attachments/assets/b661d6e3-21db-4453-b1f7-91e1d652ebcf" />

Crio a pasta templates, adiciono o arquivo form.html no mesmo e adiciono o seguinte código:
<img width="1023" height="728" alt="5" src="https://github.com/user-attachments/assets/6a841e93-aadd-4861-bfee-8d882b43fafe" />

Ao iniciar a aplicação, sou redirecionado para a URL local http://127.0.0.1:5000/, onde minha aplicação Flask está sendo executada diretamente no computador. 

O código aparenta estar funcionando corretamente. No navegador, é exibido um site com o título "Calculadora de Salário Líquido", contendo dois campos de entrada: um para inserir o salário bruto e outro para o número de dependentes. 

Após preencher os campos, é possível clicar em um botão para realizar o cálculo, e o resultado do salário líquido é exibido logo em seguida:
<img width="470" height="207" alt="tes1" src="https://github.com/user-attachments/assets/9cebbfd5-58c3-4d1e-a8f7-38cd9e42294d" />

Agora, seguindo com o enunciado, vou preencher a tabela abaixo com os dados testados e os resultados observados:

| Salário Bruto | Dependentes | Resultado                             |
|---------------|-------------|---------------------------------------|
| 3000,00       | 2           | ?                                     |
| 2000,00       | 1           | ?                                     |
| 1000,00       | 0           | ?                                     |
| -500,00       | 1           | ?                                     |
| abc           | 2           | ?                                     |
| 2500          | -1          | ?                                     |


Aqui estão os dados obtidos:

1° Teste:
<img width="1023" height="607" alt="Exem1" src="https://github.com/user-attachments/assets/a04b4cc1-e296-4171-9b5e-065d5610c412" />

Resultado:

<img width="508" height="85" alt="Exem11" src="https://github.com/user-attachments/assets/78f4718e-2e7e-41d8-8fc8-bd9f67931a37" />

2° Teste:
<img width="1023" height="609" alt="Exem22" src="https://github.com/user-attachments/assets/af7ae2d0-1616-445e-9335-2672d45087bf" />

Resultado:

<img width="505" height="91" alt="Exem2" src="https://github.com/user-attachments/assets/adf28635-b68a-47c2-80f6-fb7819a72b7d" />

3° Teste:
<img width="1023" height="606" alt="Exem3" src="https://github.com/user-attachments/assets/3fc3d69b-3bb9-49ca-80e8-13ad266e1edc" />

Resultado:

<img width="495" height="94" alt="Exem33" src="https://github.com/user-attachments/assets/b9c88220-4305-43a7-a075-6984178f59ed" />

4° Teste:
<img width="1023" height="607" alt="Exem4" src="https://github.com/user-attachments/assets/06dc2256-581b-46a9-89f9-1f1f36732084" />

Resultado:

<img width="641" height="103" alt="Exem44" src="https://github.com/user-attachments/assets/9b276609-3922-45fc-80a0-4f1a7678b166" />

5° Teste:
<img width="1023" height="608" alt="Exem5" src="https://github.com/user-attachments/assets/e46b630e-f079-4fcd-940b-77abb5090801" />

Resultado:

<img width="929" height="105" alt="Exem55" src="https://github.com/user-attachments/assets/b952d6ad-c0b7-4785-acd3-f0762286fde1" />

6° e último Teste:
<img width="1023" height="607" alt="Exem6" src="https://github.com/user-attachments/assets/fba27de2-36db-4c9f-801b-5569cac5f65d" />

Resultado:

<img width="907" height="101" alt="Exem66" src="https://github.com/user-attachments/assets/0eae2dfb-b9ea-493a-bcbf-31e3020f7ba5" />

### Tabela completa com os resultados obtidos:

| Salário Bruto | Dependentes | Resultado                             |
|---------------|-------------|---------------------------------------|
| 3000,00       | 2           | R$ 2710,00                            |
| 2000,00       | 1           | R$ 2040,00                            |
| 1000,00       | 0           | R$ 920,00                             |
| -500,00       | 1           | Erro: Salário não pode ser negativo.  |
| abc           | 2           | Erro: Insira valores válidos para salário e dependentes. |
| 2500          | -1          | Erro: Número de dependentes não pode ser negativo. |

### Com os dados obtidos e calculados, responda:

#### 1 - Com base nos seus conhecimentos, qual a vantagem de validar os dados do formulário no backend? Justifique.

A validação no backend é essencial, pois o frontend pode ser burlado e permitir o envio de dados inválidos ao servidor.

Garante que apenas dados válidos sejam processados, prevenindo erros de lógica e falhas na aplicação.

Protege o sistema contra ataques, como injeções de dados maliciosos.

Centraliza as regras de negócio, mantendo as validações e a lógica sob controle no backend.

#### 2 - Considerando que o salário líquido depende de várias variáveis (IR, INSS, dependentes), o que seria mais indicado para facilitar futuras atualizações da regra de cálculo? Reflita sobre sua resposta.

Separar a lógica de cálculo das demais partes do sistema, centralizando-a em um único local, como uma função.

Isso torna o sistema mais flexível, fácil de manter e preparado para evoluções futuras.

## RESULTADOS DE APRENDIZAGEM:

Ao final da atividade, fui capaz de desenvolver uma aplicação web funcional utilizando o framework Flask, com uma interface de entrada, regras de negócio aplicadas e respostas dinâmicas. O exercício me ajudou a exercitar o raciocínio lógico na implementação de cálculos e validações, além de reforçar boas práticas no tratamento de erros. Também pude perceber a importância de separar as regras de negócio da camada de apresentação, o que resultou em um código mais limpo, organizado e fácil de manter. Essa prática me deu uma base sólida para construir aplicações web mais robustas e com múltiplas regras de negócio.


## CÓDIGOS COMPLETO:

[app.py](https://github.com/gabriel-alex279/Python/blob/main/Python/Trabalho%20Anhanguera%202/C%C3%B3digos/app.py)

[form.html](https://github.com/gabriel-alex279/Python/blob/main/Python/Trabalho%20Anhanguera%202/C%C3%B3digos/form.html)
