# CPU Scheduling Algorithms Simulator
This project implements a simulation of various CPU scheduling algorithms used in operating systems. The program allows users to select from multiple scheduling strategies and simulates process scheduling over a specified time frame.

### Project Overview
The program simulates the following CPU scheduling algorithms:
1. **First Come First Served (FCFS)**
2. **Shortest Job First (SJF)**
3. **Shortest Remaining Time First (SRTF)**
4. **Round Robin (with time quantum = 5)**
5. **Preemptive Priority Scheduling**
6. **Non-preemptive Priority Scheduling** 
 
For each algorithm, the program calculates and displays the Gantt chart, average waiting time, and average turnaround time. The simulation runs for a total of 200 time units.

### Features
- Process Data Simulation: Includes a predefined set of processes, each with arrival time, burst time, and priority.
- Gantt Chart Generation: Displays the sequence in which processes are scheduled.
- Average Waiting & Turnaround Times: Computes these metrics for each scheduling algorithm.
- Preemption & Aging: Supports preemption for certain algorithms and includes priority aging to prevent starvation.

### Scheduling Algorithms
1. **First Come First Served (FCFS)**:
Processes are scheduled in the order they arrive, without preemption.

2. **Shortest Job First (SJF)**:
Processes with the shortest burst time are scheduled first. No preemption.

3. **Shortest Remaining Time First (SRTF)**:
Preemptive version of SJF, where the process with the shortest remaining time is selected.

4. **Round Robin (with time quantum = 5)** : 
Each process is assigned a fixed time slice (quantum). Once a process uses its quantum, it is moved to the back of the queue.

5. **Preemptive Priority Scheduling**Processes are scheduled based on priority, with higher priority processes preempting lower ones. Includes aging to dynamically adjust priorities.

6. **Non-preemptive Priority Scheduling** 
Similar to preemptive priority scheduling, but processes are not interrupted once they start executing.

### Files
- cpu_process_schedular.py: Contains all the scheduling algorithms, the process simulation, and user interaction logic.

### How It Works
The simulator asks the user to choose a scheduling algorithm to run. Once selected, the chosen algorithm schedules processes based on their arrival times, burst times, and priorities. It prints the Gantt chart and computes the average waiting time and turnaround time for each process.

### Example Process Data
The following processes are used in the simulation:

| Process | Arrival Time | Burst Time | Priority |
|---------|--------------|------------|----------|
| P1      | 0            | 10         | 3        |
| P2      | 1            | 8          | 2        |
| P3      | 3            | 14         | 3        |
| P4      | 4            | 7          | 1        |
| P5      | 6            | 5          | 0        |
| P6      | 7            | 4          | 1        |
| P7      | 8            | 6          | 2        |
