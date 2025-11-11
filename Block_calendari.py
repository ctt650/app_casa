import calendar
from datetime import datetime
from Block_bd import llegir_calendari, afegir_event_calendari

def veure_calendari():
    events = llegir_calendari()
    avui = datetime.today()
    any_actual = avui.year
    mes_actual = avui.month

    dates_reservades = set(event['data'] for event in events)

    print(f"\n--- CALENDARI DE {calendar.month_name[mes_actual]} {any_actual} ---\n")
    print("Dl  Dt  Dc  Dj  Dv  Ds  Dg")
    cal = calendar.monthcalendar(any_actual, mes_actual)

    for setmana in cal:
        for dia in setmana:
            if dia == 0:
                print("    ", end="")
            else:
                data_str = f"{any_actual}-{mes_actual:02d}-{dia:02d}"
                if data_str in dates_reservades:
                    print(f"🔴{dia:2d}", end=" ")
                else:
                    print(f"⚪{dia:2d}", end=" ")
        print()

def afegir_event():
    print("\n--- AFEGIR EVENT ---")
    data = input("Data (YYYY-MM-DD): ")
    descripcio = input("Descripció: ")
    afegir_event_calendari(data, descripcio)
    print("✅ Event afegit correctament!")