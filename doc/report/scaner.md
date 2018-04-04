## 词法分析器实验报告

---

### 1. 实验目的和内容

1. 阅读 BITMinicCompiler 框架的代码结构，为本次试验和之后的实验打下良好的基础
2. 根据提供的 C 语言的标准设计相应的 5 大类分类对应的 DFA (包括出错处理的 DFA)
3. 使用数据中心法实现设计的 DFA ，并完成总控程序的算法的编写，完整实现整个词法分析器
4. 编写相应的测试文件
   * 正确案例测试文件 - 测试设计的 DFA 的有效性
   * 错误案例测试文件 - 测试设计的 DFA 的容错性能和错误识别能力
5. 在测试文件上多次运行词法分析器并完善代码的结构和功能

### 2. 实验环境和配置信息

1. 宿主机环境

   * Ubuntu 16.04
   * openjdk-1.8 / jre 1.8
   * Python 3.6 - 宿主语言

2. 运行环境配置

   ```shell
   #!/bin/bash

   java -jar BITMiniCC.jar test.c	# test.c 为测试文件
   ```

### 3. 实验的具体过程和步骤

1. 框架代码阅读

   实验使用 Python 语言进行编写，因此对 Python 提供的接口进行了相关的研读

   * 框架的主入口文件 - BITMiniCC.java

     创建 MiniCCompiler 对象执行运行函数 (run)

   * 运行函数文件 - MinCCompiler.java

     1. readConfig

        读取 config.xml 文件并解析生成对应的接口文件(输入文件，输出文件标准格式和文件名)

     2. runPy

        根据 config.xml 文件中的配置，执行对应的 Python 脚本生成输出的 XML 文件(属性字流)

2. DFA 设计

   1. 常数类型

      * 常数类型包含 - 整型常数，实型常数，8进制常数，16进制常数，字符，字符串等等类型

      * C11标准定义文法(子集实现)

        ```c
        # 整形常量
        In		->		Dec | Oct | Hex
        Dec		->		nd | Dec+d
        Oct		->		0 | Oct+od
        Hex		->		Hex-pre+hd | Hex+hd
        hd		->		0x | 0X
        nd		->		1|2|3|4|5|6|7|8|9
        od		->		0|1|2|3|4|5|6|7
        hd		->		0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|A|B|C|D|E|F
          
        # 字符常量
        c-char-sequence	->	c-char | c-char-sequence+c-char
        c-char			->	除了 ', \, \n 之外的任何字符 | 转义字符

        # 字符串常量
        string-literal:	-> 	s-char-sequence
        s-char-sequence -> 	s-char | s-char-sequence+s-char
        s-char			->	除了 ", \, \n 之外的任何字符 | 转义字符
        ```

      * 设计图

        ​    ![](./photo/constant.png)

   2. 标识符 / 关键字类型

      * 标识符包含各类名字的表示，比如变量名，数组名，函数名，文件名

        因为标识符和关键字的内聚性比较强，所以在词法分析器的具体实现中，我采用了将标识符和关键字混合分类判断的方式:

        __对每一个识别出来的标识符进行二次加工处理，判断是否是关键字，从而对这两种类型在词法分析的阶段中进行区分__

      * C11标准定义文法(子集实现)

        ```c
        ID		->	ID-nd | ID+ID-nd | ID+d
        ID-nd	->	nd
        nd		->	_|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w| 	 x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
        d		->	0|1|2|3|4|5|6|7|8|9
        ```

      * 设计图

        ![](./photo/identifier.png)

   3. 运算符

      * 表示程序中的算数运算，逻辑运算，字符，串操作等运算的确定字符(串)

      * C11

        ```c
        [], (), ->, .
        !, -, ++, --, &, *, +, -, ~
        /, %, <<, >>, <, >, <=, >=, ==, !=, ^, |, &&, ||
        ?, :, ;, ...
        =, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=
        ,, #, ##
        ```

   4. 分隔符

      * 逗号，分号，括号，单引号，双引号等等

      * C11

        ```c
        ,, ;, {, }
        ```

      * 设计图

        ![](./photo/separate.png)

3. 实现词法分析器

   1. 数据中心法

      * 主表: 记录状态和对应的状态对应的处理函数或者分表入口

        1. 如果是终态，对应的主表项是函数对象(Python)
        2. 如果是中间状态，对应的主表项是分表

      * 分表: 记录从当前的状态经过字符转换到的状态的映射关系

      * 实现方式

        1. 使用 Python 中的 defultdict 对象

           ```python
           from collections import defaultdict
           # 主表
           main_table = defaultdict(dict)

           # 分表
           table	   = defaultdict(list)
           ```

        2. 对于分表中的字符状态检测采用 re 包的正则表达式实现，有助于程序的可扩展性和修改的便捷性

        3. 非法状态的检测

           根据当前的状态选择分表入口之后，如果对分表项中的所有正则表达式都不能有效的识别的话，程序认为即将进入非法状态，并在之后的状态返回中对 valid 属性进行相应的填充

      * 实现细节

        1. 为 5 个分类创建了 5 个函数对象以及一个错误状态处理函数对象，作为对终态的处理方式加入到 defaultdict 中

           ```python
           def solve_separate(string, state):
               return [string, "separate", True]

           def solve_constant(string, state):
               # 内部还会检测识别的数字是否是合法的，比如 018 的错误
               if wrong:
                   return [string, "constant", False]
               return [string, 'constant', True]

           def solve_identifier(string, state):
               # 内部使用 keyword 列表对识别的 identifier 
               # 进行关键字的识别，如果满足关键字的条件则为关键字类别
               # 否则是朴素的 identifier 标识符名称
               if string in keyword:
                   return [string, "keyword", True]
               else
                   return [string, "identifier", True]

           def solve_operator(string, state):
               return [string, "operator", True]

           def solve_wrong(string, state):
               return [string, "WRONG", False]
           ```

        2. 分表中的键是对读入字符的描述的**正则表达式**

           示例如图，下图是对 0 号状态的分表的构建

           ![](./photo/分表.png)

        3. 主表中的终态，使用对应的终态状态作为键，使用带有参数的函数列表作为值

           ![](./photo/1.png)

   2. 总控算法

      1. 流程图

         ![](./photo/主控算法.png)

      2. ​

### 4. 运行效果截图

### 5. 实验心得体会