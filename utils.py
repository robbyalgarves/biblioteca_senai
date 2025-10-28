from datetime import datetime

def saudacao():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia! Seja bem-vindo(a) à Biblioteca SENAI 'Morvan Figueiredo'."
    elif 12 <= hora < 18:
        return "Boa tarde! Seja bem-vindo(a) à Biblioteca SENAI 'Morvan Figueiredo'."
    else:
        return "Boa noite! Seja bem-vindo(a) à Biblioteca SENAI 'Morvan Figueiredo'."