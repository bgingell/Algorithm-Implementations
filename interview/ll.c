#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
	int val;
	struct node *n;
} node;

node * alloc_node(int val){
	node *n = malloc(sizeof(node));
	memset(n, 0, sizeof(node));
	n->val = val;
	return n;
}

node * rev(node *h){
	if(h == NULL) return NULL;
	if(h->n == NULL) return h;

	node *a, *b, *c;

	a = h;
	b = a->n;
	c = NULL;
	while(b != NULL){
		a->n = c;
		c = a;
		a = b;
		b = b->n;
	}
}

void main(){
	node a, b, c;
	a.val = 5;
	b.val = 3;
	c.val = 1;

	a.n = &b;
	b.n = &c;
	c.n = NULL;

	node *d = rev(&a);
	printf("%d ", d->val);
	d=d->n;
	printf("%d ", d->val);
	d=d->n;
	printf("%d ", d->val);
}
