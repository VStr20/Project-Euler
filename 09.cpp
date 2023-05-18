#include<iostream>
using namespace std;

int main(){
   for(int a=0;a<1001;a++){
      for(int b=0;b<1001;b++){
         for(int c=0;c<1001;c++){
            if(a+b+c==1000 && a*a + b*b == c*c){
               cout<<a*b*c<<endl;
               cout<<a<<endl<<b<<endl<<c<<endl;

            }
         }
        }
    }

}
