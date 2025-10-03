# 📊 Projeto Dynamic Programming - Gestão de Exames e Insumos

Este projeto faz parte de um trabalho acadêmico e tem como objetivo aplicar **estruturas de dados** e **algoritmos clássicos** para manipulação de exames laboratoriais, além de introduzir **Programação Dinâmica** como ferramenta para otimização do consumo de insumos em laboratórios de diagnóstico.

---

## 🚀 Estrutura do Projeto

```
dynamic-programming2/
│
├── data/
│   ├── raw/               # Dados brutos (CSV e JSON)
│   └── processed/         # Saída processada em JSON
│
├── src/
│   ├── fusao_exames_v2.py          # Script principal (ETL + testes dos algoritmos)
│   ├── processamento_dados_v2.py   # Classes de manipulação de exames e algoritmos
│
└── README.md
```

---

## 🏗️ Funcionalidades Implementadas

### **1. Leitura e Fusão de Dados**
- Leitura de arquivos **JSON** e **CSV**
- Conversão automática de CSV → JSON padronizado
- Fusão de dados entre diferentes laboratórios

### **2. Estruturas de Dados**
- **Fila (FIFO):** exames em ordem cronológica
- **Pilha (LIFO):** exames em ordem inversa

### **3. Algoritmos**
- **Ordenação (QuickSort):** por nome de paciente  
- **Busca Sequencial:** percorre todos os exames  
- **Busca Binária:** eficiente após ordenação  

### **4. Programação Dinâmica (Sprint 4)**
Modelagem de problema de otimização do **uso de insumos laboratoriais**:
- Cada exame consome determinada quantidade de insumos.
- O estoque de insumos por dia é limitado.
- O objetivo é **maximizar o número de exames realizados sem ultrapassar o estoque**.

**Implementações:**
1. **Versão Recursiva** (top-down ingênua)  
2. **Versão com Memorização** (top-down otimizada)  
3. **Versão Iterativa** (bottom-up, tabulação)  

Todas as versões retornam o **mesmo resultado ótimo**, provando a consistência do modelo.

---

## 🔎 Formulação do Problema em Programação Dinâmica

- **Estado:**  
  `f(i, capacidade)` → melhor solução considerando os primeiros `i` exames com `capacidade` insumos restantes.  

- **Decisão:**  
  - Não realizar o exame `i`  
  - Realizar o exame `i` (se houver insumos suficientes)  

- **Função de transição:**  
  ```
  f(i, capacidade) = max(
      f(i-1, capacidade),                          # não incluir exame i
      valor[i] + f(i-1, capacidade - peso[i])      # incluir exame i
  )
  ```

- **Função objetivo:**  
  Maximizar o total de exames realizados respeitando a capacidade de insumos.

---

## 📈 Análise Algorítmica

### QuickSort
- Melhor caso: `O(n log n)`  
- Pior caso: `O(n²)`  
- Caso médio: `O(n log n)`  

### Busca Sequencial
- Tempo: `O(n)`  
- Espaço: `O(1)`  

### Busca Binária
- Tempo: `O(log n)`  
- Espaço: `O(1)` (iterativa)  

### Fila e Pilha
- Enfileirar / Empilhar: `O(1)`  
- Desenfileirar: `O(n)` (lista Python, pois `pop(0)` desloca elementos)  
- Desempilhar: `O(1)`  

### Programação Dinâmica (Knapsack)
- **Recursiva pura:** `O(2^n)` (ineficiente)  
- **Com memorização:** `O(n * capacidade)`  
- **Iterativa (Bottom-up):** `O(n * capacidade)`  

---

## ⚙️ Como Executar

1. Clone o repositório:  
   ```bash
   git clone <repo_url>
   cd dynamic-programming2
   ```

2. Estrutura esperada dos dados:
   - `data/raw/dados_laboratorioA.json`
   - `data/raw/dados_laboratorioB.csv`

3. Execute o script principal:  
   ```bash
   python src/fusao_exames_v2.py
   ```

---

## 📑 Exemplo de Saída

```
Total de exames após fusão: 220

Antes de ordenar:
Carlos Mendes
João Silva
Maria Oliveira
...

Depois de ordenar:
Ana Souza
Carlos Mendes
João Silva
...

Exames encontrados para João Silva: 3
- Hemograma em 2024-01-15
- Colesterol em 2024-02-03
...

[Programação Dinâmica] Resultado ótimo:
- Recursiva: 5
- Memorizada: 5
- Iterativa: 5
```

---

## 👨‍💻 Autor
Projeto desenvolvido por **João Soave** como parte da disciplina de **Dynamic Programming** do curso de Engenharia de Software (FIAP).
