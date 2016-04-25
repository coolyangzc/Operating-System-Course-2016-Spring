## 个人思考题

#### Bakery算法的choosing作用 ####

Bakery算法摘入如下：

	do{
	    choosing[i] = ture;
	    number[i] = max(number[0],number[1],...,number[n-1])+1;
	    choosing[i] = false;
	    for(j=0; j < n; j++) {
	        while(choosing[j]);
	        while((number[j] != 0) && ((number[j],j) < (number[i],i)));
	    }
	        //critical section
	    number[i] = 0;
	        //remainder section
	} while(1);

`choosing`的作用是保证每个线程在完整计算完自己的`number[i]`后，该值才会被其他线程用于比较。

若去掉`choosing`：

	do{
	    number[i] = max(number[0],number[1],...,number[n-1])+1;
	    for(j=0; j < n; j++) {
	        while((number[j] != 0) && ((number[j],j) < (number[i],i)));
	    }
	        //critical section
	    number[i] = 0;
	        //remainder section
	} while(1);

此时`number[i]`的计算与赋值的不同步可能成为漏洞：进程0和进程1均计算出自己的`number`为1且还未赋值。进程1赋值后，进入循环，判断进程0未就绪(`number[0]还未赋值`)，然后就能进入临界区。

然后轮换到进程0执行，进程0因为拥有最小的`pid`以及同样最小的`number[0] = 1`，也顺利进入临界区。所以去除了`choosing`的`Bakery`算法没法实现忙时等待。

综上，产生这个漏洞的原因是`number`值的计算与赋值不同步，而`choosing`能保证`number`的计算完成后再会被其他进程用来比较，排除了上文所述的不同步问题。