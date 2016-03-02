# lab1 SPOC思考题

描述符特权级DPL、当前特权级CPL和请求特权级RPL的含义是什么？在哪些寄存器中这些字段？对应的访问条件是什么？ (challenge)写出一些简单的小程序（c or asm）来体现这些特权级的区别和联系。
 
- 建议参见链接“ http://blog.csdn.net/better0332/article/details/3416749 ”对特权级的表述，并查阅指令手册。

	描述符特权级DPL规定访问该段的权限级别(Descriptor Privilege Level)，存储在段描述符中，每个段的DPL固定。

	当前特权级CPL是当前进程的权限级别(Current Privilege Level)，是当前正在执行的代码所在的段的特权级，存在于cs寄存器的低两位。

	请求特权级RPL是进程对段访问的请求权限(Request Privilege Level)，是对于段选择子而言的（由段选择子里面的bit 0和bit 1位组合），每个段选择子有自己的RPL，它说明的是进程对段访问的请求权限，有点像函数参数。

	进程特权级检查，一般要求DPL >= max {CPL, RPL}

	输出特权级的小程序：

	如修改用户态程序`user/hello.c`：

		#include <stdio.h>
		#include <ulib.h>
		int
		main(void) {
		    cprintf("Hello world!!.\n");
		    cprintf("I am process %d.\n", getpid());
		    cprintf("hello pass.\n");
		    uint32_t cs = 0;
		    asm volatile("movl %%cs, %0\n" : "=r"(cs));
		    cs &= 3;
		    cprintf("user: %d\n", cs); 
		    return 0;
		}

	修改内核态程序`kern/syscall/syscall.c`：

		static int
		sys_write(uint32_t arg[]) {
			uint32_t cs = 0;
		    asm volatile("movl %%cs, %0\n" : "=r"(cs));
		    cs &= 3;
		    cprintf("kern: %d\n", cs); 
		    int fd = (int)arg[0];
		    void *base = (void *)arg[1];
		    size_t len = (size_t)arg[2];
		    
		    return sysfile_write(fd, base, len);
	
	}