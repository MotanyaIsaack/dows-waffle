<h1>MPI Implementation in Python</h1>
<p>A sample application that calculates the area under a curve using the trapezoidal rule given a list of coordinates. It uses processors to calculate partial solutions of the calculations and sent to a single process that sums the partials.</p>

<h1>Pre-requisites</h1>
<li>Local installation of MPI</li>
<li>Local installation of python</li>
<li>Preffered choice of an editor (pycharm, vscode, jupyter notebook)</li>

<h1>Running the solution</h1>
<p>mpiexec -n 6 python -m mpi4py {name of the file} </p>
