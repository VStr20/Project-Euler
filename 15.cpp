#include<iostream>
using namespace std;

long double factorial(double a){
   long double product=1;
   for(double i=1;i<=a;i++){
      product=product*i;
    }
   return product;
}
int main(){

   long double a;
   cin>>a;
   long double ans = factorial(2*a)/(factorial(a)*factorial(a));
   cout<<ans<<endl;
}

/*double a,b,n,fac=1;
cin >>n ;

for (double i=1;i<=a;i++){
    fac=fac*i;
    }
 */
