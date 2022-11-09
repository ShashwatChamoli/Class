#include<iostream>
using namespace std;
int main()
{
int a=5;
char b[10];
cout<<&a<<endl;
cout<<&b<<endl;
int *y;
y=&a;
cout<<*y;
return 0;
}
