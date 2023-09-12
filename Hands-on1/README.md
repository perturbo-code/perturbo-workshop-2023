# Installation of Perturbo
Installing Perturbo can be complicated due to the fact that it depends on other packages, such as Quantum Espresso, HDF5, LAPACK, etc.
Below we will look at 2 possible scenarios for installing Perturbo - from scratch (on your own) and using Docker.

## Installation of Perturbo from scratch

PERTURBO uses a few subroutines from the PWSCF and Phonon packages of Quantum Espresso (QE). Therefore, it needs to be compiled on top of QE. PERTURBO needs the output files from Wannier 90 (W90), which can ba obtained from the QE. In addition, PERTURBO uses the HDF5 format to store data. For the detailed instructions on the installation of these packages, please refer to their official websites: [QE](https://www.quantum-espresso.org), [HDF5](https://portal.hdfgroup.org/display/HDF5/Introduction+to+HDF5). 
If you run the calculations on a cluster or a supercomputer, these packages might be already pre-installed. Here we provide some brief instructions on the installation of these packages. Please note that these instructions can be different for your computing environement. 

### HDF5

To compile the HDF5 library, please download its source code from the [official website](https://portal.hdfgroup.org/display/support/Downloads). Once the source code is downloaded, please create an empty directory where the HDF5 library will be installed.

For example, the current directory is called _'mylib'_. We download the source code inside the directory called _'hdf5-1.12.0-source-codes'_. Now we are going to install the HDF5 library into a directory called _'hdf5'_. 

Generate a Makefile for compiling the HDF5 library using the fortran option: `--enable-fortran`. Please modify the `'prefix'` path to fit your case. Here we compile the serial HDF5 library: 
 
```bash
cd hdf5-1.12.0-source-codes
./configure --prefix=mylib/hdf5 --enable-fortran 
```

One can specify the compilers running the `./configure` command with the additional options: `CC=<c compiler>`, `CXX=<c++ compiler>`, `FC=<fortran compiler>`. For more information, run `./configure --help`. Compile HDF5:

```bash
make
make install
```

To check whether HDF5 was compiled correctly, one can run the test suite:
```bash
make test
```



Now we have the compiled HDF5 library inside the directory _'hdf5'_. We suggest to use the directory path when compiling QE (`--with-hdf5=mylib/hdf5` flag for QE compilation, see below).  

{% include warning.html content="On some systems, one may need to disable the file locking by executing the following command:

<br/>
`export HDF5_USE_FILE_LOCKING=FALSE`

" %}

### Quantum Espresso

To download QE, one can use the `wget` command:

```
wget https://github.com/QEF/q-e/archive/qe-7.2.tar.gz
tar xvzf qe-7.2.tar.gz
cd q-e-qe-7.2
```

or to clone the package from the QE GitHub repository, specifying the version:

```bash
git clone https://github.com/QEF/q-e.git
cd q-e
git checkout qe-7.2
```

Once the package is downloaded run the configure command: 
```bash
./configure
```
Configuration parameters strongly depend on the compilation scenarios (compilers, parallelization, etc.). On the [PERTURBO github page](https://github.com/perturbo-code/perturbo/tree/master/config) you can find several compilation scripts with corresponding parameters.

When you can compile QE with W90:
```bash
make pw ph pp w90
```

### PERTURBO Download and Installation

Clone the folder with Perturbo code from the [PERTURBO github page](https://github.com/perturbo-code/perturbo/tree/master/) into the QE directory.
There are three subdirectories inside the directory _"perturbo"_:

* _"config"_ contains the system-dependent files _make\_XXX.sys._
* _"pert-src"_ contains the source code of `perturbo.x` to compute electron dynamics 
* _"qe2pert-src"_ contains the source code of the interface program `qe2pert.x`

PERTURBO uses the config file _make.inc_ of QE for most of the compiler options. The configuration files in the _"config"_ folder inside the directory _"perturbo"_ specifies additional options required by Perturbo for different compiler versions and compilation scripts.  

You can take one of the provided make files as a basis, and modify it to suit your case.

Copy your chosen sample to the root folder _"perturbo"_:

```bash
$ cp make_files/make_gcc_serial.sys make.sys
```

and make the necessary changes in it. For example, you need to specify the path to your HDF5 library, if you haven't made it on the step of the QE compilation:

```bash
IFLAGS += -I/path/to/hdf5/include
HDF5_LIBS = -L/path/to/hdf5/lib -lhdf5 -lhdf5_fortran
```

Once the file _make.sys_ has been modified, you are ready to compile PERTURBO:

```bash
make
```

After the compilation, a directory called _'bin'_ is generated, which contains two executables, `perturbo.x` and `qe2pert.x`. You are ready for work with Perturbo!


## Usage of Docker

It is possible to run perturbo faster and easier if you use Docker. This will not be a universal solution, but it will allow you to get acquainted with the functionality of the package, as well as to run programs that are not computationally intensive.

### About Docker
Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. 

To summarize, Docker is essentially a small virtual machine that is configured to use a specific functionality. For example, if we're talking about `perturbo:gcc`, this image (more on that below) consists of:

1. Ubuntu shell
2. The built gcc compiler
3. Some supplementary packages (`vim`, `unzip`, etc.)
3. the HDF5 and Quantum Espresso libraries
4. Perturbo library
Accordingly, by running a container of this image (more on this below) on any computer running [Docker](https://www.docker.com) or its analogs (such as [Podman](https://podman.io)), you will be able to perform calculations using `Perturbo`, avoiding compilation. That's the point of containerization - to create an image ready to use.

### Basic concepts:

1. Image is a "virtual machine" that will be used. It is these images that are hosted on the [docker hub](https://hub.docker.com), where you can find images for many different applications. 
2. Container - is an instance of a "virtual machine" that is created from an existing image. It is in the created container that your work is done.

The relationship between an image and a container is roughly the same as between a class and an instance of the class. 

While a container is simply an instance built from an image, the image itself can be used in different ways. It can be used to create new containers as well as to create new images. For example, the Perturbo image is built in two stages - first, the supplementary [Docker Images](https://hub.docker.com/repository/docker/perturbo/perturbo_suppl/general) (containing all the supplementary libraries). The supplementary images take [`Ubuntu`](https://hub.docker.com/_/ubuntu)images as their base.

3. Volumes - are the preferred mechanism for persisting data generated by and used by Docker containers. The idea is that when each container is created, a corresponding volume is created. By default, such volumes are deleted when the container itself is deleted. This is inconvenient if we need to save some files from the container. Below is how to avoid this.
Visit https://docker-curriculum.com for more information.

### Run the Docker on your computer 
If you want to use builded images on your computer, you will need to follow these steps:
1. Install the [Docker](https://www.docker.com) application on your computer;
2. Clone the Image from the [Docker Hub of the Perturbo](https://hub.docker.com/repository/docker/perturbo/perturbo/general). You can find the command for pulling the images on the tab **Tags**. For example, for GCC case it would be:
	```bash
	docker pull perturbo/perturbo:ifort_mpi
	```
3. Run the following command:
	```bash
	docker run -v name_of_your_work_folder:/home/user/run/name_of_your_work_folder_in_container --user 500 -it -h perturbocker --rm --name perturbo perturbo/perturbo:tag
	```
This command has the following meaning:
1. `-v` - V for ~~Vendetta~~ Volumes, which we talked about earlier. To connect a folder on your primary OS to a folder inside the container, specify the name of the folder on your computer, and after the colon, what the same volume inside the container will be called. In this case, the changes that will happen to the volume inside the container will be reflected in your OS and vice versa. This allows you to not only transfer input files to the container, but also to save all outputfiles after the container is finished and the container itself is deleted;
2. `--user 500` - by default, the container is started via root, which gives a very wide range of possibilities for using the container. Often clusters (`Perlmutter`, for example) forbid this login because of its danger. Therefore, it is recommended to log in via user. This user is preregistered in the container; 
3. `-it` - interactive launch of the container, so that we can go inside and run some calculations there. Without this command, the container would start and close immediately, since no execution is defined in it;
4. `-h perturbocker` - is the hostname of the container. By default, it is the same as the container ID, which may not be particularly informative or readable. So we give it a specific name;
5. `--rm` - deletes the container after its use is finished. Made to save memory. If it is important for you to save the container itself (for example, if you have installed any packages there), this option should be removed, and the container should be started using `docker start` in the future. [Docs](https://docs.docker.com/engine/reference/commandline/start/);
6. `--name` - the name that the container will receive. During run (and, if the container is not deleted, during storage) it can be referred to by this name. 

Full list of the command line options is provided on the [offical page](https://docs.docker.com/engine/reference/commandline/run/)

You need to change two parameters:

1. The names of your volumes and volume in the container
2. The name of the image itself - instead of `tag` specify the tag of the image you want to use as a basis for creating the container.

Now you are ready for the usage of Perturbo in the Docker!
