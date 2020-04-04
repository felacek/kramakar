import server
import data
import player
import thing
import reset

def main():
    reset.run()
    data.run()
    server.run('localhost', 8080)

if __name__ == '__main__':
    main()
