import random
#ESERCIZIO COMPLETO
# Scrivere un programma che chieda all'utente di inserire i dati dei dipendenti di un supermercato.
# Ciascun dipendente è caratterizzato da un nome, un cognome, una data di nascita e un mestiere.
# di nascita e  un mestiere.ASSEGNARE A CIASCUN DIPENDENTE UN IDENTIFICATIVO UNIVOCO
#   - prendere le prime due lettere del nome, le ultime due lettere del cognome e 3 numeri casuali
# compresi tra 1 e 9. Es. Mario Rossi -> id univoco MASI356
# Chiedere all'utente di inserire i dati relativi ad un determinato dipendente e memorizzarli
# all'interno di un dizionario.
# (A)ggiungi: aggiunta di un dipendente
# (S)tampa
# (R)icerca dei dipendenti con un certo nome (consideriamo anche le omonimie)
print("*** Benvenuto ***")
print("*** Operazioni eseguibili ***")
print("     A per aggiungere un cliente")
print("     M per modificare un cliente")
print("     R per rimuovere un cliente")
print("     S per stampare l'intero database")
print("     Q per abbandonare il sistema")
lista_dipendenti = []
while True:
    scelta = input("Quale operazioni vuoi eseguire? (A)ggiungi/(S)tampa/(R)icerca/(Q)uit: ").upper()
    if scelta == 'A':     #qua sotto: richiesta dati utente, generazione identificativo,creare dipendente, aggiungere ad un database 
        #Richiesta dati utente
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        data_nascita = input("Inserisci la data di nascita: ") #"01/01/1970"
        mestiere = input("Inserisci il mestiere: ")
        #Generazione identificativo
        id = nome[:2] + cognome[len(cognome)-2:] + str(random.randint(100, 999))
        #creare il dipendente(dizionario)
        dipendente = {"Identificativo": id, "nome": nome, "cognome": cognome, "data": data_nascita, "mestiere": mestiere}
        #Aggiungere ad un database
        lista_dipendenti.append(dipendente)
    elif scelta == 'S':
        pass
    elif scelta == 'R':
        pass
    elif scelta == "Q":
        break

    else:
        print("SCELTA NON VALIDA")

