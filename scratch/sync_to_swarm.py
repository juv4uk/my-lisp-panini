import re
import socket
import time

def send_lisp(code):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('100.113.68.50', 9101))
        s.sendall(code.encode('utf-8') + b'\n')
        s.close()
        time.sleep(0.1)
    except Exception as e:
        print(f"Failed to send: {e}")

with open('c:/GitHub/my-lisp-panini/roadmap_tasks.my', 'r') as f:
    text = f.read()

task_blocks = re.findall(r'\("([^"]+)" \. \(\s*\(priority \. ([0-9.]+)\)\s*\(capabilities \. \(([^)]*)\)\)\s*\(description \. "([^"]+)"\)\s*\(done \. \((.*?)\)\)\s*\)\)', text)

for t_name, t_prio, t_caps, t_desc, t_done in task_blocks:
    caps_str = t_caps.strip()
    
    # 1. Define task
    define_cmd = f'(define-task (task {t_name}) (priority {t_prio}) (capabilities ({caps_str})) (description "{t_desc}"))'
    print(define_cmd)
    send_lisp(define_cmd)
    
    # 2. If it is marked done (like '1'), complete it.
    if t_done.strip():
        print(f"Completing {t_name}")
        send_lisp(f'(claim-task (task {t_name}))')
        send_lisp(f'(complete-task (task {t_name}) (generation 1))')

# Also force complete the stuck migration tasks explicitly
stuck_tasks = [
    "PANINI-MIGRATE-ANUVRTTI",
    "PANINI-MIGRATE-DHATU",
    "PANINI-MIGRATE-IT",
    "PANINI-MIGRATE-PARIBHASHA",
    "PANINI-MIGRATE-PRATYAHARA",
    "PANINI-MIGRATE-PRATYAYA",
    "PANINI-CLEANUP-FOUNDATION",
    "PANINI-VIDYUT-AUDIT"
]
for t in stuck_tasks:
    send_lisp(f'(claim-task (task {t}))')
    send_lisp(f'(complete-task (task {t}) (generation 1))')

print("Done syncing.")
