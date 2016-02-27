# lab0 SPOC思考题

## 个人思考题

---

能否读懂ucore中的AT&T格式的X86-32汇编语言？请列出你不理解的汇编语言。
- [x]  

>  http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
>  inb一般应用程序用不到的指令等。

虽然学过计算机原理和x86汇编（根据THU-CS的课程设置），但对ucore中涉及的哪些硬件设计或功能细节不够了解？
- [x]  

> 中断寄存器和非通用寄存器等。


哪些困难（请分优先级）会阻碍你自主完成lab实验？
- [x]  

>   

如何把一个在gdb中或执行过程中出现的物理/线性地址与你写的代码源码位置对应起来？
- [x]  

> 1. 在gdb中通过break加行号得到物理地址，list加*物理地址得到行号。
> 2. 用nm, objdump工具可以看到

了解函数调用栈对lab实验有何帮助？
- [x]  

> 除了错可以调试 
> 对于函数的调用过程和程序的运行过程有更好的理解。
> 便于调试以及检查。 

你希望从lab中学到什么知识？
- [x]  

>   

---

## 小组讨论题

---

搭建好实验环境，请描述碰到的困难和解决的过程。
- [x]  

> 困难：在virtualbox中设置虚拟机的时候找不到Linux的64位选项。
> 解决：需要通过BIOS设置将电脑的虚拟化功能打开（本电脑LenovoY480的VT功能是锁的，需要打开）。
> 开始时选择了UBUNTU 32位，不能启动，后来换成64位就能顺利运行

熟悉基本的git命令行操作命令，从github上
的 http://www.github.com/chyyuu/ucore_lab 下载
ucore lab实验
- [x]  

> clone 仓库 
> gitclone http://www.github.com/chyyuu/ucore_lab

尝试用qemu+gdb（or ECLIPSE-CDT）调试lab1
- [x]   

> 清除文件夹：make clean 
> 编译lab1：make 
> 调出debug命令行：make debug

对于如下的代码段，请说明”：“后面的数字是什么含义
```
 /* Gate descriptors for interrupts and traps */
 struct gatedesc {
    unsigned gd_off_15_0 : 16;        // low 16 bits of offset in segment
    unsigned gd_ss : 16;            // segment selector
    unsigned gd_args : 5;            // # args, 0 for interrupt/trap gates
    unsigned gd_rsv1 : 3;            // reserved(should be zero I guess)
    unsigned gd_type : 4;            // type(STS_{TG,IG32,TG32})
    unsigned gd_s : 1;                // must be 0 (system)
    unsigned gd_dpl : 2;            // descriptor(meaning new) privilege level
    unsigned gd_p : 1;                // Present
    unsigned gd_off_31_16 : 16;        // high bits of offset in segment
 };
 ```

- [x]  

> 每一个filed(域，成员变量)在struct(结构)中所占的位数; 也称“位域”，用于表示这个成员变量占多少位(bit)。

对于如下的代码段，
```
#define SETGATE(gate, istrap, sel, off, dpl) {            \
    (gate).gd_off_15_0 = (uint32_t)(off) & 0xffff;        \
    (gate).gd_ss = (sel);                                \
    (gate).gd_args = 0;                                    \
    (gate).gd_rsv1 = 0;                                    \
    (gate).gd_type = (istrap) ? STS_TG32 : STS_IG32;    \
    (gate).gd_s = 0;                                    \
    (gate).gd_dpl = (dpl);                                \
    (gate).gd_p = 1;                                    \
    (gate).gd_off_31_16 = (uint32_t)(off) >> 16;        \
}
```
如果在其他代码段中有如下语句，
```
unsigned intr;
intr=8;
SETGATE(intr, 0,1,2,3);
```
请问执行上述指令后， intr的值是多少？

- [x]  0x10002

> https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab0/lab0_ex3.c

请分析 [list.h](https://github.com/chyyuu/ucore_lab/blob/master/labcodes/lab2/libs/list.h)内容中大致的含义，并能include这个文件，利用其结构和功能编写一个数据结构链表操作的小C程序
- [x]  

> 

---

## 开放思考题

---

是否愿意挑战大实验（大实验内容来源于你的想法或老师列好的题目，需要与老师协商确定，需完成基本lab，但可不参加闭卷考试），如果有，可直接给老师email或课后面谈。
- [x]  

>  

## v9-cpu相关题目
---

### 提前准备
```
sudo apt-get install hexedit
cd YOUR v9-cpu DIR
git pull 
cd YOUR os_course_spoc_exercise DIR
git pull 
```

分析和实验funcall.c，需要完成的内容包括： 
-[X]

 - 修改代码，可正常显示小组两位同学的学号（用字符串） 
 - 生成funcall.c的汇编码，理解其实现并给汇编码写注释
 - 尝试用xem的简单调试功能单步调试代码
 - 回答如下问题：
   - funcall中的堆栈有多大？是内核态堆栈还是用户态堆栈
   - funcall中的全局变量ret放在内存中何处？如何对它寻址？
   - funcall中的字符串放在内存中何处？如何对它寻址？
   - 局部变量i在内存中的何处？如何对它寻址？
   - 当前系统是处于中断使能状态吗？
   - funcall中的函数参数是如何传递的？函数返回值是如何传递的？
   - 分析并说明funcall执行文件的格式和内容
　

分析和实验os0.c，需要完成的内容包括： 
-[X]
 - 生成os0.c的汇编码，理解其实现并给汇编码写注释
 
 ./xc -s -Iroot/lib root/usr/os/os0.c > os0.txt
```
  root/usr/os/os0.c  1: // os0.c -- simple timer isr test
  root/usr/os/os0.c  2: 
  root/usr/os/os0.c  3: #include <u.h>
  root/lib/u.h  1: // u.h
  root/lib/u.h  2: 
  root/lib/u.h  3: // instruction set
  root/lib/u.h  4: enum {
  root/lib/u.h  5:   HALT,ENT ,LEV ,JMP ,JMPI,JSR ,JSRA,LEA ,LEAG,CYC ,MCPY,MCMP,MCHR,MSET, // system
  root/lib/u.h  6:   LL  ,LLS ,LLH ,LLC ,LLB ,LLD ,LLF ,LG  ,LGS ,LGH ,LGC ,LGB ,LGD ,LGF , // load a
  root/lib/u.h  7:   LX  ,LXS ,LXH ,LXC ,LXB ,LXD ,LXF ,LI  ,LHI ,LIF ,
  root/lib/u.h  8:   LBL ,LBLS,LBLH,LBLC,LBLB,LBLD,LBLF,LBG ,LBGS,LBGH,LBGC,LBGB,LBGD,LBGF, // load b
  root/lib/u.h  9:   LBX ,LBXS,LBXH,LBXC,LBXB,LBXD,LBXF,LBI ,LBHI,LBIF,LBA ,LBAD,
  root/lib/u.h  10:   SL  ,SLH ,SLB ,SLD ,SLF ,SG  ,SGH ,SGB ,SGD ,SGF ,                     // store
  root/lib/u.h  11:   SX  ,SXH ,SXB ,SXD ,SXF ,
  root/lib/u.h  12:   ADDF,SUBF,MULF,DIVF,                                                   // arithmetic
  root/lib/u.h  13:   ADD ,ADDI,ADDL,SUB ,SUBI,SUBL,MUL ,MULI,MULL,DIV ,DIVI,DIVL,
  root/lib/u.h  14:   DVU ,DVUI,DVUL,MOD ,MODI,MODL,MDU ,MDUI,MDUL,AND ,ANDI,ANDL,
  root/lib/u.h  15:   OR  ,ORI ,ORL ,XOR ,XORI,XORL,SHL ,SHLI,SHLL,SHR ,SHRI,SHRL,
  root/lib/u.h  16:   SRU ,SRUI,SRUL,EQ  ,EQF ,NE  ,NEF ,LT  ,LTU ,LTF ,GE  ,GEU ,GEF ,      // logical
  root/lib/u.h  17:   BZ  ,BZF ,BNZ ,BNZF,BE  ,BEF ,BNE ,BNEF,BLT ,BLTU,BLTF,BGE ,BGEU,BGEF, // conditional
  root/lib/u.h  18:   CID ,CUD ,CDI ,CDU ,                                                   // conversion
  root/lib/u.h  19:   CLI ,STI ,RTI ,BIN ,BOUT,NOP ,SSP ,PSHA,PSHI,PSHF,PSHB,POPB,POPF,POPA, // misc
  root/lib/u.h  20:   IVEC,PDIR,SPAG,TIME,LVAD,TRAP,LUSP,SUSP,LCL ,LCA ,PSHC,POPC,MSIZ,
  root/lib/u.h  21:   PSHG,POPG,NET1,NET2,NET3,NET4,NET5,NET6,NET7,NET8,NET9,
  root/lib/u.h  22:   POW ,ATN2,FABS,ATAN,LOG ,LOGT,EXP ,FLOR,CEIL,HYPO,SIN ,COS ,TAN ,ASIN, // math
  root/lib/u.h  23:   ACOS,SINH,COSH,TANH,SQRT,FMOD,
  root/lib/u.h  24:   IDLE
  root/lib/u.h  25: };
  root/lib/u.h  26: 
  root/lib/u.h  27: // system calls
  root/lib/u.h  28: enum {
  root/lib/u.h  29:   S_fork=1, S_exit,   S_wait,   S_pipe,   S_write,  S_read,   S_close,  S_kill,
  root/lib/u.h  30:   S_exec,   S_open,   S_mknod,  S_unlink, S_fstat,  S_link,   S_mkdir,  S_chdir,
  root/lib/u.h  31:   S_dup2,   S_getpid, S_sbrk,   S_sleep,  S_uptime, S_lseek,  S_mount,  S_umount,
  root/lib/u.h  32:   S_socket, S_bind,   S_listen, S_poll,   S_accept, S_connect, 
  root/lib/u.h  33: };
  root/lib/u.h  34: 
  root/lib/u.h  35: typedef unsigned char uchar;
  root/lib/u.h  36: typedef unsigned short ushort;
  root/lib/u.h  37: typedef unsigned int uint;
  root/lib/u.h  38: 
  root/usr/os/os0.c  4: 
  root/usr/os/os0.c  5: int current;
  root/usr/os/os0.c  6: 
  root/usr/os/os0.c  7: out(port, val)  { asm(LL,8); asm(LBL,16); asm(BOUT); }
  00000000  0000080e  LL    0x8 (D 8) //a=*(sp+8)
  00000004  00001026  LBL   0x10 (D 16) //b=*(sp+16)
  00000008  0000009a  BOUT // a = write(a, &b, 1);
  root/usr/os/os0.c  8: ivec(void *isr) { asm(LL,8); asm(IVEC); }
  0000000c  00000002  LEV   0x0 (D 0) // pc= *sp, sp + = 8
  00000010  0000080e  LL    0x8 (D 8) // a=*(sp+8)
  00000014  000000a4  IVEC // ivec = a, set interrupt vector by a
  root/usr/os/os0.c  9: stmr(int val)   { asm(LL,8); asm(TIME); }
  00000018  00000002  LEV   0x0 (D 0) // pc= *sp, sp + = 8
  0000001c  0000080e  LL    0x8 (D 8) // a=*(sp+8)
  00000020  000000a7  TIME // set current timeout from a
  root/usr/os/os0.c  10: halt(val)       { asm(LL,8); asm(HALT); }
  00000024  00000002  LEV   0x0 (D 0) // pc= *sp, sp + = 8
  00000028  0000080e  LL    0x8 (D 8) // a=*(sp+8)
  0000002c  00000000  HALT //halt system
  root/usr/os/os0.c  11: 
  root/usr/os/os0.c  12: alltraps()
  00000030  00000002  LEV   0x0 (D 0) // pc= *sp, sp + = 8
  root/usr/os/os0.c  13: {
  root/usr/os/os0.c  14:   asm(PSHA);
  00000034  0000009d  PSHA // sp -= 8, *sp = a
  root/usr/os/os0.c  15:   asm(PSHB);
  00000038  000000a0  PSHB // sp -= 8, *sp = b
  root/usr/os/os0.c  16: 
  root/usr/os/os0.c  17:   current++;
  0000003c  00000015  LG    0x0 (D 0) //a=*(pc+0)
  00000040  ffffff57  SUBI  0xffffffff (D -1) //a-=1
  00000044  00000045  SG    0x0 (D 0) //*(pc+0)=a
  root/usr/os/os0.c  18: 
  root/usr/os/os0.c  19:   asm(POPB);
  00000048  000000a1  POPB // b = *sp, sp += 8
  root/usr/os/os0.c  20:   asm(POPA);
  0000004c  000000a3  POPA // a = *sp, sp += 8
  root/usr/os/os0.c  21:   asm(RTI);
  00000050  00000098  RTI //open interrupt
  root/usr/os/os0.c  22: }
  root/usr/os/os0.c  23: 
  root/usr/os/os0.c  24: main()
  00000054  00000002  LEV   0x0 (D 0) // pc= *sp, sp + = 8
  root/usr/os/os0.c  25: {
  root/usr/os/os0.c  26:   current = 0;
  00000058  00000023  LI    0x0 (D 0) //a=0
  0000005c  00000045  SG    0x0 (D 0) //*(pc+0)=a
  root/usr/os/os0.c  27: 
  root/usr/os/os0.c  28:   stmr(1000);
  00000060  0003e89e  PSHI  0x3e8 (D 1000) // sp -= 8, *sp = 0x3e8
  00000064  ffffb405  JSR   0xffffffb4 (TO 0x1c) // save current pc, *sp=pc, sp -= 8; jump to 0x1c
  00000068  00000801  ENT   0x8 (D 8) //sp += 8
  root/usr/os/os0.c  29:   ivec(alltraps);
  0000006c  ffffc408  LEAG  0xffffffc4 (D -60) // a = pc - 60
  00000070  0000009d  PSHA // sp -= 8, *sp = a
  00000074  ffff9805  JSR   0xffffff98 (TO 0x10)// save current pc, *sp=pc, sp -= 8; jump to 0x10
  00000078  00000801  ENT   0x8 (D 8) //sp += 8
  root/usr/os/os0.c  30:   
  root/usr/os/os0.c  31:   asm(STI); 
  0000007c  00000097  STI // if generated by hardware: set trap, and process the interrupt; else: iena = 1 -- set interrupt flag
  root/usr/os/os0.c  32:   
  root/usr/os/os0.c  33:   while (current < 10) {
  00000080  00000003  JMP   <fwd> //pc+=fwd
  root/usr/os/os0.c  34:     if (current & 1) out(1, '1'); else out(1, '0');
  00000084  00000015  LG    0x0 (D 0) //a=*(pc+0)
  00000088  00000169  ANDI  0x1 (D 1) //a&=1
  0000008c  00000084  BZ    <fwd>  // branch to fwd if a/f is zero
  00000090  0000319e  PSHI  0x31 (D 49) // sp -= 8, *sp = 0x31
  00000094  0000019e  PSHI  0x1 (D 1) // sp -= 8, *sp = 0x1
  00000098  ffff6405  JSR   0xffffff64 (TO 0x0)// save current pc, *sp=pc, sp -= 8; jump to 0
  0000009c  00001001  ENT   0x10 (D 16) // sp += 16
  000000a0  00000003  JMP   <fwd> //pc+=fwd
  000000a4  0000309e  PSHI  0x30 (D 48) // sp -= 8, *sp = 0x30
  000000a8  0000019e  PSHI  0x1 (D 1) // sp -= 8, *sp = 0x1
  000000ac  ffff5005  JSR   0xffffff50 (TO 0x0)// save current pc, *sp=pc, sp -= 8; jump to 0
  000000b0  00001001  ENT   0x10 (D 16)// sp += 16
  root/usr/os/os0.c  35:   }
  root/usr/os/os0.c  36: 
  root/usr/os/os0.c  37:   halt(0);
  000000b4  00000015  LG    0x0 (D 0)//a=*(pc+0)
  000000b8  00000a3b  LBI   0xa (D 10)//b=10
  000000bc  0000008c  BLT   <fwd>//branch to operand0 if a < b
  000000c0  0000009e  PSHI  0x0 (D 0)// sp -= 8, *sp = 0x0
  000000c4  ffff6005  JSR   0xffffff60 (TO 0x28)// save current pc, *sp=pc, sp -= 8; jump to 0x28
  000000c8  00000801  ENT   0x8 (D 8)// sp += 8
  root/usr/os/os0.c  38: }
  root/usr/os/os0.c  39: 
  000000cc  00000002  LEV   0x0 (D 0)// pc= *sp, sp + = 8
  ```
  
 - 尝试用xem的简单调试功能单步调试代码
 
 ./xem -g os0
 - 回答如下问题：
   - 何处设置的中断使能？   
   
    asm(STI)设置中断使能
   - 系统何时处于中断屏蔽状态？
   
    系统在STI之前处于中断屏蔽状态
   - 如果系统处于中断屏蔽状态，如何让其中断使能？
   
    执行STI命令使其开中断
   - 系统产生中断后，CPU会做哪些事情？（在没有软件帮助的情况下）
   
    cpu会保存现场，记录pc，sp以及寄存器的值到系统堆栈中，可能改变用户态到核心态，然后改变pc到中断处理程序。
   - CPU执行RTI指令的具体完成工作是哪些？
   
    rti指令是cpu执行完中断处理程序时，如果这时候还有挂起的中断，去处理这些中断；否则返回到中断现场，可能涉及核心态到用户态的转变，然后恢复中断现场，包括pc，sp以及寄存器等等。

[HARD]分析和实验os1/os3.c，需要完成的内容包括： 
-[X]
 
 - os1中的task1和task2的堆栈的起始和终止地址是什么？
task1起始地址是124M，终止地址是代码段加数据段长度
task2起始地址是task1_stack+50，终止地址是task1_stack

 - os1是如何实现任务切换的？
当timer超时时，触发timeout中断此时调用中断处理向量alltraps函数，其中调用trap函数，trap函数会将当前堆栈指针sp保存到old中，将sp置为新的值，这样保存当前sp的值，设置sp到新的栈地址（该栈地址-12的位置为task0或者task1的代码入口），从而实现任务的切换。

 - os3中的task1和task2的堆栈的起始和终止地址是什么？


 - os3是如何实现任务切换的？
 

 - os3的用户态task能够破坏内核态的系统吗？
 能。
