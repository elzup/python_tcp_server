# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import socketserver
    import socket
    import json

    from handles import handler
    from models import log_model

    HOST = socket.gethostbyname('')
    PORT = 4000

    def is_tdu_network(self):
        return True


    def work(self):
        lm = log_model.LogModel()
        while True:
            try:
                json_data = self.request.recv(1024).strip()
                if len(json_data) == 0:
                    break
                if json_data.__class__.__name__ == "bytes":
                    json_data = json_data.decode('UTF-8')
                data = json.loads(json_data)
#                print(data)
# TODO: filter users

                screen_name = data['name']
                ssids = data['SSIDs']
                result = is_tdu_network(ssids)

                lm.InsertLog(sn = screen_name)
                users = lm.get_active_user_wrap()
                res = json.dumps({
                    "result" : result,
                    "message": ("accepted screen_name is " + screen_name if result else "Your network is not in TDU"),
                    "active_users": users
                    })
                self.request.send(res.encode('UTF-8'))
            except (IndexError, KeyError):
                res = json.dumps({
                    "result" : False,
                    "message": "Invalid values"
                    })
                self.request.send(res.encode('UTF-8'))
                break
        self.request.close()

    handler.Handler.set_work(work)
    limit = 1
    while (limit < 10):
        limit += 1
        try:
            server = socketserver.TCPServer((HOST, PORT), handler.Handler)
            break
        except OSError:
            print("port: " + str(PORT) + " is userd")
            PORT += 1

    print('listening', server.socket.getsockname())
    server.serve_forever()
