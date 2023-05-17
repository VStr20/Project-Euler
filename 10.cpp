#include<iostream>
using namespace std;

bool prime(int a){
   if(a==1 || a==0) return false;

   for(int i=2;i<a;i++){
       if(a%i==0){
          return false;
        }
    }
    return true;
}

int main(){
   long long int n;
   cin>>n;
   long long int sum=0;

   for(int j=2;j<=n;j++){
     if(prime(j)){
        sum=sum+j;
      }
    }

    cout<<sum<<endl;
}
