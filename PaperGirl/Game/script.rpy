# The script of the game goes in this file.

# screen main_menu():
#     tag menu

#     image menu:
#         "main_menu.png"
#         zoom 0.5

#     # Add your custom background
#     add menu  # or your image filename

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default painting_name = "Ayaka"

define kuno = Character("Kuno")
define hideo = Character("Hideo (boss)")
define painting = DynamicCharacter("painting_name")

#Define images
image Kuno sad:
    "kuno sad.png"
    zoom 0.45

image Kuno smiling:
    "kuno smiling.png"
    zoom 0.45

image Kuno surprised:
    "kuno surprised.png"
    zoom 0.45

image Kuno painter:
    "kuno painting.png"
    zoom 0.45

image Hideo:
    "Hideo (enojado).png"
    zoom 0.5

image Ayaka Portrait:
    "Ayaka portrait.png"
    zoom 0.85

image Ayaka Smiling:
    "Ayaka smiling.png"
    zoom 0.85

image Empty Canvas:
    "Empty canvas.png"
    zoom 0.85


image Studio day:
    "studio apartment.png"

image Studio night:
    "studio apartment night.png"


image Office:
    "office.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Studio day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Kuno sad

    # These display lines of dialogue.

    kuno "Otra vez es lunes. Otra semana de trabajo empieza. Que me pondran hacer hoy?"

    kuno "Bueno ni modo. A empezar el dia."

    scene Office

    show Kuno smiling at right
    show Hideo at left

    hideo "Hoy necesito que te quedes hasta tarde."
    hideo "Este proyecto debe salir hoy. Tu sos el unico capaz de hacerlo."

    kuno "Si. Comprendo."

    scene Studio night

    show Kuno sad

    kuno "Que dia tan largo. Quisiera tener alguien con quien hablar."

    show Kuno smiling
    kuno "Bueno que se va hacer. Ya la noche es mia. Es hora de poner manos a la obra."

    show Kuno painter
    kuno "Que pintare hoy? Un bello paisaje con aves? Un amanecer en la playa? Un bosque?"

    menu:
        "Un paisaje con aves":
        # Statements to run if Choice 1 is selected
            kuno "Como me gustaria volar como las aves."
            jump final_decision
        "Un amanecer en la playa":
        # Statements to run if Choice 2 is selected
            kuno "El sonido de olas me relajan."
            jump final_decision
        "Un bosque":
        # Statements to run if Choice 3 is selected
            kuno "Los arboles y la vida silvestre es tan bello."
            jump final_decision

label final_decision:
    show Kuno painter at right
    show Empty Canvas at left

    kuno "Pero esa escena solo me recuerda lo solo que estoy."
    kuno "Ya se! Pintare una compañera."
    kuno "Ella sera perfecta. Ojos gentiles"
    kuno "Pelo negro como la obsidiana."

    scene Studio day
    with fade

    show Kuno painter at right
    show Ayaka Portrait at left

    kuno "Listo! Es perfecta!"
    kuno "Ahora un nombre?"
    kuno "Que nombre te pongo?"

    menu:
        "Ayaka":
            kuno "Ayaka es el nombre perfecto! Sos una bella flor colorida."
            $ painting_name = "Ayaka"
            jump name_decision

        "Tsukiko":
            kuno "Tu piel es radiante como la luna. Tsukiko es el nombre ideal para ti."
            $ painting_name = "Tsukiko"
            jump name_decision

        "Natsumi":
            kuno "Solo verte calienta mi corazon. Definitivamente sos un bello verano, Natsumi!"
            $ painting_name ="Natsumi"
            jump name_decision

label name_decision:
    kuno "Ya amanecio. Me tengo que arreglar para ir a trabajar [painting_name]"

    show Kuno smiling at right
    show Ayaka Portrait at left

    kuno "Ya me voy [painting_name] pero regresare lo más pronto posible!"

    scene Office
    with fade

    show Kuno sad at right
    show Hideo at left

    hideo "Kuno llegaste 30 minutos tarde."
    hideo "Terminaste el proyecto de ayer?"

    kuno "Perdon. Me quede hasta tarde ayer pero no pude terminar porque habian partes que faltaban del proyecto."

    hideo "Comprendo pero nos urge sacar esto lo antes posible. Por favor para hoy a mas tardar necesito que lo termines."

    scene Studio night

    show Kuno sad

    kuno "Otro dia largo."

    show Kuno smiling at right
    show Ayaka Portrait at left
    kuno "Lo bueno es que termine y tu rostro radiante me llena de esperanza, [painting_name]."
    kuno "[painting_name], me haces tan feliz. Creo que..."
    kuno "..."
    kuno "Te amo"

    "Kuno toca el rostro de [painting_name] con gentileza"
    "Siente una leve brisa"
    "Empieza a buscar el origen del aire"

    show Ayaka Smiling at left

    "De repente oye un sollozo proveniente de [painting_name]"

    show Kuno surprised at right
    kuno "[painting_name], estas viva!"

    "Kuno se repone al ver que sigue sollozando"

    show Kuno smiling at right
    kuno "Porque lloras [painting_name]?"
    painting "Nunca me imagine oir esas palabras"

    "Te gustaria saber que pasa despues?"

    menu:
        "Si":
            "Qué crees que pasara después? Hasta la proxima."
        "Tal vez":
            "Qué te gustaría que pasara después?"
        "No":
            "Lastima. Hasta la proxima"
        

    # This ends the game.

    return
