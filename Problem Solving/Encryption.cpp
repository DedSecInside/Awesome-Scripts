#include <bits/stdc++.h>
#include <cmath>

using namespace std;

// Complete the encryption function below.
string encryption(string s) {

int length = s.length();
int sqrt_length= pow(length,0.5);

int rows = sqrt_length;
int cols= sqrt_length;
cout<< length<< " " << sqrt_length<< " " << rows<< "" << cols;
while(rows*cols<length){

if(cols<=rows)
cols++;
else
rows++;

}
cout<<endl <<cols;
int index = 0;
char Text [rows][cols] ; 

for(int i=0;i<rows;i++){

    for(int j=0;j<cols;j++){

        if(s[index]!='\0'){}
        Text[i][j] = s[index];
        index++;

        
    }
    }
    string output = "";
    for(int i=0;i<cols;i++){

        for(int j=0;j<rows;j++){
            if(Text[j][i] != '\0'){
            output = output + Text[j][i];
            }
        }
        output = output + " ";
    }
    cout<<output;

return output;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = encryption(s);

    fout << result << "\n";

    fout.close();

    return 0;
}

