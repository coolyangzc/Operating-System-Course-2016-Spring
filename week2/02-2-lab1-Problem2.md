# lab1 SPOC思考题

比较不同特权级的中断切换时的堆栈变化差别；(challenge)写出一些简单的小程序（c or asm）来显示出不同特权级的的中断切换的堆栈变化情况。

- 内核态时，CPU仅把eflags和中断返回指针cs，eip压入当前内核态堆栈
用户态时，CPU会首先把原用户态堆栈指针ss和esp压入内核态堆栈，随后把标志积存器eflags的内容和返回位置cs，eip压入内核态堆栈。

	中断程序统一入口`kern/trap/trapentry.S`中，将各个寄存器压入栈中，输出即可显示相关信息：

		#include <memlayout.h>
		# vectors.S sends all traps here.
		.text
		.globl __alltraps
		__alltraps:
		    # push registers to build a trap frame	
		    # therefore make the stack look like a struct trapframe	
		    pushl %ds	
		    pushl %es
		    pushl %fs	
		    pushl %gs	
		    pushal	
		    # load GD_KDATA into %ds and %es to set up data segments for kernel
		    movl $GD_KDATA, %eax
		    movw %ax, %ds
		    movw %ax, %es
		    # push %esp to pass a pointer to the trapframe as an argument to trap()
		    pushl %esp
		    # call trap(tf), where tf=%esp
		    call trap
		    # pop the pushed stack pointer
		    popl %esp
		    # return falls through to trapret...
		.globl __trapret
		__trapret:
		    # restore registers from stack
		    popal
		    # restore %ds, %es, %fs and %gs
		    popl %gs
		    popl %fs
		    popl %es
		    popl %ds
		    # get rid of the trap number and error code
		    addl $0x8, %esp
		    iret
		.globl forkrets
		forkrets:
		    # set stack to this new process's trapframe
		    movl 4(%esp), %esp
		    jmp __trapret