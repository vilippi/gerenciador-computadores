import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

dados_path = "dados.json"

def carregar_dados():
    if os.path.exists(dados_path):
        try:
            with open(dados_path, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_dados(lista):
    with open(dados_path, "w") as f:
        json.dump(lista, f, indent=4)

def adicionar():
    nome = entry_nome.get()
    numero_pc = entry_numero_pc.get()
    processador = entry_processador.get()
    placa_video = entry_placa_video.get()
    ram = entry_ram.get()
    armazenamento = entry_armazenamento.get()
    dono_antigo = entry_dono_antigo.get()

    if nome and numero_pc and processador and placa_video and ram and armazenamento and dono_antigo:
        lista.append({
            "nome": nome,
            "numero_pc": numero_pc,
            "processador": processador,
            "placa_video": placa_video,
            "ram": ram,
            "armazenamento": armazenamento,
            "dono_antigo": dono_antigo
        })
        salvar_dados(lista)
        atualizar_lista()
        limpar_campos()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def atualizar_lista():
    for row in tree.get_children():
        tree.delete(row)
    for item in lista:
        tree.insert("", tk.END, values=(
            item['nome'],
            item['numero_pc'],
            item['processador'],
            item['placa_video'],
            item['ram'],
            item['armazenamento'],
            item['dono_antigo']
        ))

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_numero_pc.delete(0, tk.END)
    entry_processador.delete(0, tk.END)
    entry_placa_video.delete(0, tk.END)
    entry_ram.delete(0, tk.END)
    entry_armazenamento.delete(0, tk.END)
    entry_dono_antigo.delete(0, tk.END)

# Interface principal
app = tk.Tk()
app.title("Gerenciador de Computadores")
app.geometry("800x600")

style = ttk.Style()
style.theme_use("clam")  # tema mais limpo e moderno

frame_form = ttk.Frame(app, padding=10)
frame_form.pack(fill=tk.X)

def criar_label_e_entry(parent, texto):
    label = ttk.Label(parent, text=texto)
    label.pack(fill=tk.X, padx=5, pady=2)
    entry = ttk.Entry(parent)
    entry.pack(fill=tk.X, padx=5, pady=2)
    return entry

entry_nome = criar_label_e_entry(frame_form, "Nome")
entry_numero_pc = criar_label_e_entry(frame_form, "Número")
entry_processador = criar_label_e_entry(frame_form, "Processador")
entry_placa_video = criar_label_e_entry(frame_form, "Placa de Vídeo")
entry_ram = criar_label_e_entry(frame_form, "RAM")
entry_armazenamento = criar_label_e_entry(frame_form, "Armazenamento")
entry_dono_antigo = criar_label_e_entry(frame_form, "Antigo Dono")

ttk.Button(app, text="Adicionar Computador", command=adicionar).pack(pady=10)

# Treeview
colunas = ("Nome", "Número", "Processador", "Placa de Vídeo", "RAM", "Armazenamento", "Antigo Dono")
tree = ttk.Treeview(app, columns=colunas, show="headings", height=10)
for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.W, width=100)

tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

lista = carregar_dados()
atualizar_lista()

app.mainloop()