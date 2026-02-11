# MODFLOW 6 and Python workflows for developing MODFLOW models
MODFLOW is a three-dimensional hydrologic simulator that is developed and maintained by the U.S. Geological Survey and cooperating partners. MODFLOW 6 is the current “core” version of MODFLOW that is actively supported, developed, and maintained by the USGS. Newly developed capabilities extend MODFLOW from a groundwater flow simulator into a hydrologic simulator with many features not available in prior versions. FloPy is a python scripting language package for MODFLOW that can be used to build, edit, postprocess, and visualize MODFLOW simulations.  

The purpose of this course is to provide a high-level overview of MODFLOW 6 and FloPy coupled with in-depth activities. Participants will learn how to construct, edit, and post-process models in a Python environment with FloPy. The course schedule is as follows:

## Instructors: 
Josh Larsen, U.S. Geological Survey, California Water Science Center  
Eric Morway, U.S. Geological Survey, Nevada Water Science Center 

## Class Schedule:
*Thursday, June 25th*
|Time      |Topic                                                                          |Duration, Lead                    |
|----------|-------------------------------------------------------------------------------|----------------------------------|
|8:30 AM   |Introductions & Class Overview                                                 |30 minutes                        |
|9:00 AM   |Overview of the groundwater flow equation and MODFLOW CVFD methods             |1 hour 30 minutes                 |
|10:30 AM  |Break                                                                          |15 minutes                        |
|10:45 AM  |Overview of MODFLOW input and output                                           |30 minutes                        |
|11:15 AM  |Constructing a first MODFLOW model by hand (Part 1)                            |45 minutes                        |
|12:00 PM  |Lunch                                                                          |1 hour                            |
|1:00 PM   |Constructing a first MODFLOW model by hand (Part 2)                            |30 minutes                        |
|1:30 PM   |Python overview and refresher (Jupyter, Python Basics, Pandas, Geopandas)      |1 hour                            |
|2:30 PM   |Break                                                                          |15 minutes                        |
|2:45 PM   |Intro to FloPy and constructing a first MODFLOW model in Python                |1 hour                            |
|3:45 PM   |Discretization workflows for constructing Structured and Unstructured Grids    |45 minutes (part 1)               |

   - Discretization strategies and workflows for Stuctured and Unstructured Grids (2:45 - 4:00 PM)
   - Strategies for translating geospatial and temporally varying data into model boundary conditions (Part 1; 4:00 - 4:30PM)

*Friday, June 26th*
   - Strategies for translating geospatial and temporally varying data into model boundary conditions (Part 2; 8:30 - 9:30AM)
   - MODFLOW output post-processing and analysis, Zonebudget (9:30 - 10:30 AM)
   - Putting it all together- Class Project: building a model in Python from disparate data (10:30 - 12:00 PM)  *todo: need to construct or select a model to do this with*
   - Lunch (12:00 - 1:00 PM)
   - Putting it all together- Class Project: building a model in Python from disparate data (1:00 - 2:00 PM)
   - Advanced topics as time allows; topics selected based on class interest (2:00 - 4:30 PM):
        - Stream capture scenarios 
        - Speeding up slow models with Parallel MODFLOW
        - Custom model boundary conditions and behavior using the MODFLOW API
        - Particle tracking
        - Heat transport
        - Solute transport

## Required software and installation:

### Software Installation
The following instructions will guide you through the installation process and setup a conda environment for the class

#### 1. Install Miniforge
   - Go to the miniforge website and download the installer [(https://github.com/conda-forge/miniforge)](https://github.com/conda-forge/miniforge) for your platform. If you have trouble downloading Miniforge in Microsoft Edge try another browser (e.g., Chrome)
   - Run the installer program that you downloaded. On Windows the installer is called `Miniforge3-Windows-x86_64.exe`
   - Click through the installer options, and **select "Just Me (recommended)"** if asked. Default installation options should be fine, with the exception that you should select and installation location that does not have any special characters or spaces and that the install location is not on cloud storage (e.g., One Drive == BAD!)
   - After installation, you should see "Miniforge prompt" as a program under the Windows start menu

#### 2. Create an environment file
We will use an environment file to create a containerized version of Python and the Python packages needed for the class. An environment file is simply a list of packages that we want to install in our environment

   - Using a text editor, such as Notepad or Notepad++, create a file called environment.yml. It should contain the information in [this environment file](https://github.com/jlarsen-usgs/CWEMF-modflow-flopy-2026/blob/main/environment.yml). Save this file to your hard drive, preferably in your user home folder so that it can be easily accessed in the next step. (Caution! Notepad will automatically append a .txt suffix to your file name; you don't want this to happen.)

     Alternatively, clone this repository and use `environment.yml` directly

   - **For MacOS and Linux users only!** You will need to add additional dependencies to the `environment.yml` file from step 1. The following dependencies are also required:
     
     **MacOS**
     ```
     - pkg-config
     - openmpi<5.0.0
     - gfortran
     - petsc
     - netcdf-fortran
     - meson>=1.1.0
     - ninja
     ```

     **Linux**
     ```
     - pkg-config
     - openmpi
     - gfortran
     - petsc
     - netcdf-fortran
     - meson>=1.1.0
     - ninja
     ```

#### 3. Create the `cwemf-modflow` environment
   - Start the miniforge prompt from the Windows start menu (or equivalent on MacOS or Linux) to bring up a terminal.
   - At the terminal prompt enter the following command, where <path to file> is the location of the environment.yml file that you created in Part 2. You will need to be connected to the internet for this to work properly. The installation process may take a couple of minutes.
     ```
     mamba env create --file <path to file>/environment.yml
     ```
   - After the environment has been installed, you may activate this new class environment with the following command
     ```
     mamba activate cwemf-modflow
     ```
   - The windows terminal prompt should reflect the current environment
     ```
     (cwemf-modflow) C:\Users\JaneDoe>
     ```
   - We will be using jupyter notebooks in the class. To test if jupyter is installed and working properly use the following command. After entering this command, the default web browswer should open to a Jupyter Lab page.
     ```
     jupyter lab
     ```
The setup should be complete at this point. 
     
     


     
