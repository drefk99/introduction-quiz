# introduction-quiz v 0.01
This repo is for introduction quiz

## Requisitos.

* Instalar python en su versión 3.6
  * **yum install python36u**

* Tener instalado elasticsearch en la versión 5.2.2 o apache en su versión 2.4.6 
  * Elasticsearch:
    **sudo wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.rpm**
    **sudo rpm -i elasticsearch-5.2.2.rpm**
    **sudo systemctl status elasticsearch.service systemctl start elasticsearch.service**
  * Apache:
    **sudo yum install httpd**
    **sudo systemctl start httpd**

* Preparación del entorno python
 * Posicionarse en la carpeta del reposito
   * **sudo virtualenv -p python3.6 env**
   * **sudo pip install -r requirements.txt**
  
## Ejecución del script

* Se activa el entorno con el comando:
  * **source env/bin/activate**
* El script se ejcuta con el comando:
  * **python send_answers.py "http://Host_para_el_post/puerto" | python -m json.tool**
  
  ## Nota
    * Es importante tener configurado adecuadamente apache para que pueda aceptar los archivos json.
    * En algunos casos se recomienda estar como root para una correcta instalacón de los paquetes.
