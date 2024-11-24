from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
    print('This program requires at lesson 2 processes.')
else:
    if rank == 0:
        data = {'key 1 ': 'value1', 'Key 2': 'Value 2'}
        comm.send(data, desst = 1 )
        print("send data from process 0")
    elif rank == 1:
        data = comm.recv(source=0)
        print(f"received data at process 1 :{data}")
    else:
        print (f'Process {rank} is idle')
