from flask import Flask
import json

import sys
sys.path.append('/home/operativos/so-exam3')

from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/cpu')
def get_cpuinfo():
    cpu_percent = Stats.get_cpu_percent()
    return json.dumps({'cpu_percent': cpu_percent})

@app.route('/memory')
def get_memoryinfo():
    memory_info = Stats.get_available_memory_ram()
    return json.dumps({'available_memory(MB)': memory_info})

@app.route('/disk')
def get_diskinfo():
    disk_info = Stats.get_hard_disk_space()
    return json.dumps({'disk_space(MB)': disk_info})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
