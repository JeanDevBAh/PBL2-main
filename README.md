# 🕹️ Tetris em Python (com Terminal Interativo)

Este script em **Python** implementa uma versão customizada do clássico jogo **Tetris** diretamente no terminal. O projeto foi desenvolvido como atividade prática para o componente curricular **MI-Algoritmos**.

---

## 🚀 Funcionalidades

* **Tabuleiro Dinâmico:** Matriz de jogo configurada com dimensões de 20 linhas por 10 colunas, representada visualmente por emojis.
* **Peças Clássicas e Especiais:** Inclui as tradicionais peças do Tetris (I, O, T, Z, S, L, J) e uma **peça especial de bomba** (`💣`) que destrói blocos ao impactar.
* **Controles em Tempo Real:** Utiliza a biblioteca externa `keyboard` para capturar comandos de movimentação e rotação instantaneamente.
* **Sistema de Pontuação e Eliminação de Linhas:**
    * Verificação automática de linhas preenchidas com pontuação progressiva.
    * Mecânica de bônus para remoção de múltiplas linhas simultaneamente.
* **Sistema de Reinício:** Permite jogar novamente ao final de cada partida (`Game Over`) respondendo a um prompt interativo.

---

## 💻 Pré-requisitos e Dependências

Para executar este projeto, você precisará ter o **Python** instalado junto com a biblioteca externa `keyboard`.

1. Instale a biblioteca `keyboard` executando o seguinte comando no terminal:

   ```bash
   pip install keyboard
   ```

> ⚠️ **Atenção:** em sistemas Linux/macOS, a biblioteca `keyboard` pode exigir permissões de administrador (`sudo`) para capturar eventos do teclado, já que ela acessa o dispositivo de entrada diretamente.

---

## ▶️ Como Executar

Após instalar as dependências, clone o repositório (ou baixe os arquivos) e execute o script principal pelo terminal:

```bash
python tetris.py
```

> Substitua `tetris.py` pelo nome real do arquivo principal do seu projeto, caso seja diferente.

---

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| `←` | Move a peça para a esquerda |
| `→` | Move a peça para a direita |
| `↓` | Acelera a queda da peça |
| `↑` | Rotaciona a peça |
| `Espaço` | Queda instantânea (hard drop) |
| `Esc` / `Q` | Encerra o jogo |

> As teclas podem variar de acordo com a configuração feita no código-fonte.

---

## 🧩 Peças Disponíveis

* **I, O, T, Z, S, L, J** — peças clássicas do Tetris tradicional.
* **💣 Bomba** — peça especial que, ao colidir com o tabuleiro, destrói os blocos ao seu redor, abrindo espaço no tabuleiro.

---

## 🏆 Sistema de Pontuação

* Pontos são somados a cada linha completa eliminada.
* Eliminar **múltiplas linhas simultaneamente** concede um bônus extra de pontuação.
* A pontuação é exibida em tempo real durante a partida.

---

## 🔁 Game Over e Reinício

Quando as peças atingem o topo do tabuleiro, o jogo é encerrado e é exibida a mensagem de **Game Over** com a pontuação final. Em seguida, o jogador pode escolher reiniciar a partida através de um prompt interativo no terminal.

---

## 📁 Estrutura do Projeto

```
├── tetris.py        # Script principal do jogo
├── README.md        # Este arquivo
└── requirements.txt # Dependências do projeto (opcional)
```

---

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como atividade prática do componente curricular **MI-Algoritmos**, com o objetivo de aplicar conceitos de lógica de programação, estruturas de dados (matrizes), manipulação de entrada em tempo real e controle de fluxo em Python.

---

## 📜 Licença

Este projeto é de uso educacional e livre para estudo, modificação e distribuição, salvo indicação em contrário.
