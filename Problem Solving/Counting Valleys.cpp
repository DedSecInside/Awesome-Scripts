#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {

int prev=0,current=0,count=0;

for(int i=0;i<n;i++){

    prev=current;

    if(s[i]=='U')
    current++;
    if(s[i]=='D')
    current--;

    if(current==0 && prev<0){
        count++;
    }

    
}
return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}

