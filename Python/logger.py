from datetime import datetime

class Logger:
    def __init__(self, filename="logs.txt"):
        self.filename = filename

    def log(self, site, user, status, success):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"[{now}] Site: {site}, User: {user}, Status: {status}, Result: {'SUCCESS' if success else 'FAILED'}\n"
        with open(self.filename, "a", encoding='utf-8') as f:
            f.write(msg)
