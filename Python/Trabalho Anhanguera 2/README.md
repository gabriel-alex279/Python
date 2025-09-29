# 👨‍💻Meu Trabalho Anhanguera 3

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
![alt text](1-2.png)

Instalo o Flask e suas distribuições:
![alt text](2.png)

Crio um diretório chamado calculadora_salario_flask e depois crio e ativo um ambiente virtual:
![alt text](3.png)

Crio o arquivo app.py e implemento o código  do cálculo do salário:
![alt text](4.png)

Crio a pasta templates, adiciono o arquivo form.html no mesmo e adiciono o seguinte código:
![alt text](5.png)

Ao iniciar a aplicação, sou redirecionado para a URL local http://127.0.0.1:5000/, onde minha aplicação Flask está sendo executada diretamente no computador. 

O código aparenta estar funcionando corretamente. No navegador, é exibido um site com o título "Calculadora de Salário Líquido", contendo dois campos de entrada: um para inserir o salário bruto e outro para o número de dependentes. 

Após preencher os campos, é possível clicar em um botão para realizar o cálculo, e o resultado do salário líquido é exibido logo em seguida:
![alt text](tes1.png)

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

1° Teste :
![alt text](Exem1.png)

Resultado:
![alt text](Exem11.png)

2° Teste :
![alt text](Exem22-1.png)

Resultado:
![alt text](Exem2-1.png)

3° Teste :
![alt text](Exem3.png)

Resultado:
![alt text](Exem33.png)

4° Teste :
![alt text](Exem4.png)

Resultado:
![alt text](Exem44-1.png)

5° Teste :
![alt text](Exem5.png)

Resultado:
![alt text](Exem55.png)

6° e último Teste:
![alt text](Exem6.png)

Resultado:
![alt text](Exem66-1.png)

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

(App.py)[]
(form.html)[]