import json
import random
import requests
from http.server import BaseHTTPRequestHandler
from helpers import http_server
from domonic import *

# urllib3 for url parse


class BookHandler(BaseHTTPRequestHandler):
    # Handler for the GET random number info
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        number = random.randint(0, 100)
        resp = requests.get(f"http://numbersapi.com/{number}")
        respon = render(
            html(
                head(
                ),
                body(
                    style(
                        'BODY {background: url(https://capital2020.ru/d/mgtu_im_n_e_baumana_moskva.jpg) no-repeat; margin: 0px};',
                        _type="text/css",
                        ),
                    header(b('Random interesting fact about ', number,
                    _style =
                    '''font-size: 30px;
                    color: green;
                    position: absolute;
                    width: 100%;
                    text-align: center;
                    top: 5%;
                    ''')),
                    p(resp.content.decode(),
                      _style=
                      '''font-size: 20px;
                      position: absolute;
                      text-align: center;
                      width: 100%;
                      top: 15%;
                      ''')
                )
            )
        )
        self.wfile.write(respon.encode())



if __name__ == "__main__":
    server = http_server.Server(handler=BookHandler)
    server.run()
