#include <stdio.h>
int stat_count(){
	static int count;
	return ++count;
}

int main(){
	stat_count();
	stat_count();
	printf("Count is: %d\n", stat_count());
	return 0;
}
