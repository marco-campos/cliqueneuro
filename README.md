# Clique Topology in Neuroscience

## Inspiration
The purpose of this repository is to recreate the results from Chad Giusti's [paper](https://www.pnas.org/doi/abs/10.1073/pnas.1506407112)

## TODO 

### Clique Complex Code
- [x] Optimize the clique generation
	(I ended up writing a recursive function and it executes really fast. 20 vertices takes 1 second.
	The default networkx algorithm took 66 seconds. 30 vertices took 15 seconds so I will probably
	still have to look into some kind of parallelization if I want to get close to 88.)
	- [x] Implement a method which only checks for cliques of up to 6 neighbors.
	- [x] Look for other clique finders online.
	- [x] If still too slow, look into maybe doing this in parallel.
	- [x] Look into generating all the cliques only once for the top filtration
		-[x] Pick out the cliques from the top filtration using current simplices.
- [] Change `g_betti_curve` to generate take in the filtration after the persistence is computed.
	- [] Put the persistence code into the graphing tool function.
- [] Add a function to compute the integral of the betti curve.
	- The betti curves are sums of step functions so this should be easy.
- [] Add the capability to display persistence diagrams
- [] Package up the new gudhi functions
- [] Delete old simplices functions
- [] Add an option to smooth out the betti curves
- [] Build out a user-friendly CliqueComplex Class
	- [] Turn all of these functions into _get functions.
	- [] Turn the betti number related functions into properties.
	- [] Add things like the Euler Characteristic if compatible with Gudhi
- [] Place all of the graphing functions into a utilities folder.

### Geometric Clique Complexes
- [] Re-read Giusti's section on how he generated the *geometric* graphs.
- [] Generate some sampled geometric graphs.
- [] Create some artificial geometric graphs.
- [] Generate geometric graphs with N=88.
- [] Compare the betti curves
- [] Compare the integrated betti curves

### Hippocampus data
- [] Find a data set similar to Giusti's (Look at the Flies or just ask Josic)
- [] Read Giusti's methods for generating the matrix
- [] Generate the Betti curves

