import random
import subprocess


def create_pass():
    output = subprocess.check_output(r'powershell -command "[Environment]::GetFolderPath(\"Desktop\")"')
    path = output.decode().strip()
    f = open(f'{path}\\randpass{random.randint(1, 1000)}.txt', "x")
    password = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-=[]'
    password = ''.join([random.choice(password) for _ in range(int(input('Длина пароля: ')))])
    f.write(password)
    f.close()
    return password


print(create_pass())
