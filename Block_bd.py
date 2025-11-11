import os

# Constants de fitxers
FITXER_CALENDARI = "calendari.txt"
FITXER_USUARIS = "usuaris.txt"

# Variable global
usuari_actual = None

# FUNCIONS DE PERFIL

def fitxer_perfil_personalitzat():
    usuari = get_usuari_actual()
    if not usuari:
        return None
    return f"perfil_{usuari}.txt"

def llegir_perfil():
    fitxer = fitxer_perfil_personalitzat()
    if not fitxer or not os.path.exists(fitxer):
        return None
    with open(fitxer, 'r') as f:
        linies = f.readlines()
        if len(linies) >= 3:
            return {
                'nom': linies[0].strip(),
                'cognom': linies[1].strip(),
                'contrasenya': linies[2].strip()
            }
    return None

def guardar_perfil(nom, cognom, contrasenya):
    fitxer = fitxer_perfil_personalitzat()
    if not fitxer:
        print("❌ Error: No hi ha cap usuari actiu.")
        return
    with open(fitxer, 'w') as f:
        f.write(f"{nom}\n{cognom}\n{contrasenya}\n")

# FUNCIONS DE CALENDARI

def llegir_calendari():
    events = []
    if os.path.exists(FITXER_CALENDARI):
        with open(FITXER_CALENDARI, 'r') as f:
            for linia in f:
                parts = linia.strip().split('|')
                if len(parts) == 2:
                    events.append({'data': parts[0], 'descripcio': parts[1]})
    return events

def afegir_event_calendari(data, descripcio):
    with open(FITXER_CALENDARI, 'a') as f:
        f.write(f"\n{data}|{descripcio}")

# FUNCIONS D'USUARIS

def llegir_usuaris():
    usuaris = {}
    if os.path.exists(FITXER_USUARIS):
        with open(FITXER_USUARIS, 'r') as f:
            for linia in f:
                parts = linia.strip().split('|')
                if len(parts) >= 3:
                    nom, cognom, contrasenya = parts
                    usuaris[(nom, cognom)] = contrasenya
    return usuaris

def registrar_usuari(nom_usuari, cognom, contrasenya):
    with open(FITXER_USUARIS, 'a') as f:
        f.write(f"{nom_usuari}|{cognom}|{contrasenya}\n")

def verificar_usuari(nom_usuari, cognom, contrasenya):
    usuaris = llegir_usuaris()
    return (nom_usuari, cognom) in usuaris and usuaris[(nom_usuari, cognom)] == contrasenya

# FUNCIONS D’ESTAT DE SESSIÓ

def set_usuari_actual(nom):
    global usuari_actual
    usuari_actual = nom

def get_usuari_actual():
    return usuari_actual