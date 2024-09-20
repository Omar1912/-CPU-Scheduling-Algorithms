
from dataclasses import dataclass



process_data = [
    [1, 0, 10, 2, 3, 0, 0, 0],
    [2, 1, 8, 4, 2,  0, 0, 0],
    [3, 3, 14, 6, 3,  0, 0, 0],
    [4, 4, 7, 8, 1,  0, 0, 0],
    [5, 6, 5, 3, 0,  0, 0, 0],
    [6, 7, 4, 6, 4,  0, 0, 0],
    [7, 8, 6, 9, 2,  0, 0, 0],
]

@dataclass
class Process:
    process_id: int
    arrival_time: int
    burst_time: int
    comeback: int
    priority: int
    ready_queue_arrival_time: int
    comeback_flage_time: int 
    run_time: int
    cpu_remianing:int
    
    
    
process_list=[]
for p in process_data:
    obj=Process(p[0], p[1], p[2],p[3] ,p[4], p[5],p[6],p[7],p[2]) 
    process_list.append(obj)
    



ready_queue: list[Process] = []
waiting_queue:list[Process] = []
gantt_chart = []
Cpu: list[Process] = []
total_waiting_time = 0
total_turnaround_time= 0
number_of_completed_processes = 0
waiting_time = 0
compileation_time = 0
current_time = 0 

for timeunit in range(201):
    for process in process_data:
        if process [1] == timeunit:
            ready_queue.append(process)
    
    
    
    
    
    
    if ready_queue and not Cpu :
        Cpu.append(ready_queue.pop(0))
        arrive_Cpu=timeunit
        temporarly = Cpu.pop(0)
        total_waiting_time += temporarly[5]
        temporarly[5] +=1
        Cpu.append(temporarly)
        temporarly = []
        
    
    if waiting_queue:
        
        for waiting_process in waiting_queue:
            waiting_process[7] +=1
            if waiting_process[7] == waiting_process[3]:
                temp=waiting_queue.pop(waiting_queue.index(waiting_process))
                temp[7] = 0
                temp[1]=timeunit
                ready_queue.append(temp)  
    ready_queue.sort(key=lambda x: x[2])              

    if (Cpu and timeunit == compileation_time + Cpu[0][2]) or timeunit == 200 :
        
        compileation_time = timeunit
        #print(compileation_time)
        if timeunit == 200:
            Cpu[0][6] = compileation_time - Cpu[0][1]
            total_turnaround_time+=Cpu[0][6]
            #print(Cpu) 
        
        Cpu[0][6] = compileation_time - Cpu[0][1]
        total_turnaround_time += Cpu[0][6]
        Cpu[0][6] = 0
        #print(Cpu)
        waiting_queue.append(Cpu[0]) 
        number_of_completed_processes +=1
        gantt_chart.append((arrive_Cpu, Cpu[0][0] ,compileation_time))
        Cpu=[]
       
        
        
        
     
                          
    
    if ready_queue and not Cpu :
        Cpu.append(ready_queue.pop(0))
        arrive_Cpu=timeunit
        temporarly = Cpu.pop(0)
        total_waiting_time += temporarly[5]
        Cpu.append(temporarly)
        temporarly = []
    
    if ready_queue:
     for ready in ready_queue:
        ready[5]+=1    
         
     

print("\nGntt Chart:")
for item in gantt_chart:
    print(f"Start Time: {item[0]}, Process {item[1]}, End Time: {item[2]}")
    
print("waiting:",total_waiting_time)
average_waiting_time=total_waiting_time/number_of_completed_processes
average_turnaround_time=total_turnaround_time/number_of_completed_processes
print("Average waiting time:")
print(average_waiting_time)
print("\n")
print("Average trunaround time:")
print(average_turnaround_time)
print("\n")

print(number_of_completed_processes)
            