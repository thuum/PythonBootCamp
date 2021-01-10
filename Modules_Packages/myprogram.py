# We can import other python script by just using the following syntax. In this case "mymodule" is the name of the .py script
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_sub_script

some_main_script.report_main()
my_sub_script.sub_report()

# We can organize module into packages by creating a folder containing all modules for that package and adding a "__init__.py" file to that folder.
# This way we can 