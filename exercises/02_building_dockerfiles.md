# Exercises on building Dockerfiles

This set of exercises aim to get you familiar with how a Dockerfile can be build. 

We start from a Dockerfile which has been prepared upfront and will add some statements iteratively to  create a valid Dockerfile for the tool methplotlib developed at VIB UAntwerp by Wouter De Coster.

Please have look at the folder `docker` and open the file `Dockerfile.methplotlib.start`.

In this example, we will start from a parent image from `Biocontainer.pro`. 

Try to find the Dockerfile of this parent image via an internet search.

https://github.com/BioContainers/containers/blob/master/biocontainers/debian-buster-backports/Dockerfile

What the user which is used in the image when tools are run?
What mount points (volumes) are present?

Let's go back to the current Dockerfile and try to create Docker recipe for the tool `methplotlib`.

Go to the github repository of tool [methplotlib](https://bio.tools/methplotlib).

Based on the explanation how to install `methplotlib` formulate a statement for this Dockerfile to install the tool and build the Docker image by adding a version tag to the build name.

Does the build pass successfully?

Formulate an additional statement to address the error message.

Rebuild the Docker image. 

Run the image with your user and group id, mount the local `data` folder to the internal `data`folder using the working directory `/data` on the example data described in the github repository of methplotlib.

Have a look at the Dockerfile and what additional statements are present for annotation of the Docker image as well as build and example usage.

As an additional example, we would like to create a Docker image using a conda environment for methplotlib.

Again, a skeleton of the Dockerfile is present `Dockerfile.methplotlib.conda`.

Add a statement for the installation of the tool. Check on latest version of methplotlib. 
The following commands will be useful:

- conda create --name methplotlib
- conda config --add channels bioconda
- conda install --name methplotlib methplotlib=X.XX.X
- conda config --add channels conda-forge

Try to build the Docker image and run `methplotlib -v`.

With what Docker statement could you add the PATH `PATH=/usr/miniconda3/envs/methplotlib/bin/:$PATH`?

Add annotations as well as build instructions for the alternative Docker image.

Lastly, a `Dockerfile` has been provided which contains correct statements but the order is shuffled around which makes the file unusable as it is.
Put the statements in the correct order and build the Docker image with the very simple environment for RNA-seq pre-processing steps.
Please add also a correct example usage to check whether the fastqc tool in the containers runs correcty.

