

class Usuario:
    def __init__(self,nombre, correo , premium):

        self.nombre = nombre
        self.correo = correo
        self.premium = premium


        self.playlists = []

    
    # crear una playlist

    def crear_playlist(self, playlist):

        self.playlists.append(playlist)
        
        print(f"La playlist {playlist.nombre}"
              f" fue creada por {self.nombre}")
        
    
    def mostrar_informacion(self):
        print("\n ---USUARIo---")
        print(f"Nombre : {self.nombre}")
        print(f"correo : {self.correo}")

        if self.premium:
            print("Tipo de cuenta : Premium")
        else:
            print("Tipo de cuenta : gratuita")
