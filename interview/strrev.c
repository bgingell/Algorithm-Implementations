#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void strrev(char *s){
	int len = strlen(s);
	int k = len-1;
	int i = 0;
	while(i <= k){
		s[len] = s[i];
		s[i] = s[k];
		s[k] = s[len];
		i++;
		k--;
	}
	s[len] = '\0';
}

void main(){
	char *s = malloc(5);
	memset(s, 0, 5);
	strcpy(s, "ruff");
	printf("%s ", s);
	strrev(s);
	printf("%s\n", s);
	free(s);
}
