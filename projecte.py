# Importacions explícites
from Block_perfil import mostrar_perfil, editar_perfil
from Block_inicisessio import inici_sessio
from Block_calendari import veure_calendari, afegir_event
from Block_notes import veure_notes, afegir_nota, esborrar_notes
from Block_bd import get_usuari_actual

def main():
    if not inici_sessio():  # Si no inicia sessió, es tanca l'aplicació
        print("Fins aviat!")
        exit()

    while True:
        usuari_actiu = get_usuari_actual()  # Obté l'usuari actiu global
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Veure perfil")
        print("2. Editar perfil")
        print("3. Veure calendari")
        print("4. Afegir event al calendari")
        print("6. Veure notes")
        print("7. Afegir nota")
        print("8. Esborrar totes les notes")
        print("5. Tancar sessió")
        print("9. Sortir de l'aplicació")
        
        opcio = input("Selecciona una opció: ")
        
        if opcio == "1":
            mostrar_perfil()
        elif opcio == "2":
            editar_perfil()
        elif opcio == "3":
            veure_calendari()
        elif opcio == "4":
            afegir_event()
        elif opcio == "5":
            veure_notes(usuari_actiu)
        elif opcio == "6":
            afegir_nota(usuari_actiu)
        elif opcio == "7":
            esborrar_notes(usuari_actiu)
        elif opcio == "8":
            print("Sessió tancada.")
            if not inici_sessio():  # Torna a iniciar sessió o surt
                break
        elif opcio == "9":
            print("Fins aviat!")
            break
        else:
            print("Opció no vàlida, intenta-ho de nou")

if __name__ == "__main__":
    main()
#Modificació
