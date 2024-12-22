# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

import pandas as pd

FirstData = pd.DataFrame({
    'EmpId': [100, 200, 300],
    'EmpName': ['Venkat', 'Ramesh', 'Suresh']
})

SecondData = pd.DataFrame({
    'EmpId': [300, 400, 500],
    'EmpName': ['Suresh', 'Koti', 'Pavani']
})

FinalResult = pd.concat([FirstData, SecondData])  

FinalResult = FinalResult.reset_index(drop=True) 
display(FinalResult)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

FinalResult = FinalResult.drop_duplicates()
display(FinalResult)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

EmpSalary = 343
FinalOutput = "Currently I am working so my salary will be :  " + EmpSalary

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

EmpSalary = 343
FinalOutput = f"Currently I am working so my salary will be : {EmpSalary} "
print(FinalOutput)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

EmpName = 'Venkat'
FinalResult = f"My Name is {EmpName} so I am working on MS Fabric"
print(FinalResult)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
