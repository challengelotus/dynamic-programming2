# 🧪 Projeto de Fusão e Ordenação de Exames

![Link do projeto no GitHub](https://github.com/challengelotus/dynamic-programming2)

Este projeto tem como objetivo **ler, transformar, combinar e ordenar dados de exames laboratoriais** provenientes de diferentes fontes (JSON e CSV).
Além disso, foram implementados algoritmos fundamentais de **ordenação, busca, fila e pilha** para consolidar conceitos de **Estruturas de Dados**.

---

## 📂 Estrutura do Projeto

```
.
├── src/
│   ├── fusao_exames.py          # Script principal (ETL + ordenação + buscas + fila + pilha)
│   ├── processamento_dados.py   # Classe Dados (métodos de manipulação)
├── data/
│   ├── raw/                        # Dados brutos (JSON e CSV de entrada)
│   ├── processed/                  # Dados processados (JSON de saída)
```

---

## ⚙️ Funcionalidades

* **Extract (E):**

  * Leitura de arquivos JSON e CSV.
  * Conversão do CSV para formato padronizado JSON-like.

* **Transform (T):**

  * Fusão de dados entre diferentes laboratórios.
  * Ordenação alfabética dos pacientes via **Quick Sort**.
  * Busca sequencial e busca binária por paciente.
  * Estrutura de **Fila (FIFO)** para ordem cronológica dos exames.
  * Estrutura de **Pilha (LIFO)** para simulação de últimos exames primeiro.

* **Load (L):**

  * Salvamento do conjunto unificado em `data/processed/`.

---

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/jaoAprendiz/dynamic-programming2.git
   cd projeto-exames/src
   ```

2. Execute o script principal:

   ```bash
   python fusao_exames_v2.py
   ```

3. O resultado processado estará disponível em:

   ```
   data/processed/dados_laboratorios.json
   ```

---

## 📊 Exemplo de Saída (Quick Sort + Busca)

```bash
Antes de ordenar:
Carlos Lima
Beatriz Souza
João Silva
Ana Souza
Pedro Alves

Depois de ordenar:
Ana Souza
Beatriz Souza
Carlos Lima
João Silva
Pedro Alves

Exames encontrados para João Silva: 3
- Hemograma em 2024-05-20
- Colesterol em 2024-05-22
- Glicemia em 2024-05-25
```

---

## 🧮 Análise Algorítmica

### 🔹 Quick Sort

* **Descrição:** Ordena os pacientes por nome em ordem alfabética.
* **Complexidade:**

  * Melhor caso: **O(n log n)**
  * Caso médio: **O(n log n)**
  * Pior caso (lista já ordenada): **O(n²)**

---

### 🔹 Busca Sequencial

* **Descrição:** Percorre todos os exames até encontrar o paciente alvo.
* **Complexidade:**

  * Melhor caso: **O(1)** (primeiro elemento é o alvo)
  * Pior caso: **O(n)**

---

### 🔹 Busca Binária

* **Descrição:** Aplica divisão e conquista sobre a lista já ordenada.
* **Complexidade:**

  * Melhor caso: **O(1)**
  * Pior caso: **O(log n)**

> ⚠️ Pré-requisito: a lista deve estar ordenada (por `quick_sort`).

---

### 🔹 Estrutura de Fila (FIFO)

* **Enfileirar (append):** **O(1)**
* **Desenfileirar (pop(0)):** **O(n)** → pois desloca os elementos da lista.

---

### 🔹 Estrutura de Pilha (LIFO)

* **Empilhar (append):** **O(1)**
* **Desempilhar (pop()):** **O(1)**

---

## 🏗️ Possíveis Melhorias

* Utilizar `collections.deque` para otimizar a **fila** (`O(1)` em enfileirar e desenfileirar).
* Implementar ordenação estável (`merge sort`) para preservar ordem cronológica em caso de nomes iguais.
* Criar interface gráfica ou API para visualização dos dados processados.

---

## 👨‍💻 Autor

Projeto desenvolvido por **João Soave** como parte da disciplina de **Dynamic Programming** do curso de Engenharia de Software (FIAP).
