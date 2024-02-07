import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def send_email_notification(message):
    print('Sending email  ...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        mssg = f'Subject: Site Down\n{message}'
        smtp.sendemail(EMAIL_ADDRESS, EMAIL_ADDRESS, mssg)

def restart_container():
    print('Restarting application ...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.230.236.2', username='root', key_filename='C:/Users/admin/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start <containerId>')
    print(stdout.readline())
    ssh.close()
    
def restart_server_and_container():
    print('Restarting server and container ...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 24521541)
    nginx_server.reboot()

    #restart application
    while True:
        nginx_server = client.load(linode_api4.Instance, 24521541)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break

def monitor_application():
    try:
        response = requests.get('http://165.22.117.74:8080/')
        if response.status_code == 200:
            print('Application running successful')
        else:
            print('Application down!! Fix it')

            #send email to admin
            msg = f'Application returned {response.status_code}'
            send_email_notification(msg)

            #restart application
            restart_container()
            

    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible. Fix the issue'
        send_email_notification(msg)
            
        #restart linode server
        restart_server_and_container()

schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()