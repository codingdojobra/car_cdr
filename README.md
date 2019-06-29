# `car` & `cdr`
Resolução de um dos desafios do [Daily Coding Problems](https://www.dailycodingproblem.com).

> `cons(a, b)` constructs a pair, and `car(pair)` and `car(pair)`
> returns the first and last element if that pair.
> For example, `car(cons(3, 4))` returns 3, and `cdr(cons(3, 4))` returns 4.
> Given this implementation of cons:
```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
> Implement `car` and `cdr`


# Quer submeter outra solução?
- clone este repositório
```sh
git clone https://github.com/codingdojobra/calculando_estatisticas_simples
```

- crie um novo branch para a sua solução
```sh
git checkout -b UM_NOME_SIGNIFICATIVO_PARA_SEU_BRANCH
```

- desenvolva sua solução XD

- se quiser, descreva melhor a ideia da sua solução no README do seu branch.

- adicione e commite suas mudanças
```sh
git add .
```
```
git commit -m "Uma mensagem curta e descritiva sobre sua solução."
```

- volte para o branch master
```sh
git checkout master
```

- edite o README no master para adicionar sua solução, siga o modelo
> **NOME_DO_SEU_BRANCH:** solução desenvolvida por @SEU_USUARIO implementando
> [BREVE DESCRIÇÃO DA IDEIA].

- adicione e commite
```sh
git commit -am "Adiciona nova solução no branch TAL desenvolvida por @SEU_USER."
```
