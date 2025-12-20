import os
import tkinter as tk
from tkinter import messagebox

# cores da to do list
COR_FUNDO = "#EAEAEA"      # Cinza claro/Bege
COR_CABECALHO = "#A38A83"  # Marrom suave
COR_TEXTO = "#333333"      # Cinza escuro
COR_BRANCO = "#FFFFFF"

tarefas_armazenadas = []

def salvar_tarefas():
    with open("tarefas.txt", "w", encoding="utf-8") as f:
        for tarefa in tarefas_armazenadas:
            f.write(tarefa + "\n")

def carregar_tarefas():
    if os.path.exists("tarefas.txt"):
        with open("tarefas.txt", "r", encoding="utf-8") as f:
            for linha in f:
                tarefa = linha.strip()
                if tarefa: 
                    tarefas_armazenadas.append(tarefa)
        atualizar_lista_visual()

def atualizar_lista_visual():
    lista_visual.delete(0, tk.END)
    for indice, tarefa in enumerate(tarefas_armazenadas, start=1):
        lista_visual.insert(tk.END, f"  {indice}. {tarefa}")

def adicionar_tarefa():
    tarefa = entry_tarefa.get().strip()
    if tarefa != "":
        tarefas_armazenadas.append(tarefa)
        atualizar_lista_visual()
        entry_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Digite uma tarefa!")
        salvar_tarefas()

def remover_tarefa():
    try:
        indice_selecionado = lista_visual.curselection()[0]
        tarefas_armazenadas.pop(indice_selecionado)
        atualizar_lista_visual()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")
        salvar_tarefas()

def marcar_concluida():
    try:
        indice = lista_visual.curselection()[0]
        
        # EFEITO DE PISCAR: muda a cor de fundo da lista para um verde suave
        lista_visual.config(bg="#C8E6C9") 
        # apos 200 milissegundos o Python executa a função de "confirmar"
        janela.after(200, finalizar_conclusao, indice)
        
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa!")
        salvar_tarefas()

def finalizar_conclusao(indice):
    tarefa = tarefas_armazenadas[indice]
    if "✅" not in tarefa:
        tarefas_armazenadas[indice] = f"✅ {tarefa}"
    
    lista_visual.config(bg="#FFFFFF") 
    atualizar_lista_visual()
    salvar_tarefas() 

# interface
janela = tk.Tk()
janela.title("Checklist Moderno")
janela.geometry("400x600")
janela.configure(bg=COR_FUNDO)

# titulo principal
label_titulo = tk.Label(janela, text="CHECKLIST", font=("Playfair Display", 28, "bold"), 
                        bg=COR_FUNDO, fg=COR_TEXTO)
label_titulo.pack(pady=(30, 10))

frame_topo = tk.Frame(janela, bg=COR_CABECALHO, height=40)
frame_topo.pack(fill="x", padx=40)
label_tarefas = tk.Label(frame_topo, text="Tarefas", bg=COR_CABECALHO, fg=COR_BRANCO, 
                         font=("Arial", 12, "bold"))
label_tarefas.pack(side="left", padx=10, pady=5)

# lista visual 
lista_visual = tk.Listbox(janela, font=("Arial", 12), bg=COR_BRANCO, fg=COR_TEXTO,
                          selectbackground=COR_CABECALHO, relief="flat", 
                          highlightthickness=0, bd=0)
lista_visual.pack(fill="both", padx=40, pady=(0, 10), expand=True)

entry_tarefa = tk.Entry(janela, font=("Arial", 12), bg=COR_BRANCO, relief="flat", 
                        highlightthickness=1, highlightbackground="#CCCCCC")
entry_tarefa.pack(fill="x", padx=40, pady=10, ipady=5)

# vincula a tecla Enter (chamada de <Return>) a função de adicionar
entry_tarefa.bind("<Return>", lambda event: adicionar_tarefa())

frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack(pady=20)

btn_estilo = {"relief": "flat", "font": ("Arial", 10, "bold"), "fg": COR_BRANCO, "cursor": "hand2"}

tk.Button(frame_botoes, text="ADICIONAR", command=adicionar_tarefa, bg=COR_CABECALHO, **btn_estilo).pack(side="left", padx=5)
tk.Button(frame_botoes, text="✓ CONCLUIR", command=marcar_concluida, bg="#829582", **btn_estilo).pack(side="left", padx=5)
tk.Button(frame_botoes, text="✕ EXCLUIR", command=remover_tarefa, bg="#B27A7A", **btn_estilo).pack(side="left", padx=5)

carregar_tarefas()
janela.mainloop()
