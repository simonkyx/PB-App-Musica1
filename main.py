from contenido import Contenido
from cancion import Cancion
from podcast import Podcast
from artista import Artista
from playlist import Playlist
from usuario import Usuario
def main():
    
    # CREAR CANCION
    cancion_uno = Cancion("Beat it",4.50, "Pop")
    cancion_dos = Cancion("Bad", 3.25, "Pop")

    # CREAR Podcast
    podcast_uno = Podcast("Ultima luna", 35, "Comedia", 15)

    #CREAR ARTISTA

    nuevo_artista = Artista("Michael Jackson", "Pop")

    #Asociar las canciones al artista
    nuevo_artista.agregar_cancion(cancion_uno)
    nuevo_artista.agregar_cancion(cancion_dos)

    nuevo_artista.mostrar_informacion()

    #CREAR PLAYLIST

    nueva_playlist = Playlist("Fvoritos", "Canciones que me gustan")
    nueva_playlist.mostrar_playlist()

    nueva_playlist.agregar_cancion(cancion_uno)
    
    nueva_playlist.agregar_cancion(cancion_dos)


    # CREAR USUARIO

    nuevo_usuario = Usuario("Simon", "calfucura14sim@gmail.com", True)
    nuevo_usuario.crear_playlist(nueva_playlist)
    
    nuevo_usuario.mostrar_informacion()
    


if __name__=="__main__":
    main()