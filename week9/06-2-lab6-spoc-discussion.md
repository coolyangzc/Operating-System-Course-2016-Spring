# lab6 spoc 思考题

- 有"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的ucore_code和os_exercises的git repo上。


## 个人思考题

### 16.1 总体介绍

1. 进程控制块中与调度相关的字段有哪些？
2. ucore的就绪队列数据结构在哪定义？在哪进行修改？
3. ucore的等待队列数据结构在哪定义？在哪进行修改？

### 16.2 调度算法支撑框架

1. 调度算法支撑框架中的各个函数指针的功能是啥？会被谁在何种情况下调用？

 > 初始化、触发、选取、出队、入队、切换

2. 调度函数schedule()的调用函数分析，可以了解进程调度的原因。请分析ucore中所有可能的调度位置，并说明可能的调用原因。
  
### 16.3 时间片轮转调度算法

1. 时间片轮转调度算法是如何基于调度算法支撑框架实现的？
2. 时钟中断如何调用RR_proc_tick()的？

### 16.4 stride调度算法

1. stride调度算法的思路？ 
2. stride算法的特征是什么？
3. stride调度算法是如何避免stride溢出问题的？
4. 无符号数的有符号比较会产生什么效果？

 > [无符号数的有符号比较会产生什么效果？](https://piazza.com/class/i5j09fnsl7k5x0?cid=357)

5. 什么是斜堆(skew heap)？斜堆在stride算法的实现中有什么用？

 > 参考文档：[Skew heap](https://en.wikipedia.org/wiki/Skew_heap) [斜堆](http://baike.baidu.com/link?url=BYMgWi8gT5sZE2sG0ndX1CoYZVhe5NJig5s9-u1gO7ldVIxRwLzUpL9pvqN5qEOk_8nGUuJ7VSZNU8pGSicUnK)


## 小组练习与思考题

### (1)(spoc) 跟踪和展现ucore的处理机调度过程

在ucore执行处理机调度时，跟踪并显示上一个让出CPU线程的暂停代码位置和下一个进入执行状态线程的开始执行位置。

### (2)(spoc) 理解调度算法支撑框架的执行过程

即在ucore运行过程中通过`cprintf`函数来完整地展现出来多个进程在调度算法和框架的支撑下，在相关调度点如何动态调度和执行的细节。(越全面细致越好)

请完成如下练习，完成代码填写，并形成spoc练习报告
> 需写练习报告和简单编码，完成后放到git server 对应的git repo中

### (3)(spoc) lab6\_stride的溢出判断问题

在ucore中使用如下语句进行步长值大小的判断，其中`lab6_stride`是步长值：

	if ((int32_t)(p->lab6_stride - q->lab6_stride) > 0)
		p = q;

在步长值可能溢出的情况下，上式仍然能够正确判断。原因如下：

首先，任意两个步长值的差距不会超过`BIG_STRIDE`，因为当前步长值最小的进程会被调度，而最大的步进值就是`BIG_STRIDE`：

	#define BIG_STRIDE    0x7FFFFFFF /* ??? */

`BIG_STRIDE`是`2^32 / 2 - 1`，也即无符号32位整型的一半减一。

* 若p和q均未溢出，判断式自然正确
* 若p溢出，q未溢出，此时有p > q，且p最高位为0，q最高位为1(p和q差值至多为32位一半减一)，此时p-q的最高位为0，强转为32位有符号整型的结果为正数，判断出p > q。
* 若p未溢出，q溢出，此时有p < q，且p最高位为1，q最高位为0(p和q差值至多为32位一半减一)，此时p-q的最高位为1，强转为32位有符号整型的结果为负数，判断出p < q。
* 若p和q均溢出，此时两者的溢出次数要么相同，要么相差一(p和q差值至多为32位一半减一)，相当于两者模2^32，还原成前3种情况，能正确判断出p,q的大小关系。

### 练习用的[lab6 spoc exercise project source code](https://github.com/chyyuu/ucore_lab/tree/master/labcodes_answer/lab6_result)


