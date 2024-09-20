

PROCESS_DATA = [
    [1, 0, 10, 2, 3],
    [2, 1, 8, 4, 2],
    [3, 3, 14, 6, 3],
    [4, 4, 7, 8, 1],
    [5, 6, 5, 3, 0],
    [6, 7, 4, 6, 1],
    [7, 8, 6, 9, 2],
]

class Process:
	def __init__(self, process_id, arrival_time, burst_time, comeback, priority):
		self.process_id = process_id
		self.arrival_time = arrival_time
		self.burst_time = burst_time
		self.comeback = comeback
		self.priority = priority
		self.ready_queue_arrival_time = 0
		self.comeback_flag_time = 0
		self.run_time = 0
		self.cpu_remianing = 0
		self.ready_queue_timer = 0
		self.temp_priority = 0
		self.comeback_flage_time = 0



    
def non_primitive_scheduler(process_data: list[list], schedular_time: int=200):
	process_list=[]
	for p in process_data:
	    obj=Process(*p)
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
	      
	for timeunit in range(schedular_time+1):
	   
	  
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
	        ready_process.ready_queue_timer += 1
	        if ready_process.ready_queue_timer == 6:
	            ready_process.priority -=1
	            ready_process.ready_queue_timer = 0
	            if ready_process.priority < 0:
	               ready_process.priority = 0 
	               
	    
	    ready_queue.sort(key=lambda x:(x.priority,x.ready_queue_arrival_time))

	    
	    
	    if ready_queue and not Cpu:
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        Cpu[0].ready_queue_timer = 0
	        total_waiting_time += timeunit-Cpu[0].ready_queue_arrival_time
	    
	    if Cpu and (timeunit == compileation_time + Cpu[0].burst_time or timeunit == 200 ):
	        
	        compileation_time = timeunit

	        # time in cpu -> execution time
	        total_turnaround_time += Cpu[0].burst_time
	        waiting_queue.append(Cpu[0]) 
	        number_of_completed_processes +=1
	        gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,compileation_time ))
	        Cpu=[]
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit


	    total_waiting_time += timeunit - Cpu[0].ready_queue_arrival_time

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

	print(f"number_of_completed_processes: {number_of_completed_processes}")



def primitive_schedular(process_data: list[list], schedular_time: int=200):
	process_list=[]
	for p in process_data:
	    obj=Process(*p) 
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
	      
	for timeunit in range(schedular_time+1):
	   
	    if Cpu:
	        Cpu[0].run_time+=1
	    
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
	        ready_process.ready_queue_timer += 1
	        if ready_process.ready_queue_timer == 6:
	            ready_process.temp_priority -=1
	            ready_process.ready_queue_timer = 0
	            if ready_process.temp_priority < 0:
	               ready_process.temp_priority = 0 
	              
	    
	    ready_queue.sort(key=lambda x:(x.temp_priority,x.ready_queue_arrival_time))
	    
	    if ready_queue and not Cpu:
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        Cpu[0].ready_queue_timer = 0
	    
	    if ready_queue and Cpu:
	        
	        if Cpu[0].burst_time-Cpu[0].run_time == 0:
	           Cpu[0].run_time=0
	           compileation_time = timeunit
	           total_turnaround_time += compileation_time - Cpu[0].arrival_time
	           Cpu[0].temp_priority=Cpu[0].priority
	           waiting_queue.append(Cpu[0])
	           number_of_completed_processes += 1
	           gantt_chart.append((arrive_Cpu, Cpu[0].process_id, compileation_time))
	           Cpu=[]
	           Cpu.append(ready_queue.pop(0)) 
	           arrive_Cpu=timeunit
	           ready_queue.sort(key=lambda x:(x.temp_priority,x.ready_queue_arrival_time))

	        
	        elif ready_queue[0].temp_priority < Cpu[0].temp_priority or (Cpu[0].temp_priority == ready_queue[0].temp_priority and ready_queue[0].ready_queue_arrival_time < Cpu[0].ready_queue_arrival_time ):
	            Cpu[0].ready_queue_arrival_time=timeunit
	                
	                
	            ready_queue.append(Cpu[0])
	            gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,Cpu[0].ready_queue_arrival_time))
	            ready_queue.sort(key=lambda x:(x.temp_priority,x.ready_queue_arrival_time))
	            Cpu =[]
	            Cpu.append(ready_queue.pop(0))
	            arrive_Cpu=timeunit
	            ready_queue.sort(key=lambda x:(x.temp_priority,x.ready_queue_arrival_time))

	         

	        total_waiting_time += (timeunit-Cpu[0].ready_queue_arrival_time)
	            
	    	
	    
	       
	   
	print("\nGntt Chart:")
	for item in gantt_chart:
	    print(f"Start Time: {item[0]}, Process {item[1]}, End Time: {item[2]}")
	   

	average_waiting_time=total_waiting_time/number_of_completed_processes
	average_turnaround_time=total_turnaround_time/number_of_completed_processes
	print("Average waiting time:")
	print(average_waiting_time)
	print("\n")
	print("Average trunaround time:")
	print(average_turnaround_time)
	print("\n")

	print(f"number_of_completed_processes: {number_of_completed_processes}")
	   


def round_robin_schedular(process_data: list[list], schedular_time: int=200):
	process_list=[]
	for p in process_data:
	    obj=Process(*p) 
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
	time_Q = 0

	for timeunit in range(schedular_time+1):
	   
	  
	    for process in process_list:
	        if process.arrival_time == timeunit:
	           process.ready_queue_arrival_time=timeunit
	           ready_queue.append(process)
	   
	    tmp_wait_queue = waiting_queue.copy() or []
	    for waiting_process in waiting_queue:
	         waiting_process.comeback_flage_time += 1
	         
	         
	    finish_wait_queue = [p for p in waiting_queue if p.comeback_flage_time==p.comeback]
	    waiting_queue = [p for p in waiting_queue if p.comeback_flage_time!=p.comeback]
	    for p in finish_wait_queue:
	        total_turnaround_time += p.comeback

	        p.comeback_flage_time = 0
	        p.ready_queue_arrival_time = timeunit
	        ready_queue.append(p)
	    
	    if ready_queue and not Cpu:
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        total_waiting_time += timeunit-Cpu[0].ready_queue_arrival_time
	        
	     
	    if ready_queue and Cpu:
	      if Cpu[0].burst_time-Cpu[0].run_time==0:
	        Cpu[0].run_time=0
	        time_Q=0
	        compileation_time = timeunit
	        total_turnaround_time += compileation_time - Cpu[0].arrival_time
	        Cpu[0].cpu_remianing=Cpu[0].burst_time
	        waiting_queue.append(Cpu[0])
	        number_of_completed_processes += 1
	        gantt_chart.append((arrive_Cpu, Cpu[0].process_id, compileation_time))
	        Cpu=[]
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        time_Q=0
	        
	      elif time_Q==5:
	            Cpu[0].ready_queue_arrival_time=timeunit
	            ready_queue.append(Cpu[0])
	            gantt_chart.append((arrive_Cpu, Cpu[0].process_id, Cpu[0].ready_queue_arrival_time))
	            Cpu=[]
	            Cpu.append(ready_queue.pop(0))
	            arrive_Cpu=timeunit
	            total_waiting_time += timeunit - Cpu[0].ready_queue_arrival_time
	            time_Q=0
	            
	    
	    Cpu[0].run_time+=1
	    time_Q+=1
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

	print(f"number_of_completed_processes: {number_of_completed_processes}")



def shortest_job_first_schedular(process_data: list[list], schedular_time: int=200):
	process_list=[]
	for p in process_data:
	    obj=Process(*p) 
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

	for timeunit in range(schedular_time+1):
	    for process in process_list:
	        if process.arrival_time == timeunit:
	            ready_queue.append(process)
	    
	    
	    
	    
	    
	    
	    if ready_queue and not Cpu :
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        temporarly = Cpu.pop(0)
	        total_waiting_time += temporarly.ready_queue_arrival_time
	        temporarly.ready_queue_arrival_time +=1
	        Cpu.append(temporarly)
	        temporarly = []
	        
	    
	    # Handle wait queue      
	    for waiting_process in waiting_queue:
	         waiting_process.comeback_flage_time += 1
	         
	         
	    finish_wait_queue = [p for p in waiting_queue if p.comeback_flage_time==p.comeback]
	    waiting_queue = [p for p in waiting_queue if p.comeback_flage_time!=p.comeback]
	    for p in finish_wait_queue:
	        total_turnaround_time += p.comeback

	        p.comeback_flage_time = 0
	        p.ready_queue_arrival_time = timeunit
	        ready_queue.append(p) 



	    ready_queue.sort(key=lambda x: x.burst_time)              

	    if (Cpu and timeunit == compileation_time + Cpu[0].burst_time) or timeunit == 200 :
	        
	        compileation_time = timeunit
	        total_turnaround_time+= compileation_time - Cpu[0].arrival_time
	        waiting_queue.append(Cpu[0]) 
	        number_of_completed_processes +=1
	        gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,compileation_time))
	        Cpu=[]
	                          
	    
	    if ready_queue and not Cpu :
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        temporarly = Cpu.pop(0)
	        total_waiting_time += temporarly.ready_queue_arrival_time
	        Cpu.append(temporarly)
	        temporarly = []
	    
	    if ready_queue:
	     for ready in ready_queue:
	        ready.ready_queue_arrival_time +=1    
	         
	     

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

	print(f"number_of_completed_processes: {number_of_completed_processes}")



def shortest_remaining_job_first_schedular(process_data: list[list], schedular_time: int=200):
	process_list=[]
	for p in process_data:
	    obj=Process(*p) 
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
	      
	for timeunit in range(schedular_time+1):
	   
	  
	    for process in process_list:
	        if process.arrival_time == timeunit:
	           process.ready_queue_arrival_time=timeunit
	           ready_queue.append(process)
	   
	   
	    for waiting_process in waiting_queue:
	         waiting_process.comeback_flage_time += 1
	         
	         
	    finish_wait_queue = [p for p in waiting_queue if p.comeback_flage_time==p.comeback]
	    waiting_queue = [p for p in waiting_queue if p.comeback_flage_time!=p.comeback]
	    for p in finish_wait_queue:
	        total_turnaround_time += p.comeback

	        p.comeback_flage_time = 0
	        p.ready_queue_arrival_time = timeunit
	        ready_queue.append(p)
	        


	               
	   
	          
	    ready_queue.sort(key=lambda x:(x.cpu_remianing,x.ready_queue_arrival_time))
	    
	    # if cpu is empty get least time from the ready q
	    # eslse compare process in ready q with cpu 
	    
	    if ready_queue and not Cpu:
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        total_waiting_time += timeunit-Cpu[0].ready_queue_arrival_time
	    
	       
	       
	    elif ready_queue and Cpu:
	        if  Cpu[0].burst_time-Cpu[0].run_time==0:	           
	           Cpu[0].run_time=0
	           compileation_time = timeunit
	           total_turnaround_time += compileation_time - Cpu[0].arrival_time
	           Cpu[0].cpu_remianing=Cpu[0].burst_time
	           waiting_queue.append(Cpu[0])
	           number_of_completed_processes += 1
	           gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,compileation_time))
	           Cpu=[]
	           Cpu.append(ready_queue.pop(0))
	           arrive_Cpu = timeunit

	        else:
	          rimaining = Cpu[0].burst_time-Cpu[0].run_time
	          if  rimaining > ready_queue[0].burst_time or ( rimaining == ready_queue[0].burst_time and ready_queue[0].arrival_time<Cpu[0].arrival_time):
	                 Cpu[0].ready_queue_arrival_time=timeunit
	                 ready_queue.append(Cpu[0])
	                 ready_queue.sort(key=lambda x:(x.cpu_remianing,x.ready_queue_arrival_time))
	                 gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,Cpu[0].ready_queue_arrival_time))
	                 Cpu=[]
	                 Cpu.append(ready_queue.pop(0))
	                 arrive_Cpu=timeunit
	    total_waiting_time += timeunit - Cpu[0].ready_queue_arrival_time
	            

	         
	    
	    Cpu[0].run_time+=1
	print("\nGntt Chart:")
	for item in gantt_chart:
	    print(f"Start Time: {item[0]}, Process {item[1]}, End Time: {item[2]}")
	   

	average_waiting_time=total_waiting_time/len(process_list)
	average_turnaround_time=total_turnaround_time/number_of_completed_processes
	print("Average waiting time:")
	print(average_waiting_time)
	print("\n")
	print("Average trunaround time:")
	print(average_turnaround_time)
	print("\n")

	print(f"number_of_completed_processes: {number_of_completed_processes}")


	

def first_come_first_served_schedular(process_data: list[list], schedular_time: int=200):
	process_list=[]
	for p in process_data:
	    obj=Process(*p) 
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

	for timeunit in range(schedular_time+1):
	    
	    for process in process_list:
	        if process.arrival_time == timeunit:
	            process.ready_queue_arrival_time = timeunit
	            ready_queue.append(process)
	            
	    
	    # Handle wait queue      
	    for waiting_process in waiting_queue:
	         waiting_process.comeback_flage_time += 1
	         
	         
	    finish_wait_queue = [p for p in waiting_queue if p.comeback_flage_time==p.comeback]
	    waiting_queue = [p for p in waiting_queue if p.comeback_flage_time!=p.comeback]
	    for p in finish_wait_queue:
	        total_turnaround_time += p.comeback

	        p.comeback_flage_time = 0
	        p.ready_queue_arrival_time = timeunit
	        ready_queue.append(p) 
	    
	    
	    
	    if ready_queue and not Cpu :
	        Cpu.append(ready_queue.pop(0))
	        arrive_Cpu=timeunit
	        total_waiting_time += timeunit-Cpu[0].ready_queue_arrival_time
	        total_turnaround_time += timeunit-Cpu[0].ready_queue_arrival_time
	        Cpu[0].ready_queue_arrival_time=0
	        
	        
	    


	    if Cpu and (timeunit == compileation_time + Cpu[0].burst_time or timeunit == 200 ):
	        
	        compileation_time = timeunit
	        # time in cpu -> execution time
	        total_turnaround_time += compileation_time-Cpu[0].arrival_time
	        waiting_queue.append(Cpu[0]) 
	        number_of_completed_processes +=1
	        gantt_chart.append((arrive_Cpu, Cpu[0].process_id ,compileation_time))
	        Cpu=[]
	                             
	    
	        if ready_queue:
	            Cpu.append(ready_queue.pop(0))
	            arrive_Cpu=timeunit
	            total_waiting_time += timeunit-Cpu[0].ready_queue_arrival_time
	            total_turnaround_time += timeunit-Cpu[0].ready_queue_arrival_time
	         
	     

	print("\nGntt Chart:")
	for item in gantt_chart:
	    print(f"Start Time: {item[0]}, Process {item[1]}, End Time: {item[2]}")

	    
	print("waiting:",total_waiting_time)
	average_waiting_time=total_waiting_time/number_of_completed_processes
	average_turnaround_time=total_turnaround_time/len(process_list)
	print("Average waiting time:")
	print(average_waiting_time)
	print("\n")
	print("Average trunaround time:")
	print(average_turnaround_time)
	print("\n")

	print(f"number_of_completed_processes: {number_of_completed_processes}")
	            


if __name__ == "__main__":
    while True:

	    print("\nWelcome to CPU Scheduler Simulator.")
	    print("Which scheduler algorithm would you like to run?")
	    print("1. First Come First Served")
	    print("2. Shortest Job First")
	    print("3. Shortest Remaining Time First")
	    print("4. Round Robin with Q=5")
	    print("5. Preemptive Priority")
	    print("6. Non-preemptive Priority")
	    print("Enter 'q' to quit.")

	    user_input = input("Enter the number of your choice or 'q' to exit: ")

	    if user_input.lower() == 'q':
	        print("Exiting the CPU Scheduler Simulator.")
	        break

	    if not user_input.isdigit() or not 1 <= int(user_input) <= 6:
	    	print("Invalid input. Please enter a number between 1 and 6, or 'q' to exit.")
	    	continue

	    if int(user_input) == 1:
	    	print("runing first_come_first_served_schedular:\n")
	    	first_come_first_served_schedular(process_data=PROCESS_DATA)
	    	print(f"finish first_come_first_served_schedular.\n")

	    elif int(user_input) == 2:
	    	print("runing shortest_job_first_schedular:\n")
	    	shortest_job_first_schedular(process_data=PROCESS_DATA)
	    	print("finish shortest_job_first_schedular.\n")

	    elif int(user_input) == 3:
	    	print("runing shortest_remaining_job_first_scheduler:\n")
	    	shortest_remaining_job_first_schedular(process_data=PROCESS_DATA)
	    	print("finish shortest_remaining_job_first_scheduler.\n")

	    elif int(user_input) == 4:
	    	print("runing round_robin_schedular:\n")
	    	round_robin_schedular(process_data=PROCESS_DATA)
	    	print("finish round_robin_schedular.\n")

	    elif int(user_input) == 5:
	    	print("runing primitive_schedular:\n")
	    	primitive_schedular(process_data=PROCESS_DATA)
	    	print("finish primitive_schedular.\n")

	    elif int(user_input) == 6:
	    	print("runing non_primitive_scheduler:\n")
	    	non_primitive_scheduler(process_data=PROCESS_DATA)
	    	print("finish non_primitive_scheduler.\n")





