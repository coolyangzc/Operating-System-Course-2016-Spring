# lec5 SPOC思考题

## 提前准备

- 完成lec５的视频学习和提交对应的在线练习
- git pull ucore_os_lab, v9_cpu, os_course_spoc_exercises 　in github repos。这样可以在本机上完成课堂练习。
- 理解连续内存动态分配算法的实现（主要自学和网上查找）

NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy systemm分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)

最先匹配

	优点：简单；在高地址空间有大块的空闲分区
	缺点：外部碎片；分配大块时较慢，前面分的越碎越慢
最佳匹配

	优点：大部分分配的尺寸较小时，效果很好：可避免大的空闲分区被拆分；可减小外部碎片的大小；相对简单
	缺点：外部碎片；释放分区较慢；容易产生很多无用的小碎片；
最差匹配

	优点：中等大小的分配较多时，效果最好；避免出现太多的小碎片
	缺点：释放分区较慢；外部碎片

伙伴系统

	优点：分配、释放分区较快；地址整齐；能较好地胜任各种随机大小的尺寸分配。
	缺点：外碎片和内碎片；类线段树的组织方式使得有些时候明明有足够的连续空间却没法分配

	

>  

## 小组思考题

请参考ucore lab2代码，采用`struct pmm_manager` 根据你的`学号 mod 4`的结果值，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种或多种，在应用程序层面(可以 用python,ruby,C++，C，LISP等高语言)来实现，给出你的设计思路，并给出测试用例。 (spoc)

```
如何表示空闲块？ 如何表示空闲块列表？ 
[(start0, size0),(start1,size1)...]
在一次malloc后，如果根据某种顺序查找符合malloc要求的空闲块？如何把一个空闲块改变成另外一个空闲块，或消除这个空闲块？如何更新空闲块列表？
在一次free后，如何把已使用块转变成空闲块，并按照某种顺序（起始地址，块大小）插入到空闲块列表中？考虑需要合并相邻空闲块，形成更大的空闲块？
如果考虑地址对齐（比如按照4字节对齐），应该如何设计？
如果考虑空闲/使用块列表组织中有部分元数据，比如表示链接信息，如何给malloc返回有效可用的空闲块地址而不破坏
元数据信息？
伙伴分配器的一个极简实现
http://coolshell.cn/tag/buddy
```

最先匹配算法实现
 - 思路：通过维护一个链表记录当前free的内存区域，malloc和free时通过修改链表实现，其中free时有表项的合并等等问题。
 - 测试用例见main函数。

		typedef unsigned int uint;
		
		union header {
		  struct {
		    union header *ptr;
		    uint size;
		  } s;
		  long x;
		};
		
		typedef union header Header;
		
		static Header b1, b2;
		static Header *head = &b1, *tail = &b2;
		
		
		Header*
		free(void *ap)
		{
		  Header *bp, *p, *prevp = head;
		
		  bp = (Header*)ap - 1;
			for (p = prevp->s.ptr; p != tail; prevp = p, p = p->s.ptr){
				if (bp > p && bp < p->s.ptr)
					break;
			}
			if (p == tail){
				head->s.ptr = bp;
				bp->s.ptr = tail;
				return bp;
			}
			else{
				  if(bp + bp->s.size == p->s.ptr){
					bp->s.size += p->s.ptr->s.size;
					bp->s.ptr = p->s.ptr->s.ptr;
				  } else
					bp->s.ptr = p->s.ptr;
				
				  if(p + p->s.size == bp){
					p->s.size += bp->s.size;
					p->s.ptr = bp->s.ptr;
					return p;
				  } else{
					p->s.ptr = bp;
					return bp;
				  }
			}
		}
		
		static Header*
		morecore(uint nu)
		{
		  char *p;
		  Header *hp;
		
		  if(nu < 4096)
		    nu = 4096;
		  p = sbrk(nu * sizeof(Header));
		  if(p == (char*)-1)
		    return 0;
		  hp = (Header*)p;
		  hp->s.size = nu;
		  return free((void*)(hp + 1)) + 1;
		}
		
		void*
		malloc(uint nbytes)
		{
		  Header *p, *prevp = head;
		  uint nunits;
		
		  nunits = (nbytes + sizeof(Header) - 1)/sizeof(Header) + 1;
			for (p = prevp->s.ptr; p != tail; prevp = p, p = p->s.ptr){
				if (p->s.size >= nunits){
					  if(p->s.size == nunits)
						prevp->s.ptr = p->s.ptr;
					  else {
						p->s.size -= nunits;
						p += p->s.size;
						p->s.size = nunits;
					  }
					  return (void*)(p + 1);
				}
			}
			return (void*)morecore(nunits);
		}
		
		void main(){
			head->s.ptr = tail;
			Header* f = (Header*)malloc(1000);
			free((void*) f);
			return;
		}
