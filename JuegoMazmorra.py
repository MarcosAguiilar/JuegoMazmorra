from operator import truediv

import random

print("Bienvenido al juego de la mazmorra\n"
      "----------------------------------\n"
      "Tu y tu compañero de celda os habéis escapado de la prisón espacial, habéis despistado a los guardias \n"
      "y os dirigís hacia el exterior. Al salir os econtrais con una mazmorra llena de montruos alienigenas \n"
      "que debeis atravesar. Por sorpresa un guardia pilla a tu compañero, tu tienes suerte ya que pasaste \n"
      "desapercibido. Es tu momento de escapar, tienes dos opciones, cual eliges?\n"
      "\n"
      "Puedes seguir el camino recto y oscuro, a la derecha tienes una puerta y a tu izquerda se abre otro \n"
      "camino con un claro al final."
      )

tiene_llave = False
opcion = input("RECTO[R] || DERECHA[D] || IZQUERDA[I]: ").upper()
hipotenusa = 3.125

if opcion == "R":
    print("Sigues caminando por el pasillo oscuro, te encuentras una espada y un escudo policial. \n"
          "Que decides lo cojes o lo dejas?"
          )
    opcion_espada_escudo = input("COJER[C] || DEJAR[D]: ").upper()
    if opcion_espada_escudo == "C":
        print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
              "Onanaquis, la espécie alienígena mas temida del universo. Tuviste suerte de cojer esa espada \n"
              "y ese escudo.\n"
              "Quieres combatir o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
              )
        opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
        if opcion_combate == "H":
            print("Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                  "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                  "que pierdes la conciencia y finalmente mueres.")
        else:
            print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                  "Tras una intesa batalla, consigues derrotarlo. Exploras la sale y no encuentras nada\n"
                  "por lo que decides volver sobre tus pasos. Llegas al inicio, te quedan dos opciones.\n"
                  "Intentar abrir la puerta o investigar el otro camino. Que decides?"
                  )
            opcion_inicio = input("PUERTA[P] || CAMINO[C]: ").upper()
            if opcion_inicio == "P":
                print("Intentas abrir la puerta pero esta bloqueada por una cerradura que necesita una llave y \n"
                      "un código. En la puerta están talladas las siguientes instrucciones: \n"
                      "\n"
                      "Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?\n"
                      "\n"
                      "Como no tienes la llave decides seguir el camino iluminado hasta que te encuentras con una \n"
                      "sala llena de comida, parece ser donde los guardias guardan todo lo que se requisa de la \n"
                      "prison. Quieres comer o prefieres seguir el camino?\n")
                opcion_comer = input("COMER[C] || SEGUIR[S]: ").upper()
                if opcion_comer == "C":
                    print(
                        "Comiste hasta que ni moverte pudiste, te entro sueño y dormido te quedaste. Un guardia te vio \n"
                        "durmiendo y te devolvió a la carcel. Ahora te esperan 6 meses de aislamiento y toda una vida \n"
                        "en prison.")
                else:
                    print("No te distraes y sigues avanzando, llegas hasta una sala en la cual se encuentra la llave \n"
                          "maestra que abre todas las puertas del universo. Vuelves hacia la puerta he introduces la \n"
                          "llave pero te falta el código...\n"
                          "Vuelves a leer el tallado en la puerta")
                    tiene_llave = True
                    solucion_hipotenusa = float(
                        input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
                    while solucion_hipotenusa != hipotenusa:
                        print("Contraseña incorrecta.")
                        solucion_hipotenusa = float(
                            input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))

                    print(
                        "Correcto! La puerta se ha abierto, destrás de ella se encuentra la zona de despegue. Coges una nave y \n"
                        "te escapas a la velocidad de la luz.")

            if opcion_inicio == "C":
                print("decides seguir el camino iluminado hasta que te encuentras con una \n"
                      "sala llena de comida, parece ser donde los guardias guardan todo lo que se requisa de la \n"
                      "prison. Quieres comer o prefieres seguir el camino?\n")
                opcion_comer = input("COMER[C] || SEGUIR[S]: ").upper()
                if opcion_comer == "C":
                    print(
                        "Comiste hasta que ni moverte pudiste, te entro sueño y dormido te quedaste. Un guardia te vio \n"
                        "durmiendo y te devolvió a la carcel. Ahora te esperan 6 meses de aislamiento y toda una vida \n"
                        "en prison.")
                else:
                    print("No te distraes y sigues avanzando, llegas hasta una sala en la cual se encuentra la llave \n"
                          "maestra que abre todas las puertas del universo. Vuelves hacia la puerta he introduces la \n"
                          "llave pero te falta el código...\n"
                          "Vuelves a leer el tallado en la puerta")
                    tiene_llave = True
                    solucion_hipotenusa = float(
                        input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
                    while solucion_hipotenusa != hipotenusa:
                        print("Contraseña incorrecta.")
                        solucion_hipotenusa = float(
                            input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))

                    print(
                        "Correcto! La puerta se ha abierto, destrás de ella se encuentra la zona de despegue. Coges una nave y \n"
                        "te escapas a la velocidad de la luz.")
    else:
        print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
              "Onanaquis, la espécie alienígena mas temida del universo. \n"
              "Quieres combatir mano a mano o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
              )
        opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
        if opcion_combate == "H":
            print("Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                  "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                  "que pierdes la conciencia y finalmente mueres.")
        else:
            print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                  "Es demasiado fuerte y en los primeros 10 segundos te perfora el abdomen con sus \n"
                  "garras, con tus últimos alientos sientes como te enguye poco a poco."
                  )

if opcion == "D":
    print("Intentas abrir la puerta pero esta bloqueada por una cerradura que necesita una llave y \n"
          "un código. En la puerta están talladas las siguientes instrucciones: \n"
          "\n"
          "Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?\n"
          "\n"
          "Con la puerta bloqueada solo nos quedan dos opciones, camino oscuro o camino claro."
          )
    opcion = input("OSCURO[O] || CLARO[C]: ").upper()
    if opcion == "O":
        print("Sigues caminando por el pasillo oscuro, te encuentras una espada y un escudo policial. \n"
              "Que decides lo cojes o lo dejas?"
              )
        opcion_espada_escudo = input("COJER[C] || DEJAR[D]: ").upper()
        if opcion_espada_escudo == "C":
            print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
                  "Onanaquis, la espécie alienígena mas temida del universo. Tuviste suerte de cojer esa espada \n"
                  "y ese escudo.\n"
                  "Quieres combatir o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
                  )
            opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
            if opcion_combate == "H":
                print("Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                      "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                      "que pierdes la conciencia y finalmente mueres.")
            else:
                print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                      "Tras una intesa batalla, consigues derrotarlo. Exploras la sale y no encuentras nada\n"
                      "por lo que decides volver sobre tus pasos. Llegas al inicio y como no tienes la llave \n"
                      "decides seguir el camino iluminado hasta que te encuentras con una \n"
                      "sala llena de comida, parece ser donde los guardias guardan todo lo que se requisa de la \n"
                      "prison. Quieres comer o prefieres seguir el camino?\n")
                opcion_comer = input("COMER[C] || SEGUIR[S]: ").upper()
                if opcion_comer == "C":
                    print(
                        "Comiste hasta que ni moverte pudiste, te entro sueño y dormido te quedaste. Un guardia te vio \n"
                        "durmiendo y te devolvió a la carcel. Ahora te esperan 6 meses de aislamiento y toda una vida \n"
                        "en prison.")
                else:
                    print(
                        "No te distraes y sigues avanzando, llegas hasta una sala en la cual se encuentra la llave \n"
                        "maestra que abre todas las puertas del universo. Vuelves hacia la puerta he introduces la \n"
                        "llave pero te falta el código...\n"
                        "Vuelves a leer el tallado en la puerta")
                    tiene_llave = True
                    solucion_hipotenusa = float(
                        input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
                    while solucion_hipotenusa != hipotenusa:
                        print("Contraseña incorrecta.")
                        solucion_hipotenusa = float(
                            input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))

                    print(
                        "Correcto! La puerta se ha abierto, destrás de ella se encuentra la zona de despegue. Coges una nave y \n"
                        "te escapas a la velocidad de la luz.")

        else:
            print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
                  "Onanaquis, la espécie alienígena mas temida del universo. \n"
                  "Quieres combatir mano a mano o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
                  )
            opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
            if opcion_combate == "H":
                print("Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                      "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                      "que pierdes la conciencia y finalmente mueres.")
            else:
                print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                      "Es demasiado fuerte y en los primeros 10 segundos te perfora el abdomen con sus \n"
                      "garras, con tus últimos alientos sientes como te enguye poco a poco."
                      )

    if opcion == "C":
        print("Sigues el camino iluminado hasta que te encuentras con una sala llena de comida,\n "
              "parece ser donde los guardias guardan todo lo que se requisa de la \n"
              "prison. Quieres comer o prefieres seguir el camino?")
        opcion_comer = input("COMER[C] || SEGUIR[S]: ").upper()
        if opcion_comer == "C":
            print(
                "Comiste hasta que ni moverte pudiste, te entro sueño y dormido te quedaste. Un guardia te vio \n"
                "durmiendo y te devolvió a la carcel. Ahora te esperan 6 meses de aislamiento y toda una vida \n"
                "en prison.")
        else:
            print("No te distraes y sigues avanzando, llegas hasta una sala en la cual se encuentra la llave \n"
                  "maestra que abre todas las puertas del universo.Vuelves al inicio y tienes dos opciones.\n")
            opcion_puerta = input("ABRIR PUERTA[P] || SEGUIR CAMINO OSCURO[S]: ").upper()
            if opcion_puerta == "S":
                print("Sigues por el camino oscuro y dejas la puerta atrás. Te encuentras una espada y un escudo. \n"
                      "Los cojes?")
                opcion_espada_escudo = input("SI[S] || NO[N]: ").upper()
                if opcion_espada_escudo == "S":
                    print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
                          "Onanaquis, la espécie alienígena mas temida del universo. Tuviste suerte de cojer esa espada \n"
                          "y ese escudo.\n"
                          "Quieres combatir o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
                          )
                    opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
                    if opcion_combate == "H":
                        print(
                            "Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                            "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                            "que pierdes la conciencia y finalmente mueres.")
                    else:
                        print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                              "Tras una intesa batalla, consigues derrotarlo. Exploras la sala y no encuentras nada\n"
                              "por lo que decides volver sobre tus pasos. LLegas a la entrada, introduces la \n"
                              "llave pero te falta el código...\n"
                              "Vuelves a leer el tallado en la puerta")
                        tiene_llave = True
                        solucion_hipotenusa = float(
                            input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
                        while solucion_hipotenusa != hipotenusa:
                            print("Contraseña incorrecta.")
                            solucion_hipotenusa = float(
                                input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))

                        print(
                            "Correcto! La puerta se ha abierto, destrás de ella se encuentra la zona de despegue. Coges una nave y \n"
                            "te escapas a la velocidad de la luz.")
                else:
                    print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
                          "Onanaquis, la espécie alienígena mas temida del universo. \n"
                          "Quieres combatir mano a mano o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
                          )
                    opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
                    if opcion_combate == "H":
                        print(
                            "Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                            "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                            "que pierdes la conciencia y finalmente mueres.")
                    else:
                        print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                              "Es demasiado fuerte y en los primeros 10 segundos te perfora el abdomen con sus \n"
                              "garras, con tus últimos alientos sientes como te enguye poco a poco."
                              )

if opcion == "I":
    print("Sigues el camino iluminado hasta que te encuentras con una sala llena de comida,\n "
          "parece ser donde los guardias guardan todo lo que se requisa de la \n"
          "prison. Quieres comer o prefieres seguir el camino?")
    opcion_comer = input("COMER[C] || SEGUIR[S]: ").upper()
    if opcion_comer == "C":
        print(
            "Comiste hasta que ni moverte pudiste, te entro sueño y dormido te quedaste. Un guardia te vio \n"
            "durmiendo y te devolvió a la carcel. Ahora te esperan 6 meses de aislamiento y toda una vida \n"
            "en prison.")
    else:
        print("No te distraes y sigues avanzando, llegas hasta una sala en la cual se encuentra la llave \n"
              "maestra que abre todas las puertas del universo.Vuelves al inicio y tienes dos opciones.\n")
        tiene_llave = True
        opcion_puerta = input("ABRIR PUERTA[P] || SEGUIR CAMINO OSCURO[S]: ").upper()
        if opcion_puerta == "P":
            print("Introduces la llave pero te falta el código...\n"
                  "Lees el tallado en la puerta...")
            tiene_llave = True
            solucion_hipotenusa = float(
                input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
            while solucion_hipotenusa != hipotenusa:
                print("Contraseña incorrecta.")
                solucion_hipotenusa = float(
                    input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
            print(
                "Correcto! La puerta se ha abierto, destrás de ella se encuentra la zona de despegue. Coges una nave y \n"
                "te escapas a la velocidad de la luz.")

        else:
            print("Sigues por el camino oscuro y dejas la puerta atrás. Te encuentras una espada y un escudo. \n"
                  "Los cojes?")
            opcion_espada_escudo = input("SI[S] || NO[N]: ").upper()
            if opcion_espada_escudo == "S":
                print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
                      "Onanaquis, la espécie alienígena mas temida del universo. Tuviste suerte de cojer esa espada \n"
                      "y ese escudo.\n"
                      "Quieres combatir o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
                      )
                opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
                if opcion_combate == "H":
                    print(
                        "Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                        "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                        "que pierdes la conciencia y finalmente mueres.")
                else:
                    print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                          "Tras una intesa batalla, consigues derrotarlo. Exploras la sala y no encuentras nada\n"
                          "por lo que decides volver sobre tus pasos. LLegas a la entrada, introduces la \n"
                          "llave pero te falta el código...\n"
                          "Vuelves a leer el tallado en la puerta")
                    tiene_llave = True
                    solucion_hipotenusa = float(
                        input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))
                    while solucion_hipotenusa != hipotenusa:
                        print("Contraseña incorrecta.")
                        solucion_hipotenusa = float(
                            input("Si tiene 2,74 de altura y 1,5 de anchura, cuanto mide su hipotenusa?"))

                    print(
                        "Correcto! La puerta se ha abierto, destrás de ella se encuentra la zona de despegue. Coges una nave y \n"
                        "te escapas a la velocidad de la luz.")

            else:
                print("Llegas a una inmensa sala iluminada por antorchas ancestrales. En esta sala te espera un \n"
                      "Onanaquis, la espécie alienígena mas temida del universo. \n"
                      "Quieres combatir mano a mano o prefieres huir y rezar para que el Onanaquis te perdone la vida?"
                      )
                opcion_combate = input("COMBATIR[C] || HUIR[H]: ").upper()
                if opcion_combate == "H":
                    print(
                        "Decides empezar a correr pero el Onanaquis te sigue, es muy rápido te pisa los talones, \n"
                        "te alcanza. Te desentraña con sus carras mientras tu gritas desesperado hasta \n"
                        "que pierdes la conciencia y finalmente mueres.")
                else:
                    print("Te envalentonas y decides enfrentarte al alienigena mas temido del universo. \n"
                          "Es demasiado fuerte y en los primeros 10 segundos te perfora el abdomen con sus \n"
                          "garras, con tus últimos alientos sientes como te enguye poco a poco."
                          )
