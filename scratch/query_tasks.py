import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        s.connect(('100.113.68.50', 9101))
        req = b'(next-best-action (capabilities ("my-lisp-panini")))\n'
        s.sendall(req)
        
        # Read response
        resp = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            resp += chunk
            if b')' in chunk: # crude heuristic for end of sexpr
                break
                
        print("SWARM_RESPONSE:")
        print(resp.decode('utf-8'))
        s.close()
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
