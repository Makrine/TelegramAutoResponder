from telegrambot_manager import *


def main():
    print(time.asctime(), '-', 'Started!')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
    
if __name__ == '__main__':
    main()