40.知错能改

进程p0,p1共享变量flag,turn;他们进入临界区的算法如下:

	var flag:array[0..1] of boolean;//初值为false
	turn:0 1
	process i (0或1)
		while true
		do begin
			flag[i] =true;
			while turn!=i
			do begin
				while flag[j]==false
				do skip;//skip为空语句
				turn = i
			end
			临界区;
			flag[i] = false;
			出临界区;
		end

该算法能否正确地实现互斥?若不能,应该如何修改(假设flag,turn单元内容的修改和访问是互斥的).

	不能正确实现互斥。

直接参照`Peterson算法`修改如下：

	var flag:array[0..1] of boolean;//初值为false
	turn:0 1
	process i (0或1)
		while true
		do begin
			flag[i] =true;
			turn = j;
			while (flag[j] && turn == j)
			do skip;//skip为空语句

			临界区;
			flag[i] = false;
			出临界区;
		end