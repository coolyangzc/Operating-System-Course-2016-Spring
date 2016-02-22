# 操作系统概述思考题

* * *

## 个人思考题

###分析你所认识的操作系统（Windows、Linux、FreeBSD、Android、iOS）所具有的独特和共性的功能？

* windows封闭全面，Linux开放，FreeBSD没有使用过，Android开放兼容，IOS用户体验好。
* 它们的共同点是作为一个软件系统管理起来硬件，使上层应用很好的运行起来。


###请总结你认为操作系统应该具有的特征有什么？并对其特征进行简要阐述。

* 提供中断处理程序
*	提供接口供用户程序进行受限的硬件访问
*	提供程序间的通信方式
*	多进程调度
*	多CPU调度

###请给出你觉得的更准确的操作系统的定义？

* 操作系统（Operating System，简称OS）是管理和控制计算机硬件与软件资源的计算机程序，是直接运行在“裸机”上的最基本的系统软件，任何其他软件都必须在操作系统的支持下才能运行。(百度百科)

###你希望从操作系统课学到什么知识？

* 掌握操作系统运行的基本原理，巩固编程能力。


###操作系统内核有什么特征？

* 它负责管理系统的进程、内存、设备驱动程序、文件和网络系统，决定着系统的性能和稳定性。

###操作系统面临什么挑战？

* 分布式系统管理
* 网络化


###什么是操作系统内核？什么是微内核？什么是外核（Exokernel）？

* 操作系统内核是指大多数操作系统的核心部分。它由操作系统中用于管理存储器、文件、外设和系统资源的那些部分组成。操作系统内核通常运行进程，并提供进程间的通信。
* 微内核（Microkernelkernel）结构由一个非常简单的硬件抽象层和一组比较关键的原语或系统调用组成，这些原语仅仅包括了建立一个系统必需的几个部分，如线程管理，地址空间和进程间通信等。

###你理解的虚拟化是什么？

* 在计算机硬件上直接虚拟一层结构，提供给上层接口与使用权。

* * *

## 小组讨论题

* * *

###目前的台式PC机标准配置和价格？

* 联想Erazer X310（i5 4460）
*	CPU型号：Intel 酷睿i5 4460
*	CPU频率：3.2GHz
*	内存容量：8GB DDR3
*	硬盘容量：1TB 7200转
*	显卡芯片：NVIDIA GeForce GTX 750ti 2GB
*	光驱类型：DVD-Rambo
*	操作系统：Windows 8.1 
*	价格：4999

###为什么现在的操作系统基本上用C语言来实现？

* 写操作系统需要编程语言提供以下几个特征：1、跨平台，不能是只在某个平台下编译（VB就不行）；2、必须是编译型语言（PHP就不行），或者有一个非常高效的解释器；3、必须有方便的操作硬件的功能，容易嵌入汇编（Java就不行）；4、兼容性要好，最好不同编译器编译的符号要基本相同，容易链接（C++不行，如果放弃Class的话C++基本可以）；5、编译器本身最好是由该语言自己完成的（大部分语言的编译器都是用C/C++写的）；6、开发者可以很方便的扩展、改造、或者使用第三方的运行库（大部分语言的库都无法修改）；7、开发者众多（小众语言就不行）；8、该语言开发操作系统的资料要足够完善。所以总结下来，C语言是首选。

###为什么没有人用python，java来实现操作系统？

* 同上。

###请评价用C++来实现操作系统的利弊？

* c++作为高级编程语言，实现操作系统可以很好的模块化，但是C++的问题在于混合编译时符号表比较麻烦（VC和GCC生成的全局符号名字不一样），C++的运行效率略低于C，所以一般没有人用C++去写内核。一般可以用c++写驱动什么的。

* * *

## v9-cpu相关题目

* * *

###在v9-cpu中如何实现时钟中断

`timer`变量为运算的指令数，但在`em.c`的具体实现中，`timer`会在pc换页时一次性加上整个页表的指令数（即常量`delta`:4096），同时判断`timer`是否超过阈值`timeout`，若超过且中断使能打开则发生一个时钟中断（`FTIMER`置位1，关中断使能`iena`，转至中断处理）

可通过`TIME`命令设置阈值`timeout`。

`timeout`置零时不产生时钟中断。

###v9-cpu指令，关键变量描述有误或不全的情况

Branch指令应该是pc+=operand0而非跳转到操作数0`(branch to operand0)`

###在v9-cpu中的跳转相关操作是如何实现的

1.根据条件判断是否发生跳转

2.若需要跳转，则修改pc寄存器的值

- 2.a 若跳转后的指令与跳转前的指令在同一页表中，则直接执行下一条指令`(goto next)`。

- 2.b 若跳转后的位置与跳转前的指令不在同一页表中，则需要重新装填页表`(goto fixpc)`


###在v9-cpu中如何设计相应指令，可有效实现函数调用与返回

使用J型指令`(JSR/JSRA)`，在函数调用时，将返回地址、调用参数等依序压栈。在函数调用和返回时再分别通过J型指令跳转到对应地址。

###emhello/os0/os1等程序被加载到内存的哪个位置,其堆栈是如何设置的

    read(f, (void*)mem, st.st_size - sizeof(hdr))
根据如上语句，程序被加载到`mem`处，即内存起始位置。

    cpu(hdr.entry, memsz - FS_SZ);
初始调用`cpu(pc, sp)`时，sp的初值是内存大小减去RAM文件系统的大小，默认为128M-4M=124M，故栈指针是从大到小增长的。

###在v9-cpu中如何完成一次内存地址的读写

页大小是`4K(2^12)`，页表条目数是`1M(2^20)`，并分为两级。包括核心态读写页表与用户态读写页表。有两个指针`tr/tw`， 分别指向内核态或用户态的`read/write page translation table`，对地址做了虚实转换：

    tr/tw[page number]=phy page number //页帧号

tpages存储每一个虚页表项，使用`flush()`清空Table：
    
    flush()
    {
      uint v; 
      while (tpages) {
        v = tpage[--tpages];
        trk[v] = twk[v] = tru[v] = twu[v] = 0;    
      }
    }

在访问`虚地址v`时，取其高20位访问`tr/tw`，若不存在则调用`rlook/wlook`

    if (!(p = tr[(v >> 12]) && !(p = rlook(v)))

`rlook`:

    uint rlook(uint v)
    {
      uint pde, *ppde, pte, *ppte, q, userable;
      if (!paging) return setpage(v, v, 1, 1); //未开启虚拟内存
      pde = *(ppde = (uint *)(pdir + (v>>22<<2))); // 取虚地址高10位作为page directory entry（第一级页表）
      if (pde & PTE_P) { //如果是当前页表
        if (!(pde & PTE_A)) *ppde = pde | PTE_A; //置访问位(Access)
        if (pde >= memsz) { trap = FMEM; vadr = v; return 0; } //bad physical address
        pte = *(ppte = (uint *)(mem + (pde & -4096) + ((v >> 10) & 0xffc))); // page table entry //取中间10位（第二级页表）
        if ((pte & PTE_P) && ((userable = (q = pte & pde) & PTE_U) || !user)) {
          if (!(pte & PTE_A)) *ppte = pte | PTE_A; //置访问位(Access)
          return setpage(v, pte, (pte & PTE_D) && (q & PTE_W), userable); // set writable after first write so dirty gets set
        }
      }

      //page fault on read
      trap = FRPAGE;
      vadr = v;
      return 0;
    }


###在v9-cpu中如何实现分页机制

见上题