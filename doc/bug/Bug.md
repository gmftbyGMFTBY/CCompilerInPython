## Bug report

---

>兰天		1120151828
>
>徐恒达 		1120151811

1. 关于 Python / C / C++ 报的 `java.lang.IllegalMonitorStateException` 异常

   * 原因

     scan / parser / semantic / intermediate code generate / optimization / code generate / simulate

     对应行数

     131, 151, 171, 191, 211, 231

     判读语句中

     ```java
     if (pp.type.equals("python")) 	// 应该改成对应的scan, parser, ...
     ```

   * 上述的原因所有的 Python 程序进入了 `MiniCCompile.java: run` 函数中运行，并没有进入 `runPy` 函数中运行

   * 在 `run` 函数中, 创建运行时环境等待子进程结束的语句使用抛出异常 `java.lang.IllegalMonitorStateException`

     修改为

     ```java
     p.waitFor();
     ```

2. 关于 Python 的版本的问题

   1. Python 版本使用的 Jython 版本号是 2.6 , 大部分同学使用的是 `Python3` 环境开发

   2. 解决方案

      * 建议删除 `MiniCCompiler.java` 中的 `runPy` 函数，全部采用 `run` 函数在运行时环境中执

        行，并且建议删除 `Jython` 环境

      * 只需要学生在自己电脑上安装最新的 `Python` 环境即可

      * 并且对于 `run` 函数需要针对 `Python` 进行修改

        ```java
        Process p = rt.exec("python " + path + " " + iFile + " " + oFile);
        // 或者在 config.xml 文件中，在 path 字段中写入 python path，前提是Python必须加入用户电脑的环境变量中，Linux 用户只需要对 Python 脚本加上可执行权限即可
        ```