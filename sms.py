import requests, os, sys, platform, time, datetime
from requests import get

####### COLORS #######
blanco="\033[1;37m"
rojo="\033[1;31m"
verde="\033[1;32m"
amarillo="\033[1;33m"
q_color = "\033[0m"

def banner():
    print("  _____ __  __  _____       ______ _____                ")
    print(" / ____|  \/  |/ ____|     |  ____/ ____|   ┌──────────┐")
    print("| (___ | \  / | (___ ______| |__ | |        |\        /|")
    print(" \___ \| |\/| |\___ \______|  __|| |        |  \    /  |")
    print(" ____) | |  | |____) |     | |___| |____    |    \/    |")
    print("|_____/|_|  |_|_____/      |______\_____|   └──────────┘")
    pass

def sms():
    codigo = input("Escriba el código de país: ")
    celular = input("Escriba el número celular: ")
    mensaje = input("Escriba el sms a enviar: ")

    response = requests.post('https://textbelt.com/text',{
        'phone': codigo + celular,
        'message': mensaje,
        'key': 'textbelt'
    })

    print(response.text)
    tiempo = datetime.datetime.now()
    hora = tiempo.strftime("%X") #X mayuscula
    fecha = tiempo.strftime("%x") #x minuscula
    guardar = open("registro.txt", "a")
    guardar.write(f"\nip = {ip} \nhora = {hora} \nfecha = {fecha} \nmensaje = {mensaje} \nestado = {response.text} \ncelular = {codigo + celular}\n")

def estado():
    textID = input("Escriba el textID del sms: ")
    os.system(f"curl https://textbelt.com/status/{textID}")

def ayuda():
    print("A. ¡No puedo enviar sms después de un intento en el mismo número!")
    print("B. No puedo enviar sms debido al gran uso del sitio web. ")
    print("C. No se puede enviar más de un sms ni siquiera a un número diferente. ")
    print("D. Otro")
    opcion = input(">>> ").lower()
    if opcion == "a" :
        print("Porque esta es solo una versión de demostración, por lo que puede enviar solo 1 sms en un día al mismo número, sin embargo, puede enviar a un número diferente usando vpn")
    elif opcion == "b" :
        print("A veces, cuando el sitio web se usa en gran cantidad, deshabilitan los sms gratuitos por algún tiempo. Espere un momento...")
    elif opcion == "c" :
        print("Por favor revise su vpn cuidadosamente y use solo los mejores vpns. Como nordvpn, protonvpn, etc.")
    elif opcion == "d" :
        print("¡Perdón por cualquier problema! Envíenos su problema por correo electrónico a hackersacademyofindia@gmail.com o puede mencionar su problema en github.com/Sanif007")
    else :
        print("Opción inválida! \nSaliendo")
        exit()

def historial():
    if os.path.exists("registro.txt") :
        with open("registro.txt","r") as file :
            sessions = file.read().splitlines()
            numero_sesiones = len(sessions)
            if numero_sesiones > 1 :
                os.system("python info_sesiones.py")
                mas_detalles = input("¿Quiere ver todas las sesiones? (Default: No): ").lower()
                if mas_detalles == "si" or mas_detalles == "s" :
                    if (platform.system() == "Linux"):
                        os.system("cat registro.txt")
                    else:
                        os.system("type registro.txt")
                else :
                    print("Gracias por usar SMS-EC")
            elif numero_sesiones == 1 :
                print(file.readline)
            else :
                print("El archivo de registro esta vacío o ha ocurrido un error en la lectura.")
    else:
        print("Talves sea la primera vez que usa esta herramienta o el archivo de registro fue eliminado.")


def salir():
    print("Gracias por usar nuestra herramienta")
    exit()

def menu():
    print(verde + "1. Enviar sms anómino {q_color}")
    print(verde + "2. Checkear el estado del sms {q_color}")
    print(verde + "3. Ayuda {q_color}")
    print(verde + "4. Consulta el historial anterior! {q_color}")
    print(verde + "5. Salir {q_color}")
    print()

def opciones():
    opcion = input("Elija una opción: ")
    if opcion == "1":
        sms()
    elif opcion == "2":
        estado()
    elif opcion == "3":
        ayuda()
    elif opcion == "4":
        historial()
    elif opcion == "5":
        salir()
    else:
        print(rojo + "Número inválido {q_color}")
    pass


if (platform.system() == "Linux"):
    os.system("clear")
    os.system("bash request.sh")
else:
    os.system("cls")

banner()
print()

print("Editado por: Darlyn Buenaño")
startTime = datetime.datetime.now().strftime("%X")
print("Programa iniciado a las: " + amarillo + startTime + q_color)
print()

ip = get("https://api.ipify.org").text
print("Ip pública: " + amarillo + ip + q_color)
print()

menu()
opciones()