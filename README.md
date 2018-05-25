# so-exam3
**Nombre:** Laura Isabella Tabares Perez  
**Código:** A00054120  
**URL github:** https://github.com/Lauraitp/so-exam3/tree/laura-exam3  

____________

## punto 3: Implementar un servicio web en Flask

Para la impementación de este punto dese debe:   
1. crear una carpeta op_stats, en ella crear un archivo app.py y stats.py  
En el archivo stats.py debe ir lo siguiente:  

```Console
import psutil

class Stats():

  @classmethod
  def get_cpu_percent(cls):
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

  @classmethod
  def get_available_memory_ram(cls):
    available_memory = psutil.virtual_memory().available
    return available_memory

  @classmethod
  def get_hard_disk_space(cls):
    disk_space = psutil.disk_usage('/').free
    return disk_space
```  

**NOTA:** Es importante tener instalada psutil.

Por otro lado en app.py debe ir:  

```Console
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
```

Para correr los dos archivos, primero se debe seguir el siguiente comando:  
```Console
python stats.py
```  
Y a continuaciòn: :  
```Console  
python app.py  
```
Para luego abrir Postman, que los descarè en  la siguinete pàgina: https://www.getpostman.com/  
En la aplicación de postman se debe ir al adirección con la que se ingresó a Putty, en mi caso 192.168.1.21 con el puerto 8080 y la dirección cpu, para ver solo el consumo de la misma.    
![](imagenes/cpu.png)

para la memoria RAM disponible es: 192.168.1.21:8080/memory  
![](imagenes/memory.png)  

Y por último para el espacio disponible en el disco: 192.168.1.21:8080/disk
  
![](imagenes/disk.png)  


![](imagenes/peticiones.png)  

## Punto 4: Implemente las pruebas unitarias para los servicios empleando Fixtures y Mocks.  

