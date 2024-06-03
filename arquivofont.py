import tkinter as tk
from tkinter import ttk

# Definição dos recursos de saúde mental por categoria
recursos = {
    "Meditação e Mindfulness": [
        {"nome": "Headspace", "descricao": "App de meditação guiada", "link": "https://www.headspace.com/"},
        {"nome": "Calm", "descricao": "App de meditação e relaxamento", "link": "https://www.calm.com/"},
        {"nome": "Insight Timer", "descricao": "App com meditações guiadas e sons relaxantes",
         "link": "https://insighttimer.com/"}
    ],
    "Apoio Emocional": [
        {"nome": "CVV - Centro de Valorização da Vida", "descricao": "Atendimento telefônico para apoio emocional",
         "link": "https://www.cvv.org.br/"},
        {"nome": "Terapia Cognitivo-Comportamental (TCC)",
         "descricao": "Abordagem terapêutica para tratamento de problemas emocionais",
         "link": "https://www.abctcc.com.br/"},
        {"nome": "Psicólogos Online", "descricao": "Plataforma para encontrar psicólogos e agendar sessões online",
         "link": "https://www.psiconlinews.com.br/"}
    ],
    "Terapia Online": [
        {"nome": "BetterHelp", "descricao": "Plataforma online de terapia com profissionais licenciados",
         "link": "https://www.betterhelp.com/"},
        {"nome": "Talkspace", "descricao": "Plataforma de terapia online com sessões de chat, vídeo ou áudio",
         "link": "https://www.talkspace.com/"},
        {"nome": "Online-Therapy.com", "descricao": "Serviço online de terapia com suporte de chat ao vivo",
         "link": "https://www.online-therapy.com/"}
    ]
}


# Função para exibir os recursos de uma categoria
def exibir_recursos(categoria):
    for widget in frame.winfo_children():
        widget.destroy()
    if categoria == "Escolha uma Categoria" or categoria == "Voltar ao Início":
        introducao = tk.Label(frame,
                              text="A saúde mental é fundamental para o bem-estar geral. Aqui estão alguns recursos que podem ajudar a melhorar e manter sua saúde mental. Por favor, selecione uma categoria para começar.",
                              font=("Helvetica", 12, "bold"), wraplength=500)
        introducao.pack(pady=20)
    else:
        introducao = None

        recursos_label = tk.Label(frame, text=f"Recursos para {categoria}", font=("Helvetica", 16, "bold"))
        recursos_label.pack(pady=10)

        for recurso in recursos[categoria]:
            nome = tk.Label(frame, text=f"Nome: {recurso['nome']}", font=("Helvetica", 12, "bold"))
            nome.pack(anchor="w")
            descricao = tk.Label(frame, text=f"Descrição: {recurso['descricao']}", font=("Helvetica", 12))
            descricao.pack(anchor="w")
            link = tk.Label(frame, text=f"Link: {recurso['link']}", font=("Helvetica", 12), fg="blue", cursor="hand2")
            link.pack(anchor="w")
            link.bind("<Button-1>", lambda e, url=recurso['link']: abrir_link(url))

    return introducao


# Função para abrir o link no navegador padrão
def abrir_link(url):
    import webbrowser
    webbrowser.open_new(url)


# Configuração da janela principal
root = tk.Tk()
root.title("Guia de Recursos de Saúde Mental")
root.geometry("600x400")
background_image = tk.PhotoImage(file="what-is-mental-health.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Frame para exibir os recursos
frame = tk.Frame(root)
frame.pack(pady=20)

# Texto introdutório inicial
introducao = exibir_recursos("Escolha uma Categoria")

# Menu dropdown para selecionar a categoria
categoria_selecionada = tk.StringVar()
categoria_selecionada.set("Escolha uma Categoria")

opcoes_menu = ["Escolha uma Categoria", "Voltar ao Início"] + list(recursos.keys())
menu = ttk.OptionMenu(root, categoria_selecionada, *opcoes_menu, command=exibir_recursos)
menu.pack(pady=20)

root.mainloop()
