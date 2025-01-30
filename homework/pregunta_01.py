# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd
import glob
import os



def open_data(input_directory):
    carpetas = ["test/negative", "test/neutral", "test/positive", 
                "train/negative", "train/neutral", "train/positive"]
    test_train = ['test', 'train']
    targets = ['negative', 'neutral', 'positive']

    
    
    # Iteramos sobre las carpetas
    for carpeta in test_train:
        # Aqui se guardaran los datos
        secuencia = []
        path = input_directory + '/' + carpeta

        for target in targets:
            files = glob.glob(f'{path}/{target}/*.txt')
            

            # Se itera sobre cada archivo txt
            for file in files:
                with open(file, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                    secuencia.append((raw_content, target))
        
        # Se crea el archivo test.csv y train.csv
        csv_creator(secuencia, carpeta)

    return secuencia

def csv_creator(data, csv_name):
    ruta = f'files/output/{csv_name}_dataset.csv'
    df = pd.DataFrame(data, columns=['phrase','target'])

    # Crea la carpeta output
    if not os.path.exists('files/output'):
        os.makedirs('files/output')
    # Crea los archivos csv
    df.to_csv(ruta, index=False)



def pregunta_01():
    path = 'files/input'
    # Crea los archivos csv
    datos = open_data(path)

pregunta_01()

# # Para probar si sirve
# path = 'files/output/train_dataset.csv'
# df = pd.read_csv(path)
# negative = df[df['target'] == 'negative']
# print(negative)



"""
La información requerida para este laboratio esta almacenada en el
archivo "files/input.zip" ubicado en la carpeta raíz.
Descomprima este archivo.

Como resultado se creara la carpeta "input" en la raiz del
repositorio, la cual contiene la siguiente estructura de archivos:


```
train/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
test/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
```

A partir de esta informacion escriba el código que permita generar
dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
del repositorio.

Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

Cada archivo tendria una estructura similar a la siguiente:

```
|    | phrase                                                                                                                                                                 | target   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
|  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
|  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
|  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
|  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
```


"""