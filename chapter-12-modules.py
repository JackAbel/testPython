#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import nested_scopes
import sys
from Tkinter import (Tk, Frame, Button, Entry)
print sys.path
sys.path.append('/home/py/lib')
print sys.modules   # 可以找到当前导入了那些模块和他们的文件位置
# 模块导入顺序·标准库 第三方 自定义    三种模块中间空一行
# 模块在函数中导入时，作用域是局部的
# 标准模块多行导入方式 许多属性用()
# 使用as关键字命名导入的模块或属性 # 导入__future__不会有任何改变
sys = __import__('sys')
# 避免导入循环



