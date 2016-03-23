# lab3 SPOC思考题


## 小组思考题
---
(1)(spoc) 请参考lab3_result的代码，思考如何在lab3_results中实现clock算法，给出你的概要设计方案。可4人一个小组。要求说明你的方案中clock算法与LRU算法上相比，潜在的性能差异性。进而说明在lab3的LRU算法实现的可能性评价（给出理由）。

现有的`swap_manager`框架并不足以支持`extended clock`页替换算法，因为只有`_fifo_map_swappable`、`_fifo_swap_out_victim`而并没有供访问页面时调用的函数。需要在此基础上增加访问与修改页面时调用的函数，在该函数中修改访问/修改页面的访问位或修改位。

clock算法与LRU相比：

* 访问/修改在内存中的页时，clock算法只需修改该页的访问/修改位，效率很高；LRU算法需要将该页从栈中取出并压入栈，效率低。
* clock算法在寻找替换页时，要扫描双向循环链表；而LRU算法只需访问栈底的页，效率更高
* 进行页替换时，clock算法将被替换的页的相关信息修改为被替换进入的页接口；而LRU算法需要弹出被替换的页，压入替换入的页，效率更低。
* LRU算法可能能更好地利用局域性原理从而实现更少次数的页替换。


## v9-cpu相关
---
(1)分析并编译运行v9-cpu git repo的testing branch中的,root/etc/os_lab2.c os_lab3.c os_lab3_1.c,理解虚存机制是如何在v9-cpu上实现的，思考如何实现clock页替换算法，并给出你的概要设计方案。

观察`os_lab2.h`中关于`P2V`和`V2P`等常量的设置，然后结合`os_lab2.c`中开启页模式的代码：

		// turn on paging
		pdir(kpdir);
		spage(1);
		kpdir = P2V+(uint)kpdir;
		mem_top = P2V+mem_top;
		
以及跳转用户程序的代码：

		// jump (via return) to high memory
		ksp = P2V+(((uint)kstack + sizeof(kstack) - 8) & -8);
		*ksp = P2V+(uint)mainc;
	
我们分析虚拟地址仅仅通过在虚地址加一个`V2P`或者是地址加一个`P2V`来实现，这一点在用户程序中也得到印证，在`mainc`函数中：

		userinit();            // first user process
		printf("mainc %x, Welcome!\n",mainc);
		pdir(V2P+(uint)(proc0.pdir));
		kstack = proc0.context; //proc0 kstack

所以总之这个代码中实现的虚拟存储管理应该是简单的增加或减去偏移量。

(2)分析并编译运行v9-cpu git repo的testing branch中的,root/etc/os_lab2.c os_lab3.c os_lab3_1.c，理解内存访问异常的各种情况，并给出你的分析结果。