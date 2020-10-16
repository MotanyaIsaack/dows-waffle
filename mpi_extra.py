from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
number_of_processors = comm.Get_size()
xmin = 0
xmax = 10
n = 5
y = [4, 6, 6, 4, 4, 5]
y1 = [4, 6, 6]
y2 = [6, 4, 4]
y3 = [4, 5]
total_area = 0


def trapezoidal_rule(y):
    change_in_x = ((xmax - xmin) / n)
    size_of_y = len(y)
    result = 0
    for i in range(size_of_y):
        if i != 0 and i != size_of_y - 1:
            result = result + 2 * y[i]
        else:
            result = result + y[i]
    result = result * (change_in_x / 2)
    return result


if rank != 0:
    if rank == 1:
        message = trapezoidal_rule(y1)
        comm.send(message, dest=0)
    elif rank == 2:
        message = trapezoidal_rule(y2)
        comm.send(message, dest=0)
    elif rank == 3:
        message = trapezoidal_rule(y3)
        comm.send(message, dest=0)
    print("Hello from:" + str(rank))
else:
    for procid in range(1, number_of_processors):
        message = comm.recv(source=procid)
        total_area += message
        print('Calculated area from process {} is : {}'.format(procid, message))

    if total_area > 0:
        print('Total trapezium area is : {}'.format(total_area))
        print(message)
