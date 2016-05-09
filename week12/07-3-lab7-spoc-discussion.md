# 同步互斥(lec 19 lab7) spoc 思考题
 
## 小组思考题

1. (扩展练习) 每人用ucore中的信号量和条件变量两种手段分别实现40个同步问题中的一题。向勇老师的班级从前往后，陈渝老师的班级从后往前。请先理解与采用python threading 机制实现的异同点。

2. （扩展练习）请在lab7-answer中分析
  -  cvp->count含义是什么？cvp->count是否可能<0, 是否可能>1？请举例或说明原因。
  -  cvp->owner->next\_count含义是什么？cvp->owner->next_count是否可能<0, 是否可能>1？请举例或说明原因。
  -  目前的lab7-answer中管程的实现是Hansen管程类型还是Hoare管程类型？请在lab7-answer中实现另外一种类型的管程。

cvp->count含义是等待条件变量`cvp`的进程/线程数目。

cvp->count不可能小于零，因为所有cvp->count的增加都在对应的减少操作之前，而程序执行的顺序是固定的，与同步互斥无关。

cvp->count可能大于1，如多个进程等待同一个信号量。

cvp->owner->next\_count含义是发出条件变量`cvp`的signal的正在等待的进程/线程数目。

cvp->owner->next\_count不可能小于0，因为所有cvp->owner->next\_count的增加都在对应的减少操作之前，而程序执行的顺序是固定的，与同步互斥无关。

cvp->owner->next\_count不可能大于1，因为next\_count的增加是在cond\_signal过程中；而某一个cond\_signal过程在执行期间将全程持有互斥锁`mt.mutex`（该互斥锁会短暂传递给某一个cond_wait进程，然后再返还回来，在此过程中因为没有方法获取互斥锁`mt.mutex`，所以不可能有第二个进程/线程调用cond\_signal）。故cvp->owner->next\_count的增加与减少将配套执行。

目前的lab7-answer中管程的实现是Hoare管程类型。
