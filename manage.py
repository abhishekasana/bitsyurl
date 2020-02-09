from app import app

from flask_script import Manager, Server


manager = Manager(app)

server = Server(host='localhost', port='5000')
manager.add_command("runserver", server)

if __name__ == "__main__":
    manager.run()
