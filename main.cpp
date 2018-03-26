#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float s;
    float x = 1.0;
    float a ;
    float b ;
    int counter = 0;
    cout<<"Enter the number: "<<endl;
    cin>>s;


    if (s<0){
        cout<<"Sorry, The number is negative"<<endl;
    }
    else if (s==0){
        cout<<"The square root is 0"<<endl;

}
    else {
        while(counter <= 7) {
                a = (s - x * x) / (2 * x);
                b = x + a;
                x = b - (a * a) / (2 * b);
                counter=counter + 1 ;

        }




    cout<<"The square root using Bakhshali's method Equal:  "<< abs(x) <<endl;
    cout<<"The real square root is: " << sqrt(s) <<endl;

}


    return 0;
}
