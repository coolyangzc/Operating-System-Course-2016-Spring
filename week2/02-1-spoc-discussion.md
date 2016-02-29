#lec 3 SPOC Discussion

## 第三讲 启动、中断、异常和系统调用-思考题

## 3.1 BIOS
 1. 比较UEFI和BIOS的区别。
 1. 描述PXE的大致启动流程。

## 3.2 系统启动流程
 1. 了解NTLDR的启动流程。
 1. 了解GRUB的启动流程。
 1. 比较NTLDR和GRUB的功能有差异。
 1. 了解u-boot的功能。

## 3.3 中断、异常和系统调用比较
 1. 举例说明Linux中有哪些中断，哪些异常？
 1. Linux的系统调用有哪些？大致的功能分类有哪些？  (w2l1)

```
  + 采分点：说明了Linux的大致数量（上百个），说明了Linux系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 1. 以ucore lab8的answer为例，uCore的系统调用有哪些？大致的功能分类有哪些？(w2l1)
 
 ```
  + 采分点：说明了ucore的大致数量（二十几个），说明了ucore系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.4 linux系统调用分析
 1. 通过分析[lab1_ex0](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex0.md)了解Linux应用的系统调用编写和含义。(w2l1)
 

 ```
  + 采分点：说明了objdump，nm，file的大致用途，说明了系统调用的具体含义
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 
 ```
 
 1. 通过调试[lab1_ex1](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex1.md)了解Linux应用的系统调用执行过程。(w2l1)
 

 ```
  + 采分点：说明了strace的大致用途，说明了系统调用的具体执行过程（包括应用，CPU硬件，操作系统的执行过程）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.5 ucore系统调用分析
 1. ucore的系统调用中参数传递代码分析。

	参考`kern/syscall/syscall.c`：

		void
		syscall(void) {
		    struct trapframe *tf = current->tf;
		    uint32_t arg[5];
		    int num = tf->tf_regs.reg_eax;
		    if (num >= 0 && num < NUM_SYSCALLS) {
		        if (syscalls[num] != NULL) {
		            arg[0] = tf->tf_regs.reg_edx;
		            arg[1] = tf->tf_regs.reg_ecx;
		            arg[2] = tf->tf_regs.reg_ebx;
		            arg[3] = tf->tf_regs.reg_edi;
		            arg[4] = tf->tf_regs.reg_esi;
		            tf->tf_regs.reg_eax = syscalls[num](arg);
		            return ;
		        }
		    }
		    print_trapframe(tf);
		    panic("undefined syscall %d, pid = %d, name = %s.\n",
		            num, current->pid, current->name);
		}

	tf是`current->tf`，即当前进程的trap frame。其中eax寄存器中存储系统调用号，用以区分不同的系统调用。系统调用的其他参数分别存储在edx/ecx/ebx/edi/esi存储器中，放入arg[0]~arg[5]。最后通过函数指针`syscalls[num](arg)`，根据系统调用号`num`调用不同的程序，并将返回值存入tf的reg_eax寄存器中，即a寄存器。

	而在用户程序中，参数传递是通过调用一系列汇编语句`asm volatile`来实现的（类似：`"i" (T_SYSCALL)`），将各个寄存器赋予对应的值，再通过系统调用`"int %1;"`进入内核态。
	
	

 2. ucore的系统调用中返回结果的传递代码分析。

	同上，`"=a" (ret)`，内核态将返回结果存在a寄存器中，作为返回值传递回来。

 3. 以ucore lab8的answer为例，分析ucore 应用的系统调用编写和含义。

	代码如第一小题所示，ucore的系统调用通过指定寄存器存储返回值，传递一个`T_SYSCALL`指示调用类型，然后传递各个参数（存在寄存器中）的方法进行系统调用（`"int %1;"`）。


 4. 以ucore lab8的answer为例，尝试修改并运行ucore OS kernel代码，使其具有类似Linux应用工具`strace`的功能，即能够显示出应用程序发出的系统调用，从而可以分析ucore应用的系统调用执行过程。

	在系统调用的同一调用处输出相关信息，修改`kern/trap/trap.c`：
    
		case T_SYSCALL:
	    	cprintf("SYSCALL\n"); // new printf
	        syscall();
	        break;

	也可内核态解析系统调用时输出，即第一小问中的`kern/syscall/syscall.c`，此时可以根据`int num = tf->tf_regs.reg_eax;`判断不同的系统调用。

		
 
## 3.6 请分析函数调用和系统调用的区别
 1. 请从代码编写和执行过程来说明。
   1. 说明`int`、`iret`、`call`和`ret`的指令准确功能
 
