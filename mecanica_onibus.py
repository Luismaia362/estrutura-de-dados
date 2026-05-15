from tkinter import *
from tkinter import ttk, messagebox

fila = []
contador_chegada = 0

def cadastrar():
    global contador_chegada

    nome = entry_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite o nome do ônibus!")
        return

    onibus = {
        "nome": nome,
        "prioridade": combo_prioridade.get(),
        "facilidade": combo_facilidade.get(),
        "chegada": contador_chegada
    }

    contador_chegada += 1

    fila.append(onibus)

    atualizar_tabela()

    entry_nome.delete(0, END)

def ordenar():
    prioridade_valor = {
        "Alta": 1,
        "Média": 2,
        "Baixa": 3
    }

    facilidade_valor = {
        "Fácil": 1,
        "Médio": 2,
        "Difícil": 3
    }

    fila.sort(
        key=lambda x: (
            prioridade_valor[x["prioridade"]],
            facilidade_valor[x["facilidade"]],
            x["chegada"]
        )
    )

    atualizar_tabela()

def atender():
    if len(fila) == 0:
        messagebox.showinfo("Fila", "Nenhum ônibus na fila!")
        return

    ordenar()

    primeiro = fila.pop(0)

    messagebox.showinfo(
        "Atendimento",
        f"Atendendo: {primeiro['nome']}"
    )

    atualizar_tabela()

def atualizar_tabela():
    tabela.delete(*tabela.get_children())

    for i, onibus in enumerate(fila):
        tabela.insert(
            "",
            END,
            values=(
                i + 1,
                onibus["nome"],
                onibus["prioridade"],
                onibus["facilidade"],
                onibus["chegada"]
            )
        )

janela = Tk()
janela.title("Mecânica de Ônibus")
janela.geometry("900x500")
janela.configure(bg="#1e1e1e")

titulo = Label(
    janela,
    text="SISTEMA DA MECÂNICA DE ÔNIBUS",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=10)

frame_cadastro = Frame(janela, bg="#2b2b2b", padx=10, pady=10)
frame_cadastro.pack(pady=10)

Label(
    frame_cadastro,
    text="Nome do Ônibus",
    bg="#2b2b2b",
    fg="white"
).grid(row=0, column=0, padx=5, pady=5)

entry_nome = Entry(frame_cadastro, width=25)
entry_nome.grid(row=0, column=1, padx=5)

Label(
    frame_cadastro,
    text="Prioridade",
    bg="#2b2b2b",
    fg="white"
).grid(row=0, column=2, padx=5)

combo_prioridade = ttk.Combobox(
    frame_cadastro,
    values=["Alta", "Média", "Baixa"],
    state="readonly"
)

combo_prioridade.current(0)
combo_prioridade.grid(row=0, column=3, padx=5)

Label(
    frame_cadastro,
    text="Facilidade",
    bg="#2b2b2b",
    fg="white"
).grid(row=0, column=4, padx=5)

combo_facilidade = ttk.Combobox(
    frame_cadastro,
    values=["Fácil", "Médio", "Difícil"],
    state="readonly"
)

combo_facilidade.current(0)
combo_facilidade.grid(row=0, column=5, padx=5)

btn_cadastrar = Button(
    frame_cadastro,
    text="Cadastrar",
    bg="green",
    fg="white",
    width=15,
    command=cadastrar
)

btn_cadastrar.grid(row=0, column=6, padx=10)

frame_botoes = Frame(janela, bg="#1e1e1e")
frame_botoes.pack(pady=10)

btn_ordenar = Button(
    frame_botoes,
    text="Ordenar Fila",
    bg="blue",
    fg="white",
    width=20,
    command=ordenar
)

btn_ordenar.grid(row=0, column=0, padx=10)

btn_atender = Button(
    frame_botoes,
    text="Atender Próximo",
    bg="red",
    fg="white",
    width=20,
    command=atender
)

btn_atender.grid(row=0, column=1, padx=10)

frame_tabela = Frame(janela)
frame_tabela.pack(pady=10)

colunas = ("Posição", "Ônibus", "Prioridade", "Facilidade", "Chegada")

tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show="headings",
    height=12
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack()

janela.mainloop()
