# NFL Play by Play Win Prediction SSE for Qlik

![Sheet 1](https://s3.amazonaws.com/dpi-sse/dpi-python-sse-play-predictions-nfl/Dash1.png)

![Sheet 2](https://s3.amazonaws.com/dpi-sse/dpi-python-sse-play-predictions-nfl/Dash2.png)

![Sheet 3](https://s3.amazonaws.com/dpi-sse/dpi-python-sse-play-predictions-nfl/Dash3.png)

## REQUIREMENTS

- **Assuming prerequisite: [Python with Qlik Sense AAI – Environment Setup](https://s3.amazonaws.com/dpi-sse/DPI+-+Qlik+Sense+AAI+and+Python+Environment+Setup.pdf)**
	- This is not mandatory and is intended for those who are not as familiar with Python to setup a virtual environment. Feel free to follow the below instructions flexibly if you have experience.
- Qlik Sense June 2018+
- *Note: this may be used with QlikView as of November 2017+.
    - *See how to setup Analytic Connections within QlikView [here](https://help.qlik.com/en-US/qlikview/November2017/Subsystems/Client/Content/Analytic_connections.htm)*
- Python 3.5.3 64 bit
- Python Libraries: grpcio, pandas, sckkit-learn==0.17, nflwin, preprocessing
- *Including data originally taken from [ryurko/nflscrapR-data](https://github.com/ryurko/nflscrapR-data/tree/master/data) and then massaged to fit the NFLWin models*

## LAYOUT

- [Prepare your Project Directory](#prepare-your-project-directory)
- [Install Python Libraries and Required Software](#install-python-libraries-and-required-software)
- [Setup an AAI Connection in the QMC](#setup-an-aai-connection-in-the-qmc)
- [Copy the Package Contents and Import Examples](#copy-the-package-contents-and-import-examples)
- [Prepare And Start Services](#prepare-and-start-services)
- [Leverage Play by Play Predictions from within Qlik Sense](#leverage-play-by-play-predictions-from-within-qlik-sense)
- [Configure your SSE as a Windows Service](#configure-your-sse-as-a-windows-service)

 
## PREPARE YOUR PROJECT DIRECTORY
>### <span style="color:red">ALERT</span>
><span style="color:red">
>Virtual environments are not necessary, but are frequently considered a best practice when handling multiple Python projects.
></span>

1. Open a command prompt
2. Make a new project folder called QlikSenseAAI, where all of our projects will live that leverage the QlikSenseAAI virtual environment that we’ve created. Let’s place it under ‘C:\Users\\{Your Username}’. If you have already created this folder in another guide, simply skip this step.
3. We now want to leverage our virtual environment. If you are not already in your environment, enter it by executing:

```shell
$ workon QlikSenseAAI
```

4. Now, ensuring you are in the ‘QlikSenseAAI’ folder that you created (if you have followed another guide, it might redirect you to a prior working directory if you've set a default, execute the following commands to create and navigate into your project’s folder structure:
```
$ cd QlikSenseAAI
$ mkdir NFL
$ cd NFL
```


5. Optionally, you can bind the current working directory as the virtual environment’s default. Execute (Note the period!):
```shell
$ setprojectdir .
```
6. We have now set the stage for our environment. To navigate back into this project in the future, simply execute:
```shell
$ workon QlikSenseAAI
```

This will take you back into the environment with the default directory that we set above. To change the
directory for future projects within the same environment, change your directory to the desired path and reset
the working directory with ‘setprojectdir .’


## INSTALL PYTHON LIBRARIES AND REQUIRED SOFTWARE

1. Open a command prompt or continue in your current command prompt, ensuring that you are currently within the virtual environment—you will see (QlikSenseAAI) preceding the directory if so. If you are not, execute:
```shell
$ workon QlikSenseAAI
```
2. Execute the following commands. If you have followed a previous guide, you have more than likely already installed grpcio):

```shell
$ pip install grpcio
$ pip install pandas
$ pip install scikit-learn==0.17
$ pip install nflwin
$ pip install preprocessing
```

## SET UP AN AAI CONNECTION IN THE QMC

1. Navigate to the QMC and select ‘Analytic connections’
2. Fill in the **Name**, **Host**, and **Port** parameters -- these are mandatory.
    - **Name** is the alias for the analytic connection. For the example qvf to work without modifications, name it 'NFL'
    - **Host** is the location of where the service is running. If you installed this locally, you can use 'localhost'
    - **Port** is the target port in which the service is running. This module is setup to run on 50099, however that can be easily modified by searching for ‘-port’ in the ‘\_\_main\_\_.py’ file and changing the ‘default’ parameter to an available port.
3. Click ‘Apply’, and you’ve now created a new analytics connection.


## COPY THE PACKAGE CONTENTS AND IMPORT EXAMPLES

1. Now we want to setup our service and app. Let’s start by copying over the contents of the example
    from this package (from NFLWin-SSE) to the ‘..\QlikSenseAAI\NFL\’ location.
2. Since NFLWin is built for Python 2.x and Qlik requires Python 3.4+, I've modified the sections of the NFLWin package's code needed to run this SSE so that it can run in 3.5+ (tested on 3.5.3). In the content, you will see a folder named NFLWin-ModifiedPackage. Navigate to your virtualenv location (or your Python location if not using virtualenv) and find the NFLWin package. If you've followed this guide using the virtualenv, the file path should resemble 'C:\\{YourUserName}\\Envs\\QlikSenseAAI\\Libs\\site-packages\\nflwin\\'. Replace all of the files in this directory with the files from NFLWin-ModifiedPackage.
3. After copying over the contents, go ahead and import the example qvf found [here](https://s3.amazonaws.com/dpi-sse/dpi-python-sse-play-predictions-nfl/Football+-+AAI.qvf).
4. Lastly, download and import the extensions needed for the demo app:
	1.  [Sense-navigation](https://github.com/stefanwalther/sense-navigation) 
	2.  [Black Background Theme](https://s3.amazonaws.com/dpi-sse/dpi-python-sse-play-predictions-nfl/BlackBackground.zip) *optional, requires Qlik Sense February 2018+*
5. _Optionally, if you wanted to create your own models, I've included my script to do so in the NFLWin-CreateModels folder. Note that this needs to be executed in a Python 2.x environment (tested on 2.7)._


## PREPARE AND START SERVICES

1. At this point the setup is complete, and we now need to start the extension service. To do so, navigate back to the command prompt. Please make sure that you are inside of the virtual environment.
2. Once at the command prompt and within your environment, execute (note two underscores on each side):
```shell
$ python __main__.py
```
3. We now need to restart the Qlik Sense engine service so that it can register the new AAI service. To do so,
    navigate to windows Services and restart the ‘Qlik Sense Engine Service’
4. You should now see in the command prompt that the Qlik Sense Engine has registered the function _PredictPlayByPlay_ from the extension service over port 50099, or whichever port you’ve chosen to leverage.


## LEVERAGE PLAY BY PLAY PREDICTIONS FROM WITHIN SENSE

1. The *PredictPlayByPlay()* function leverages a modified version (to run on Python 3.x) of the [NFLWin](http://nflwin.readthedocs.io/en/stable/) package and accepts twelve mandatory arguments:
    - *ModelFileName (string)*: i.e. '2009model.pkl'
    - *GameID (string) (this is ignored in the model)*
    - *Quarter (string) - The quarter, prepended with “Q” (e.g. `Q1` means the first quarter). Overtime periods are denoted as `OT`, `OT2`, and theoretically `OT3` if one were to ever be played.*
    - *QuarterSecondsElapsed (string) - seconds elapsed since the start of the quarter.*
    - *OffensiveTeam (string) - The abbreviation of the team currently with possession of the ball.*
    - *Yardline (string) - The current field position. Goes from -49 to 49, where negative numbers indicate that the team with possession is on its own side of the field.*
    - *Down (string) - The down. kickoffs, extra points, and similar have a down of 0.*
    - *YardsToGo (string) - How many yards needed in order to get a first down (or touchdown).*
    - *HomeTeam (string) - The abbreviation of the home team.*
    - *AwayTeam (string) - The abbreviation of the away team.*
    - *HomeTeamCurrentScore (string) - The home team’s score at the start of the play.*
    - *AwayTeamCurrentScore (string) - The away team’s score at the start of the play.*
2. Example function calls:
	
    ```  
    NFL.PredictPlayByPlay(	'2009model.pkl',
						    '2017102906',
						    'Q2',
						    '0',
						    'NYJ',
						    '20',
						    '3',
						    '2',
						    'NYJ',
						    'NE',
						    '0',
						    '7'
	)
    
    ``` 
    


## CONFIGURE YOUR SSE AS A WINDOWS SERVICE

Using NSSM is my personal favorite way to turn a Python SSE into a Windows Service. You will want to run your SSEs as services so that they startup automatically and run in the background.
1. The **Path** needs to be the location of your desired Python executable. If you've followed my guide and are using a virtual environment, you can find that under 'C:\Users\\{USERNAME}\Envs\QlikSenseAAI\Scripts\python.exe'.
2. the **Startup directory** needs to be the parent folder of the extension service. Depending on what guide you are following, the folder needs to contain the '_\_main\_\_.py' file or the 
'ExtensionService_{yourservicename).py' file.
3. The **Arguments** parameter is then just the name of the file that you want Python to run. Again, depending on the guide, that will either be the '\_\_main\_\_.py' file or the 'ExtensionService_{yourservicename).py' file.

**Example:**

![ServiceExample](https://s3.amazonaws.com/dpi-sse/PythonAsAService.png)