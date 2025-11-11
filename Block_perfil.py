from Block_bd import llegir_perfil, guardar_perfil, get_usuari_actual

def mostrar_perfil():
    """Mostra les dades del perfil actual"""
    perfil = llegir_perfil()  # Obté dades des del fitxer de perfil
    nom_usuari = get_usuari_actual()  # Obté el nom de l'usuari actiu
    
    print("\n--- EL TEU PERFIL ---")
    print(f"Usuari actiu: {nom_usuari}")
    
    if perfil:
        print(f"Nom: {perfil['nom']}")
        print(f"Cognom: {perfil['cognom']}")
        print(f"Contrasenya: {perfil['contrasenya']}")
    else:
        print("Encara no tens perfil creat.")

def editar_perfil():
    """Permet editar el perfil"""
    print("\n--- EDITAR PERFIL ---")
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    contrasenya = input("Contrasenya: ")
    guardar_perfil(nom, cognom, contrasenya)  # Desa al fitxer personalitzat
    print("✅ Perfil actualitzat correctament!")