# CSC_581_ASE


Objective :
	The objective of the testcase is to implement math utility functions using python to test the script. We used Jenkins to automate the pipeline using python scripts.

Python :
	Created a math_utils.py python script to test the math utilities like addition, subtraction, multiplication and division.

	Then we created test_math_utils.py python script which is to test the mathematical operations.

Jenkins Pipeline:
	Downloaded the Jenkins framework to automate the python test cases from the git repository.
	Build the pipeline to compile the python test cases to execute when the changes made in the github repository and create a XML file for status in the repository.
	Pipeline script can be found in the Jenkins repository.
	It will automate the build whenever the commit made in github repository.

Screenshot of my Built:

 ![image](https://github.com/AkilanP1726/CSC_581_ASE/assets/158797742/79966d6d-4696-42ee-abbf-4e72da315e15)

Pipeline overview:

<img width="617" alt="image" src="https://github.com/AkilanP1726/CSC_581_ASE/assets/158797742/c2870eb2-21f6-48ce-810d-636baa0ba4d9">


 
Console Output:

Started by user Akilan Pandiyan
Obtained Jenkinsfile from git https://github.com/AkilanP1726/CSC_581_ASE.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in C:\ProgramData\Jenkins\.jenkins\workspace\python-with-jenkins
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git.exe rev-parse --resolve-git-dir C:\ProgramData\Jenkins\.jenkins\workspace\python-with-jenkins\.git # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/AkilanP1726/CSC_581_ASE.git # timeout=10
Fetching upstream changes from https://github.com/AkilanP1726/CSC_581_ASE.git
 > git.exe --version # timeout=10
 > git --version # 'git version 2.43.0.windows.1'
 > git.exe fetch --tags --force --progress -- https://github.com/AkilanP1726/CSC_581_ASE.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision a710e797aee9778e01604c88ee5caf2f7efc2d26 (refs/remotes/origin/master)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f a710e797aee9778e01604c88ee5caf2f7efc2d26 # timeout=10
Commit message: "Update Jenkinsfile with filename"
 > git.exe rev-list --no-walk b99c9aa6a3d8a3e9694403fee9dcf87232ca8339 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (build)
[Pipeline] bat

C:\ProgramData\Jenkins\.jenkins\workspace\python-with-jenkins>python -m py_compile math_utils.py 
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)
[Pipeline] bat

C:\ProgramData\Jenkins\.jenkins\workspace\python-with-jenkins>python -m pytest --junit-xml test-reports/results.xml test_math_utils.py 
============================= test session starts =============================
platform win32 -- Python 3.12.1, pytest-8.0.0, pluggy-1.4.0
rootdir: C:\ProgramData\Jenkins\.jenkins\workspace\python-with-jenkins
collected 5 items

test_math_utils.py .....                                                 [100%]

- generated xml file: C:\ProgramData\Jenkins\.jenkins\workspace\python-with-jenkins\test-reports\results.xml -
============================== 5 passed in 0.14s ==============================
Post stage
[Pipeline] junit
Recording test results
[Checks API] No suitable checks publisher found.
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
