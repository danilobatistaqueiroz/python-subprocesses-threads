**process.py** e **child.py**  

usam `subprocess.Popen` para enviar e receber dados entre ambos os processos.  


**main.py** e **tray.py**  

usam `subprocess.Popen` do mesmo modo, porém, ambos abrem uma thread com `threading.Thread` para ler os dados recebidos.  

