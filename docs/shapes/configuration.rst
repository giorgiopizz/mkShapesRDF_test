
A configuration folder for shapeAnalysis
============================================

The ``configuration.py`` file
-----------------------------

It's the only necessary python file, it has to include the following variables

- tag
- runnerFile
- ouputFile
- outputFolder
- batchFolder
- configFolder

- imports
- filesToExec
- varsToKeep
- batchVars

- lumi

and when running the plotter the required variables are

- plotPath
- minRatio
- maxRatio


All the other python files to be executed have to be included in the `filesToExec` list. While the variables defined that have to be digested by runner have to be provided in `varsToKeep`
