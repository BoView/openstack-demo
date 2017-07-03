from wsgiref import simple_server

from openstack_demo.api import app

def main():
    host = '0.0.0.0'
    port = 8080

    application = app.setup_app()
    srv = simple_server.make_server(host,port,application)

    srv.server_forever()

if __name__ == '__main__':
    main()