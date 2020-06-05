# finder

Web application using Python 3.8, Flask 1.1, HTML5 and Boostrap 4.4

Description: this application serves as a simple modern contact book, where you can create an account and upload your contact
information such as address, email, phone number, social media, website etc, so that other people can look you up.
Or you can simply search for contacts (you don't need an account for that).

Version control system used: Git

Environment variables you need to set:
SECRET_KEY
DATABASE_URI
Note: we use a particular Anaconda workflow to set/unset the values of these variables whenever our virtual environment is
activated/deactivated, so as not to conflict with variables of the same name needed for other projects or OS-wide. And while 
we do reccommend that, you can still follow along just fine setting environment variables the traditional way.

Dependencies: for managing virtual environments and third party packages, we have used Anaconda. If you do have Anaconda
installed, and you have cloned the repo locally, follow these steps to install the dependencies:
(Note: file names and commands are wrapped with single quotation marks)
-cd to the local repo root directory
-hit 'ls' and verify that you have a file called 'environment.yaml'
-hit 'conda create --f environment.yaml --name pick_a_name' to create the virtual environment
-hit 'conda activate your_env_name' to activate the virtual environment
-while the environment is activated, hit 'conda list' to verify the dependencies have been indeed installed
-if you still aren't sure, compare the output of the command above, to the contents of environment.yaml

It's best to always keep that virtual environment activated while are working on this project, to avoid mixing up
dependencies among different projects of yours or the base python installation(s). 
To deactivate the environment, hit 'conda deactivate'. Refer to Anaconda docs for more information.

Note: If you install new packages or remove/update existing ones, you are merely updating the conda environment, which resides
outside your local repo root directory, and the changes are therefore not tracked by source control.
If you would like to push those changes remotely (which you should), follow these steps:
-hit 'conda env export > environment.yaml' while in project's top level dir, to reflect the changes to the environment file
-open 'environment.yaml' and verify that its contents have indeed been updated
-don't forget to include 'environment.yaml' in the coming commit

If another contributor has gone through the above mentioned process, and you pulled the changes in, then your anaconda environment is 
likely not up to date, and the project may not even run anymore due to missing dependencies.
You can view the new contents of 'environment.yaml' and manually update your environment to match those exact dependencies, but a 
more practical way is to update the environment with the following steps:
-hit 'conda deactivate' to deactivate the environment, as it can sometimes lead to problems if it's activated
-hit 'conda env update -f environment.yaml --prune' to update the environment based on a file with the latest dependencies
-hit 'conda activate' to go back to working
Read the Anaconda docs for more.

If you don't have Anaconda installed and/or would rather use other tools (venv, virtualenv etc) to manage virtual 
environments, it's up to you to recreate a similar environment based on the 'environment.yaml' file.

