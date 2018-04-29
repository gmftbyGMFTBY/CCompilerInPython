## Test LR(1) for C

---

```C
// 程序体,全局变量申明和函数列表声明
CMPL_UNIT -> FUNC_LIST | INIT_STMT
  
// 函数列表,包括main函数
FUNC_LIST -> FUNC_DEF FUNC_LIST | @
  
// 函数定义声明
FUNC_DEF -> TYPE_SPEC ID ( ARG_LIST ) CODE_BLOCK

// 类型符号
TYPE_SPEC -> int | void | float | double

// 参数列表
ARG_LIST -> ARGUMENT | ARGUMENT , ARG_LIST | @

// 参数，类型和标识符
ARGUMENT -> TYPE_SPEC ID

// 代码段
CODE_BLOCK -> { STMT_LIST }

// 语句列表
STMT_LIST -> STMT STMT_LIST | @

// 语句: 返回值语句，赋值语句
STMT -> RTN_STMT | ASSIGN_STMT | INIT_STMT | ITER_STMT | IF_STMT
  
// 循环语句，实现 for, while 
ITER_STMT -> for ( EXPR ; EXPR ; EXPR ) CODE_BLOCK | for ( EXPR ; EXPR ; EXPR ) STMT | while ( EXPR ) CODE_BLOCK | while ( EXPR ) STMT
  
// 分支语句, if, if-else
IF_STMT -> if ( EXPR ) CODE_BLOCK | if ( EXPR ) STMT |  if ( EXPR ) CODE_BLOCK else CODE_BLOCK
  
// 函数调用语句
CALL_STMT -> ID ( PARG_LIST )
PARG_LIST -> PARG | PARG , PARG_LIST | @
PARG -> ID

// 返回值语句
RTN_STMT -> return EXPR ; 

// 赋值语句
ASSIGN_STMT -> ID = EXPR ;
  
// 初始化语句
INIT_STMT -> TYPE_SPEC ID ; | TYPE_SPEC ID = EXPR ;

// 表达式
EXPR -> TERM EXPR2
EXPR2 -> + TERM EXPR2 | - TERM EXPR2 | @
TERM -> FACTOR TERM2 
TERM2 -> * FACTOR TERM2 | / FACTOR TERM2 | @

// 标识符，　常量，　子表达式
FACTOR -> ID | CONST | ( EXPR ) | CALL_STMT
```

