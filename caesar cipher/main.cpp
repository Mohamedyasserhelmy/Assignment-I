//ASSIGNMENT :2
//TASK 2 : CAESAR ENCRYPTION AND DECYPTION
// MOHAMED YASSER HELMY
//FCI CAIRO UNIVERSITY




#include <bits/stdc++.h>
#include <string>
using namespace std;

int main()
{
    int choice, length, shift, s;
    string input ;
    char X;

    cout<<"Ahlan ya user ya habibi "<<endl;
    cout<<"What do you want to do today? "<<endl;
    cout<<"1-Cipher a message "<<endl;
    cout<<"2-Decipher a message "<<endl;
    cout<<"3-End"<<endl;
    cout<<"Enter your choice: ";
    cin>>choice;

    if(choice==2){
            cout<<"Enter your ENCRYPTED TEXT : ";
            cin.ignore();
            getline(cin,input);
            length=(int)input.length();
            cout<<"Enter the number of shifts : ";
            cin>>shift;

            for(int i=0; i<length;i++){
                    if(isupper(input[i])){

                        s=(int)input[i]-65;
                        X=((s-shift)%26) +65 ;
                        cout<<X<<" ";
                    }
                    else
                        s=(int)input[i]-97;
                        X=((s-shift)%26) +97;
                        cout<<X<<" ";
    }


    }

     if (choice==1){
            cout<<"Enter your plain text: " ;
            cin.ignore();
            getline(cin,input);
            length=(int)input.length();
            cout<<"Enter the number of shifts : ";
            cin>>shift;

            for(int j=0;j<length;j++){

                    if(isupper(input[j])){
                            s=(int)input[j]-65;
                            X=(s+shift) %26 +65;
                            cout<<X<<" " ;
                    }

                    else {
                            s=(int)input[j]-97;
                            X=(s+shift)%26 +97;
                            cout<<X<<" ";
                    }
    }

    }


     if(choice ==3 ){


            cout<<"Good bye , see u soon "<<endl;
    }

    return 0;
}
