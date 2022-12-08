from telegrambot_manager import *
# from keep_alive import keep_alive

def main():
    print(time.asctime() + '-' + 'Started!')
    client.start()
    client.run_until_disconnected()
    print(time.asctime() + '-' +'Stopped!')
    
if __name__ == '__main__':
    # keep_alive()
    main()
