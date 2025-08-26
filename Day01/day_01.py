info_superheroes = {
    "Iron Man": {
        "nombre_real": "Tony Stark",
        "poderes": ["Tecnología avanzada", "Movilidad aérea"],
        "equipo": "Los vengadores",
    },
    "Capitán América": {
        "nombre_real": "Steve Rogers",
        "poderes": ["Fuerza sobrehumana", "Agilidad y reflejos sobresalientes"],
        "equipo": "Los vengadores",
    },
    "Thor": {
        "nombre_real": "Thor Odinson",
        "poderes": ["Mjolnir", "Viento y trueno"],
        "equipo": "Los vengadores",
    },
    "Spiderman": {
        "nombre_real": "Peter Parker",
        "poderes": ["Balanceo", "Telarañas pegajosas", "Sentido aracnido"],
        "equipo": "Los vengadores",
    },
    "Hulk": {
        "nombre_real": "Bruce Banner",
        "poderes": ["Fuerza sobrehumana", "Invulnerabilidad"],
        "equipo": "Los vengadores",
    },
}

def mostrar_informacion_superheroe(superheroe):
    datos = info_superheroes.get(superheroe)
    if datos:
        print(f"\nInfo {superheroe}")
        print(f"\tNombre real: {datos['nombre_real']}")
        print(f"\tPoderes: {', '.join(datos['poderes'])}")
        print(f"\tEquipo: {datos['equipo']}")
    else:
        print(f"{superheroe} no está en la base de datos.")

def mostrar_informacion_superheroes(lista_superheroes):
    for sh in lista_superheroes:
        mostrar_informacion_superheroe(sh)

mostrar_informacion_superheroe('Iron Man')
mostrar_informacion_superheroes(['Iron Man', 'Spiderman', 'Thor'])
