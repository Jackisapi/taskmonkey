import psutil
import time
# For stat monitoring
from keyboard import is_pressed as pressed


# For cpu and mem info quiting the two menus


def cpu_info():
    cpu_percent = str(psutil.cpu_percent(3))
    cpu_clock = str(psutil.cpu_freq())
    print(type(cpu_clock))
    # Fetch the current CPU percent usage every three seconds
    print("Percent usage " + cpu_percent + "% \n Ghz: " + cpu_clock)


def mem_info():
    swap_percent = str(psutil.swap_memory())
    virt_percent = str(psutil.virtual_memory())
    print("Swap: " + swap_percent + '\n ' + virt_percent)


def task_man():
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            process_name = proc.name()
            process_id = proc.pid
            print(process_name, ' ::: ', process_id)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def temp():
    cpu_temp = psutil.sensors_temperatures(fahrenheit=False)['coretemp']
    nvme_temp = psutil.sensors_temperatures(fahrenheit=False)['nvme']
    while True:
        print(str(cpu_temp) + "\n" + str(nvme_temp))
        time.sleep(5)


while True:
    print("Hello and Welcome to snake task")
    task = input("For cpu type cpu ,memory type mem  Tasks type tasks,or type in exit to exit ")
    if task.upper() == "CPU":
        print("Press q to stop displaying results ")
        while not pressed('q'):
            cpu_info()
    elif task.upper() == "MEM":
        print("Press q to stop displaying results ")
        while not pressed('q'):
            mem_info()
    elif task.upper() == "TASKS":
        task_man()
    elif task.upper() == "TEMP":
        while not pressed('q'):
            temp()
    elif task.upper() == "EXIT":
        exit("Thank you have a nice day")
