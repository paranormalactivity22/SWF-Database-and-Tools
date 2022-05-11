import time
import os

def main():
    data = os.system("Emulador.py")
    if data == 1:
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 10 seconds"
        time.sleep(10)
        os.system("cls")
        main()
    elif data in [5,1280]:
        print "[INFO] Server Parado!"
        raw_input("")
    elif data in [11,2816]:
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 10 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 9 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 8 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 7 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 6 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor5 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 4 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 3 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 2 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor 1 segundo"
        time.sleep(1)
        os.system("cls")
        main()
    else:
        print "[ERROR] Server Caiu, Reiniciar servidor 20 segundos"
        time.sleep(20)
        os.system("cls")
        main()

if __name__=="__main__":
    main()
