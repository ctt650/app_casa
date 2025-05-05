from Block_bd import registrar_usuari, verificar_usuari, set_usuari_actual

def inici_sessio():
    """Gestiona l'inici de sessió o registre"""
    print("\n--- INICI DE SESSIÓ ---")

    while True:
        print("1. Iniciar sessió")
        print("2. Registrar-se")
        print("3. Sortir")

        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            nom = input("Nom d'usuari: ")
            cognom = input("Cognom: ")
            contrasenya = input("Contrasenya: ")
            if verificar_usuari(nom, cognom, contrasenya):
                set_usuari_actual(nom)  # Guarda qui ha iniciat sessió
                print(f"✅ Benvingut/da, {nom} {cognom}!")
                return True
            else:
                print("❌ Credencials incorrectes")
        elif opcio == "2":
            nom = input("Nom d'usuari: ")
            cognom = input("Cognom: ")
            contrasenya = input("Contrasenya: ")
            registrar_usuari(nom, cognom, contrasenya)
            print("✅ Usuari registrat correctament!")
        elif opcio == "3":
            return False
        else:
            print("Opció no vàlida")
