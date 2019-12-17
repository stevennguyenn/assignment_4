import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(10)])]))])
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_int_ast_int_add(self):
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(2))])]))])
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_int_ast_int_minus(self):
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putInt"),[BinaryOp("-",IntLiteral(2),IntLiteral(2))])]))])
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_ast_int_mul(self):
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putInt"),[BinaryOp("*",IntLiteral(2),IntLiteral(2))])]))])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_int_ast_int_div(self):
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putFloat"),[BinaryOp("/",IntLiteral(5),IntLiteral(2))])]))])
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_int_ast_int_greater_than(self):
    #     input = Program([
    #             FuncDecl(Id("main"),[],VoidType(),Block([
    #                 CallExpr(Id("putBool"),[BinaryOp(">",IntLiteral(3),IntLiteral(2))])]))])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

