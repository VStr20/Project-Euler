#include<iostream>
using namespace std;

int main(){
   int n;
   cin>>n;
   int sum=0;
   int sum_square=0;
   for(int i=1;i<=n;i++){
      sum=sum+i;
    }
    long long int square_sum=sum*sum;
   for(int j=1;j<=n;j++){
     sum_square=sum_square+j*j;
    }
    long long int answer=square_sum-sum_square;
    cout<<answer<<endl;

}
