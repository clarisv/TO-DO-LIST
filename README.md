# 🗒️ Checklist Moderno & Inteligente

Um aplicativo de gerenciamento de tarefas desenvolvido em **Python** com uma interface minimalista e elegante inspirada em designs modernos. O projeto foca em organização pessoal com recursos de automação e persistência de dados.

## ✨ Novas Implementações Profissionais

- **Design Minimalista:** Interface limpa com paleta de cores neutras e botões no estilo "Flat" (sem bordas 3D).
- **Persistência de Dados:** Uso da biblioteca `os` para salvar e carregar tarefas automaticamente de um arquivo `.txt`. Suas metas não somem ao fechar o app!
- **Numeração Inteligente:** Sistema que reorganiza automaticamente os números dos itens (1, 2, 3...) mesmo após a exclusão de tarefas intermediárias.
- **Micro-animações:** Feedback visual de "piscar" ao concluir tarefas, aumentando a interatividade.
- **Atalhos de Teclado:** Integração com a tecla `Enter` para adição rápida de itens.

## 🛠️ Tecnologias e Conceitos Utilizados

- **Python & Tkinter:** Construção da GUI.
- **Manipulação de Arquivos (I/O):** Leitura e escrita de dados com `utf-8`.
- **Event Binding:** Vinculação de eventos de teclado (`<Return>`).
- **Lógica de Coleções:** Uso de listas dinâmicas para gerenciar o estado das tarefas.

## 📸 Como ficou o visual
> [!IMPORTANT]
> **Dica:** Agora que o design está lindo, tire aquele print da tela e substitua o link abaixo!
> `![Checklist Moderno](screenshot-checklist.png)`

## 🚀 Como testar
1. Baixe o arquivo `LISTA-TAREFAS.py`.
2. Execute no seu terminal: `python LISTA-TAREFAS.py`.
3. O arquivo `tarefas.txt` será criado automaticamente na primeira vez que você adicionar uma meta.
