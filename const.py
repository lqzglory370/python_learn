 # -*- coding: UTF-8 -*- 
class _const:                               # 定义常量类_const
    class ConstError(TypeError): pass       # 继承自TypeError
    def __setattr__ (self, name, value):
        if self.__dict__.has_key(name):	    # 如果__dict__中不包含对应的key则抛出错误
            raise self.ConstError, "Can't rebind const(%s)"%name
        self.__dict__[name] = value
import sys
sys.modules[__name__] = _const()            # 将const注册进sys.modules的全局dict中