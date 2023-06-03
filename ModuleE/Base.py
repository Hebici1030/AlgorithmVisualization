from PyQt5.QtCore import QObject
import ast

class CustomizeFunction(QObject):
    def __init__(self):
        super(CustomizeFunction, self).__init__()
        self.globals_dict={}
        self.name_fundef = {}

    def GetFunction(self,name:str):
        return self.name_fundef[name]

    def cheakStr(self,expr_str:str):
        try:
            fun_node = ast.parse(expr_str).body[0]
        except SyntaxError:
            return False
        if isinstance(fun_node,ast.FunctionDef):
            return True
        return False
    def Define(self,expr_str:str,name:str):
        func_ast = ast.parse(expr_str,mode='exec')
        func_def = compile(func_ast,filename='blah',mode='exec')
        exec(func_def,self.globals_dict)
        nodeName = None
        for node in ast.walk(func_ast):
            if isinstance(node, ast.FunctionDef):
                nodeName = node.name;
        if (nodeName == None):
            return
        self.name_fundef[name] = nodeName
        return
    def AddFunction(self,expr_str:str,name:str):
        if not self.cheakStr(expr_str):
            return
        self.Define(expr_str,name)

