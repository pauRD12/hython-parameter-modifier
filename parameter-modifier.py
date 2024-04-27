import sys

class ParameterModifier():

        def __init__(self):
            """Initialize dictionaries and variables."""
            self.contexts_tuple, self.parents_tuple = (), ()
            self.nodes_tuple, self.parms_tuple = (), ()
            self.selected_context, self.selected_parent = None, None
            self.selected_node, self.selected_parameter = None, None
            self.hip_file_path = sys.argv[1] # Get the path of the hip file from command line argument

        def load_hip_file(self):
            """"Load a hip file from the chosen path."""
            hou.hipFile.load(self.hip_file_path)

        def list_contexts(self):
            """Generate a tuple containing all the contexts.""" 
            count = 1
            self.contexts_tuple = hou.node("/").children() 
            for context in self.contexts_tuple:
                name = context.name()
                print(f"  {count}. {name}")
                count += 1

        def select_context(self):
            """The user selects the context to enter."""
            i = True  
            while i:
                number = input("\n Enter the number of the context you wish to access:  ") 
                number = int(number)-1
                if number>=0 and number<= len(self.contexts_tuple):
                    self.selected_context = self.contexts_tuple[number]
                    context_name = self.selected_context.name()
                    print(f"\n Yo are inside the'{context_name}' context")
                    i = False
                else:
                    print(" ERROR: Enter a valid number")            

        def list_parents(self):
            """Generate a tuple containing all the nodes inside the selcted context.""" 
            count = 1
            self.parents_tuple = self.selected_context.children() 
            for parent in self.parents_tuple:
                name = parent.name()
                print(f"  {count}. {name}")
                count += 1  

        def select_parent(self):
            """The user selects the node to acces."""
            i = True  
            while i:
                number = input("\n Enter the node number you wish to access: ") 
                number = int(number)-1
                if number>=0 and number<= len(self.contexts_tuple):
                    self.selected_parent = self.parents_tuple[number]
                    i = False
                else:
                    print(" ERROR: Enter a valid number")    

        def list_nodes(self):
            """Generate a list containing all the nodes inside the node we selcted, incuding itself."""       
            count = 1
            self.nodes_tuple = self.selected_parent.allSubChildren() 
            self.nodes_tuple = list(self.nodes_tuple) 
            self.nodes_tuple.insert(0, self.selected_parent)        
            print(f"\n List of all nodes contained in '{self.selected_parent.name()}', including itself first: ")
            for node in self.nodes_tuple:
                path = node.path()
                print(f"  {count}. {path}")
                count += 1

        def select_node(self):
            """The user selects one of the nodes from the list."""
            i = True  
            while i:        
                number = input("\n Enter the number of the node to be selected:  ") 
                number = int(number)-1
                if number>=0 and number<= len(self.nodes_tuple):
                    self.selected_node = self.nodes_tuple[number]
                    i = False
                else:
                    print(" ERROR: Enter a valid number")

        def list_parameters(self):
            """Generate a tuple containing all the parameters from the selected node."""
            count = 1
            self.parms_tuple = self.selected_node.parms()
            print(f"\n List of all parameters inside the node '{self.selected_node.name()}': ")
            for parm in self.parms_tuple:
                name = parm.name()
                print(f"  {count}. {name}")
                count += 1

        def select_parameter(self):
            """The user selects one of the parameters."""
            i = True  
            while i:
                number = input("\n Enter the number of the parameter to be selected:  ") 
                number = int(number)-1
                if number>=0 and number<= len(self.parms_tuple):
                    self.selected_parameter = self.selected_node.parm(self.parms_tuple[number].name())
                    parm_name = self.selected_parameter.name()
                    value = self.selected_parameter.eval()
                    print(f"\n The value of the parameter '{parm_name}' is: {value} ")
                    i = False
                else:
                    print(" ERROR: Enter a valid number")

        def modify_parameter(self):
            """Modify the value of the parameter selected."""
            ask_user = input("\n Do you want to modify the parameter value? (y/n)")    
            if ask_user.lower() == "y":
                new_value = input("\n Enter new value: ")
                self.selected_parameter.set(new_value)
                print(f" '{self.selected_parameter.name()}' set to {new_value}")

        def save_hip_file(self):
            """Save hip file."""
            hou.hipFile.save(self.hip_file_path)

        def run(self):
            """Main method to execute"""
            self.load_hip_file()
            run = True
            while run:
                self.list_contexts()
                self.select_context()
                self.list_parents()
                self.select_parent()
                self.list_nodes()
                self.select_node()
                parm = True
                while parm:
                    self.list_parameters()
                    self.select_parameter()
                    self.modify_parameter()
                    ask_user2 = input(f"\n Do you whis to change another parameter from '{self.selected_node}'? (y/n)")
                    if ask_user2.lower() != "y":
                        parm = False
                ask_user3 = input("\n Do you whis to continue using the progrm? (y/n)")
                if ask_user3.lower() != "y":
                    run = False
            self.save_hip_file()
            print("\n Exit")

x = ParameterModifier()
x.run()