import cliente as sc
import servidor as ss
import threading as th

porta = 22500

def main():
    th.Thread(target=ss.criarServidor, args=(porta, ), name="Servidor").start()
    th.Thread(target=sc.criarCliente, args=(porta, ), name="Cliente").start()

    print("aqui")

if __name__ == '__main__':
    main()
