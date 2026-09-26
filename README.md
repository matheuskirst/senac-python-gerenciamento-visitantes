# Exercício — Central de Visitantes do Parque

## Contexto

Você foi contratado para desenvolver o sistema de gerenciamento de visitantes de um grande parque de diversões.

O sistema deverá permitir cadastrar, remover, listar, ordenar, filtrar e consultar visitantes.

---

## 1. Menu principal

O programa deverá apresentar continuamente o seguinte menu:

```text
========================================
              PARQUE AVENTURA
========================================

1 - Cadastrar visitante
2 - Remover visitante
3 - Listar visitantes
4 - Ordenar visitantes
5 - Filtrar visitantes
6 - Consultar visitante
0 - Encerrar programa

Escolha uma opção:
```

O menu deverá continuar sendo apresentado até que o usuário escolha a opção **0 - Encerrar programa**.

---

## 2. Cadastro de visitante

Cada visitante deverá possuir as seguintes informações:

- Nome
- Data de nascimento
- CPF
- Tipo de ingresso
- Data da visita
- Número do ingresso

Os tipos de ingresso disponíveis são:

```text
1 - Normal
2 - VIP
3 - Premium
```

O número do ingresso deverá ser gerado automaticamente utilizando `UUID`.
Deve ter validação evitando campos vazios ou campos com valores inválidos.

---

## 3. Validação de CPF

Antes de cadastrar um visitante, o sistema deverá verificar se já existe um visitante cadastrado com o mesmo CPF.

O CPF deverá ser considerado o **identificador único do visitante**.

Caso já exista um visitante com o CPF informado:

```text
Já existe um visitante cadastrado com este CPF.

O cadastro não foi realizado.
```

O visitante não deverá ser adicionado à lista.

Caso o CPF ainda não esteja cadastrado, o visitante poderá ser adicionado normalmente.

---

## 4. Remover visitante

A remoção deverá ser realizada utilizando o CPF do visitante.

O sistema deverá solicitar o CPF.

Caso o visitante seja encontrado:

```text
Visitante removido com sucesso!
```

Caso não seja encontrado:

```text
Nenhum visitante encontrado com esse CPF.
```

---

## 5. Listar visitantes

A opção de listagem deverá apresentar apenas as seguintes informações:

- Nome
- Idade
- Tipo de ingresso

Exemplo:

```text
========================================
               VISITANTES
========================================

Nome: João da Silva
Idade: 26
Ingresso: VIP

Nome: Maria Souza
Idade: 19
Ingresso: Normal

Nome: Pedro Oliveira
Idade: 34
Ingresso: Premium
```

O CPF, a data de nascimento, a data da visita e o número do ingresso não deverão ser exibidos nessa listagem.

---

## 6. Ordenar visitantes

O sistema deverá permitir que o usuário escolha como deseja ordenar os visitantes.

O menu deverá apresentar:

```text
========================================
              ORDENAR VISITANTES
========================================

1 - Ordenar por nome
2 - Ordenar por idade

Escolha:
```

## 7. Filtrar visitantes por tipo de ingresso

O sistema deverá permitir visualizar somente os visitantes que possuem determinado tipo de ingresso.

O usuário deverá escolher:

```text
========================================
              FILTRO DE INGRESSOS
========================================

1 - Normal
2 - VIP
3 - Premium

Escolha:
```

Por exemplo, ao escolher `VIP`, o sistema deverá apresentar somente os visitantes VIP:

```text
VISITANTES VIP

João da Silva - 26 anos
Carlos Santos - 31 anos
Mariana Oliveira - 24 anos
```

Caso não exista nenhum visitante com o tipo de ingresso escolhido:

```text
Nenhum visitante encontrado.
```

---

## 8. Consultar visitante pelo CPF

O usuário deverá conseguir consultar um único visitante informando seu CPF.

Nessa consulta, deverão ser apresentadas todas as informações do visitante:

```text
========================================
              INGRESSO ENCONTRADO
========================================

Nome: João da Silva
Idade: 26 anos
CPF: 12345678900
Data de nascimento: 12/05/2000
Ingresso: VIP
Data da visita: 20/09/2026

Número do ingresso:
550e8400-e29b-41d4-a716-446655440000
```

Caso o CPF não esteja cadastrado:

```text
Visitante não encontrado.
```

---

## 9. Encerrar programa

Ao escolher a opção 7, o programa deverá ser encerrado.

---

## 10. Extra: Salvar visitantes em arquivo json
Salvar visitantes cadastrados em um arquivo json para manter a persistência dos dados.
Ao listar os visitantes, deve ler desse arquivo json.

## 11. Controle de data da visita

O sistema deverá validar a data da visita informada pelo usuário.

- A data não poderá ser anterior à data atual.
- O sistema deverá aceitar somente datas válidas.
- Caso seja informada uma data inválida, deverá apresentar:

```text
Data da visita inválida.

Informe uma data igual ou posterior à data atual.
```

## 12. Consultar visitantes por data da visita

O sistema deverá possuir uma nova opção no menu para consultar os visitantes que possuem uma determinada data de visita.

O menu deverá ser atualizado para:
```text
========================================
             PARQUE AVENTURA
========================================

1 - Cadastrar visitante
2 - Remover visitante
3 - Listar visitantes
4 - Ordenar visitantes
5 - Filtrar visitantes
6 - Consultar visitante
7 - Consultar por data da visita
0 - Encerrar programa

Escolha uma opção:
```

O sistema deverá solicitar uma data e apresentar os visitantes que irão ao parque naquele dia.

Exemplo:

```text
========================================
       VISITANTES DO DIA 20/09/2026
========================================

João da Silva - 26 anos - VIP
Maria Souza - 19 anos - Normal
Pedro Oliveira - 34 anos - Premium

Caso não existam visitantes para a data informada:

Nenhum visitante encontrado para esta data.
```

## 13. Estatísticas dos visitantes

O sistema deverá possuir uma opção para apresentar um resumo estatístico dos visitantes cadastrados.

Deverá apresentar:

- Total de visitantes;
- Quantidade de ingressos Normal;
- Quantidade de ingressos VIP;
- Quantidade de ingressos Premium;
- Média de idade dos visitantes.

Exemplo:
```text
========================================
          ESTATÍSTICAS DO PARQUE
========================================

Total de visitantes: 25

Ingressos Normal: 10
Ingressos VIP: 8
Ingressos Premium: 7

Média de idade: 27,4 anos

Caso não existam visitantes cadastrados:

Não existem visitantes cadastrados para gerar estatísticas.
```