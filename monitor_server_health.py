import psutil
CPU_THRESHOLD = 80 # set the threshold value
try:
    if __name__ == "__main__":  
        while True:
            cpu_in_percentage = psutil.cpu_percent(1)  # interval of 1 second
            # chaking cpu usges
            if cpu_in_percentage <= CPU_THRESHOLD:
                print(f"Current CPU use in percentage {cpu_in_percentage} %")
            # chaking crosing threshold
            if cpu_in_percentage > CPU_THRESHOLD:
               print(f"Alert! CPU usage exceeds threshold: {cpu_in_percentage}%")
## If user interpated in monitoring it will shows the error            
except:
    print("\nMonitoring interrupted by the user.")