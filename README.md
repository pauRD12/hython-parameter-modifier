# hython-parameter-modifier
Python script for modifying parameters of any Houdini scene without launching the application. Execute changes via command line using Hython

- Demo Video: [Linkedin Demo Video](https://www.linkedin.com/posts/pau-rodr%C3%ADguez-dalmau_python-houdini-hython-activity-7193497353876623362-LUxc?utm_source=share&utm_medium=member_desktop)

### Important: 
- Make sure to include the path to where you have Hython installed in the environment variable `PATH`, within the bin folder of the Houdini installation directory (C:\Program Files\Side Effects Software\Houdini 20.0.547\bin).
If you do not know how to do it, you can follow these steps: https://www.imatest.com/docs/editing-system-environment-variables/#Windows

### How to use it:
1. Download the file `parameter_modifier.py`
2. Open CMD and type: `hython "script path" "hip file path"`, where "script path" is the path to the Python file downloaded earlier, and "hip file path" is the path to the Houdini file you want to modify.
3. Follow the instructions displayed on the terminal. You can see it in this example: [Linkedin Demo Video](https://www.linkedin.com/posts/pau-rodr%C3%ADguez-dalmau_python-houdini-hython-activity-7193497353876623362-LUxc?utm_source=share&utm_medium=member_desktop)
