import paramiko
import threading
  
sftpURL  = '192.168.15.16'
sftpUser = 'suporte'
sftpPass = 'suporte'

def conectar():
    global ssh
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        ssh.connect(sftpURL, username=sftpUser, password=sftpPass)
    except Exception as e:
        raise Exception(f'Não foi possível conectar... ({e})')

def listar():
    global sftp
    sftp = ssh.open_sftp()
    files = sftp.listdir()
    for file in files:
        if not file.startswith('.'):
            print(f'arquivo: {file}')

def enviar(lista_de_arquivos):
    for nome_arquivo in lista_de_arquivos:
        try:
            print(f'Enviando arquivo: {nome_arquivo}')
            sftp.put(nome_arquivo, nome_arquivo)
        except Exception as e:
            print(f'Não consegui enviar o arquivo: {nome_arquivo}')

def receber(nome_arquivo):
    print(f'Recebendo arquivo: {nome_arquivo}')
    sftp.get(nome_arquivo, nome_arquivo)    

conectar()
listar()
       
try:
    lista = ['eu.txt', 'enviar.py', 'ssh.py','enviar.py', 'ssh.py']
    enviar(lista)
    receber('eu.txt')

except Exception as e:
    print(f'Ocorreu um erro durante a execução.')
    print(e)
    
print('Final....')

ssh.close()
    