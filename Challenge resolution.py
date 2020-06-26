import time
real_password = '0546'

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    d = ['0','1','2','3','4','5','6','7','8','9']
    x=0
    y=0
    z=0
    v=0
    numero = d[x]+d[y]+d[z]+d[v]
    c = False
    while(c!=True):
        start_time=time.time() 
        c = check_password(numero)
        elapsed_time=time.time()-start_time
        
        while(elapsed_time <= 0.2):
            x+=1
            numero = d[x]+d[y]+d[z]+d[v]
            start_time=time.time() 
            c = check_password(numero)
            elapsed_time=time.time()-start_time
    
        while(elapsed_time <= 0.3):
            y+=1
            numero = d[x]+d[y]+d[z]+d[v]
            start_time=time.time()
            c = check_password(numero)
            elapsed_time=time.time()-start_time
    
        while(elapsed_time <= 0.4):
            z+=1
            numero = d[x]+d[y]+d[z]+d[v]
            start_time=time.time()
            c = check_password(numero)
            elapsed_time=time.time()-start_time
    
        while(elapsed_time <= 0.5 and c == False):
            v+=1
            numero = d[x]+d[y]+d[z]+d[v]
            start_time=time.time()
            c = check_password(numero)
            elapsed_time=time.time()-start_time
            
            
    return numero
start_time=time.time() 
print(crack_password())
elapsed_time=time.time()-start_time
print(elapsed_time)
    