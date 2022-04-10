import os

import multiprocessing

port = os.environ.get("LISTEN_PORT", 5000)
bind = f"0.0.0.0:{port}"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "-"
errorlog = "-"
