import network
try:
    import socket
except ImportError:
    import usocket as socket


class APWebserver():
    """
    I figured that everything on the net side of things should be wrapped
    in its own package, to make things a bit easier.
    """

    def __init__(self, ssid, passwd, host_ip):
        self.ap = network.WLAN(network.AP_IF)
        self.ap.config(essid=ssid, password=passwd)

        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind(('', 80))

        self.ap.active(True)
        while self.ap.active() == False:
            pass
        print(f"Server is setup and ready on {self.ap.ifconfig()}")
        self._s.listen(5)


    def wait_connection(self, buffers):
        conn,addr = self._s.accept()
        print(f"Connection from {addr}")
        request = conn.recv(1024)
        print(f"Content = {bytes.decode(request, 'utf-8')}")

        conn.send(self.webpage(buffers))
        conn.close()


    def webpage(self, buffers):
        html = """<html>
        <head><title>SPOKANE ROCKERT METRICS</title><meta http-equiv="refresh" content="3"></head>
        <body>
        """
        for b in buffers:
            html += f"{b}"
        html += "</body></html>"
        return html

