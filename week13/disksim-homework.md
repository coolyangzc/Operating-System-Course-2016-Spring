# 磁盘访问 练习

## 问题 1：请执行 FIFO磁盘调度策略


	./disksim.py  采用FIFO -a 0
	./disksim.py   -a 6
	./disksim.py   -a 30
	./disksim.py   -a 7,30,8
	./disksim.py   -a 10,11,12,13，24,1

请回答每个磁盘请求序列的IO访问时间


>python disksim-homework.py -a 0 -c

	REQUESTS ['0']

	Block:   0  Seek:  0  Rotate:165  Transfer: 30  Total: 195
	
	TOTALS      Seek:  0  Rotate:165  Transfer: 30  Total: 195

>python disksim-homework.py -a 6 -c

	REQUESTS ['6']
	
	Block:   6  Seek:  0  Rotate:345  Transfer: 30  Total: 375
	
	TOTALS      Seek:  0  Rotate:345  Transfer: 30  Total: 375

>python disksim-homework.py -a 30 -c

	REQUESTS ['30']
	
	Block:  30  Seek: 80  Rotate:265  Transfer: 30  Total: 375
	
	TOTALS      Seek: 80  Rotate:265  Transfer: 30  Total: 375

>python disksim-homework.py -a 7,30,8 -c

	REQUESTS ['7', '30', '8']
	
	Block:   7  Seek:  0  Rotate: 15  Transfer: 30  Total:  45
	Block:  30  Seek: 80  Rotate:220  Transfer: 30  Total: 330
	Block:   8  Seek: 80  Rotate:310  Transfer: 30  Total: 420
	
	TOTALS      Seek:160  Rotate:545  Transfer: 90  Total: 795

>python disksim-homework.py -a 10,11,12,13,24,1 -c

REQUESTS ['10', '11', '12', '13', '24', '1']

	Block:  10  Seek:  0  Rotate:105  Transfer: 30  Total: 135
	Block:  11  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  12  Seek: 40  Rotate:320  Transfer: 30  Total: 390
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  24  Seek: 40  Rotate:260  Transfer: 30  Total: 330
	Block:   1  Seek: 80  Rotate:280  Transfer: 30  Total: 390
	
	TOTALS      Seek:160  Rotate:965  Transfer:180  Total:1305

## 问题 2：请执行 SSTF磁盘调度策略

```
./disksim.py   -a 10,11,12,13，24,1
```
请回答每个磁盘请求序列的IO访问时间

>python disksim-homework.py -a 10,11,12,13,24,1 -c -p SSTF

	REQUESTS ['10', '11', '12', '13', '24', '1']
	
	Block:  10  Seek:  0  Rotate:105  Transfer: 30  Total: 135
	Block:  11  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:   1  Seek:  0  Rotate: 30  Transfer: 30  Total:  60
	Block:  12  Seek: 40  Rotate:260  Transfer: 30  Total: 330
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  24  Seek: 40  Rotate:260  Transfer: 30  Total: 330
	
	TOTALS      Seek: 80  Rotate:655  Transfer:180  Total: 915

## 问题 3：请执行 SCAN, C-SCAN磁盘调度策略

```
./disksim.py   -a 10,11,12,13，24,1
```
请回答每个磁盘请求序列的IO访问时间

>python disksim-homework.py -a 10,11,12,13,24,1 -c -p SCAN

	REQUESTS ['10', '11', '12', '13', '24', '1']
	
	Block:  10  Seek:  0  Rotate:105  Transfer: 30  Total: 135
	Block:  11  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:   1  Seek:  0  Rotate: 30  Transfer: 30  Total:  60
	Block:  12  Seek: 40  Rotate:260  Transfer: 30  Total: 330
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  24  Seek:120  Rotate:180  Transfer: 30  Total: 330
	
	TOTALS      Seek:160  Rotate:575  Transfer:180  Total: 915

>python disksim-homework.py -a 10,11,12,13,24,1 -c -p C-SCAN

	REQUESTS ['10', '11', '12', '13', '24', '1']
	
	Block:  10  Seek:  0  Rotate:105  Transfer: 30  Total: 135
	Block:  11  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:   1  Seek:  0  Rotate: 30  Transfer: 30  Total:  60
	Block:  24  Seek: 80  Rotate:220  Transfer: 30  Total: 330
	Block:  12  Seek: 40  Rotate:290  Transfer: 30  Total: 360
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	
	TOTALS      Seek:120  Rotate:645  Transfer:180  Total: 945

为了更好地展示`C-SCAN`磁盘调度策略，可以执行如下测例：
>python disksim-homework.py -a 12,13,14,15,16,17,18,19,20,21,22,23 -G -p C-SCAN

	REQUESTS ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
	
	Block:  23  Seek:120  Rotate: 15  Transfer: 30  Total: 165
	Block:  12  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  14  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  15  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  16  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  17  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  18  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  19  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  20  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  21  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  22  Seek:  0  Rotate:  0  Transfer: 30  Total:  30