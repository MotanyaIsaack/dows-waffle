from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

no_of_processes = comm.Get_size()

if rank !=0:
    message='Hello from {} '.format(rank)
    comm.send(message,dest=0)

else:
    for procid in range(1, no_of_processes):
        message=comm.recv(source=procid)
        print('Message from process {} : {}'.format(procid, message))