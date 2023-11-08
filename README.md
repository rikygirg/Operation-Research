# Operation-Research
**Algorithms and methods for linear programming**

This repo contains some Python code for basic linear programming techniques, such as solution of optimization problems using the Simplex method. 

The project is far from complete, many things are still missing for the code to be actually useful in any context, other than college-level exercises. In the `main.py` file you'll find a list of the features that still need to be introduced, which I'll briefly report here:

 - Not sure the program works where no admissible basis can be found. Implement Phase I simplex
- The algo does not manage the case of an illimitate
problem. Add limitation clause in the `j = argmin` section
- Test the script for performance in terms of execution
time and memomary management, I bet there's still a lot of room for improvement. Develop an actual benchmark, not the one currently implemented
- Adapt the optimum outcome to the actual scope, wether a maximization or minimization
- Implement other methods to solve a linear programming
problem.

If you wish to contribute to this project, feel free to contact me on my [LinkedIn](https://www.linkedin.com/in/matteo-campagnoli-3a515b1bb/). 
