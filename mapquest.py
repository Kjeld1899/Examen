while True: 
    import json
    import requests
    import urllib.parse


#Variables
    url = "https://www.mapquestapi.com/directions/v2/route?"
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    apikey = "J4YAIu0xt21RjLtN0HF1v3p9lXKkiQpO"

    consulta = url + urllib.parse.urlencode({"key":apikey, "from":origen, "to":destino, "locale": "es_ES"})
    print(consulta)
    print("")
    
     
    data = requests.get(consulta).json()
    #narrativa de viaje
    print("InInstrucciones de ruta:")
    for step in data["route"]["legs"][0]["maneuvers"]:
     print(step["narrative"])
    
    #Distancia en km
    distancia = data["route"]["distance"] 
    operacion = int(distancia * 1.6) 
    print("La distancia fue: ", operacion , "Km")
    
    #tiempo de viaje
    tiempo = data["route"]["formattedTime"] 
    print("El tiempo total de viaje ha sido de: ", tiempo)

    #consumo de combustible
    opconsumo = int(operacion / 12)
    print("El consumo aproximado de combustible es: ", opconsumo , "lt.")

    

    
    salida = input("¿Desea salir de la aplicacion(s/n)?:  ")
    
    if salida == ("n"):
        break