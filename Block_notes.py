import os

def _fitxer_notes(nom_usuari):
    return f"notes_{nom_usuari}.txt"  # Fitxer personal per usuari

def afegir_nota(nom_usuari):
    print("\n--- AFEGIR NOTA ---")
    nota = input("Escriu la teva nota: ")
    fitxer = _fitxer_notes(nom_usuari)
    with open(fitxer, 'a') as f:
        f.write(nota + '\n')
    print("✅ Nota guardada!")

def veure_notes(nom_usuari):
    print("\n--- LES TEVES NOTES ---")
    fitxer = _fitxer_notes(nom_usuari)
    if not os.path.exists(fitxer):
        print("No tens cap nota encara.")
        return
    with open(fitxer, 'r') as f:
        notes = f.readlines()
    if not notes:
        print("No tens cap nota.")
    else:
        for i, nota in enumerate(notes, start=1):
            print(f"{i}. {nota.strip()}")

def esborrar_notes(nom_usuari):
    print("\n--- ESBORRAR TOTES LES NOTES ---")
    fitxer = _fitxer_notes(nom_usuari)
    if os.path.exists(fitxer):
        os.remove(fitxer)
        print("🗑️ Notes esborrades.")
    else:
        print("No tens cap nota per esborrar.")
