
from dataclasses import dataclass



process_data = [
    [1, 0, 10, 2, 3, 0, 0, 0, 0],
    [2, 1, 8, 4, 2,  0, 0, 0, 0],
    [3, 3, 14, 6, 3,  0, 0, 0, 0],
    [4, 4, 7, 8, 1,  0, 0, 0, 0],
    [5, 6, 5, 3, 0,  0, 0, 0, 0],
    [6, 7, 4, 6, 1,  0, 0, 0, 0],
    [7, 8, 6, 9, 2,  0, 0, 0, 0],
]

@dataclass
class Process:
    process_id: int
    arrival_time: int
    burst_time: int
    comeback: int
    priority: int
    ready_queue_arrival_time: int
    comeback_flag_time: int 
    run_time: int
    cpu_remianing:int
    ready_queue_timer: int
    
    
    
process_list=[]
for p in process_data:
    obj=Process(p[0], p[1], p[2],p[3] ,p[4], p[5],p[6],p[7],p[2],p[8]) 
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
   
  
    for process in process_list:
        if process.arrival_time == timeunit:
           process.ready_queue_arrival_time=timeunit
           ready_queue.append(process)
    
       
    
    for waiting_process in waiting_queue:
         waiting_process.comeback_flag_time += 1
         
         
    finish_wait_queue = [p for p in waiting_queue if p.comeback_flag_time==p.comeback]
    waiting_queue = [p for p in waiting_queue if p.comeback_flag_time!=p.comeback]
    for p in finish_wait_queue:
        total_turnaround_time += p.comeback
        p.ready_queue_timer=0
        p.comeback_flag_time = 0
        p.ready_queue_arrival_time = timeunit
        ready_queue.append(p)
   
    for ready_process in ready_queue:
        #print(f"ready{ready_queue}")
        ready_process.ready_queue_timer += 1
        #print((ready_process.process_id,ready_process.ready_queue_timer))
        if ready_process.ready_queue_timer == 6:
            ready_process.priority -=1
            ready_process.ready_queue_timer = 0
            if ready_process.priority < 0:
               ready_process.priority = 0 
               
        #print(f"after{ready_queue}")        
    
    ready_queue.sort(key=lambda x:(x.priority,x.ready_queue_arrival_time))
    
    
    
    if ready_queue and not Cpu:
        Cpu.append(ready_queue.pop(0))
        arrive_Cpu=timeunit
        Cpu[0].ready_queue_timer = 0
        total_waiting_time += timeunit-Cpu[0].ready_queue_arrival_time
        #print(f"{Cpu}")
    
    if Cpu and (timeunit == compileation_time + Cpu[0].burst_time or timeunit == 200 ):
        
        compileation_time = timeunit
        print(compileation_time) 
        #print(Cpu)

        # time in cpu -> execution time
        total_turnaround_time += Cpu[0].burst_time
        waiting_queue.append(Cpu[0]) 
        number_of_completed_processes +=1
        gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,compileation_time ))
        Cpu=[]
        #print(ready_queue)
        #ready_queue.sort(key=lambda x:(x.priority,x.ready_queue_arrival_time))
        #print(f"ready {[(p.process_id,p.priority,p.ready_queue_timer) for p in ready_queue]}")
        Cpu.append(ready_queue.pop(0))
        arrive_Cpu=timeunit
        #print(Cpu)
    #print(f"ready {[(p.process_id,p.priority,p.ready_queue_timer) for p in ready_queue]}")

    #print(ready_queue)
                               
    #print(Cpu) 
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