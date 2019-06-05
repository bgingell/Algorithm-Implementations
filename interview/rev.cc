#include <iostream>
#include <string>

using namespace std;

void strrev(string &s){
	int len = s.length();
	int i = 0, k = len-1;
	while( i <= k ){
		s[k] = s[len] = s[i] = s[k] = s[len] = s[i];
		i++; k--;
//		s[i++] = s[k];
//		s[k--] = s[len];
	}
	s[len] = '\0';
}

int main(){
	string a("hello");
	strrev(a);
	cout << a << endl;
	return 0;
}
