from ModuleD.Base import *

def test_constant_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("1")
    assert isinstance(tf.notations.biggest,ConstantNotation)

def test_constant_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("1")
    assert isinstance(tf.notations.biggest,ConstantNotation)

def test_NlogN_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("NLogN")
    assert isinstance(tf.notations.biggest,NLogNotation)

def test_LogN_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("LogN,K=1")
    assert isinstance(tf.notations.biggest,LogNotation)

def test_Exponent_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("N^2,K=1")
    assert isinstance(tf.notations.biggest,ExponentNotation)

def test_Exponent2_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("N^2,K=0")
    assert isinstance(tf.notations.biggest,ConstantNotation)

def test_Exponent3_time_complexity():
    tf:NotationFactory = NotationFactory()
    tf.addSingleNotation("N^2,K=-1")
    assert tf.notations.biggest == CoreNotation("-",0)

def test_NumberExponent_time_complexity():
    tf: NotationFactory = NotationFactory()
    tf.addSingleNotation("2^N")
    assert isinstance(tf.notations.biggest,NumberExpNotation)

def test_Factorial_time_complexity():
    tf: NotationFactory = NotationFactory()
    tf.addSingleNotation("N!")
    assert isinstance(tf.notations.biggest,FactorialNotation)
