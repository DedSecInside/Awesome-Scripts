#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long int n;
    cout<<"\n\n\t\tWelcome to \"CATCH THE CAT GAME!!!\"\n\n\t\tThis Game is Made by Rahul Kocheta.\n\n\t\t\tTerms and conditions:\nDon't try to copy the code, just try to develop your own (It's fun Man!!).\nP.S. This game is based on a very popular puzzle. Hope you will enjoy this game.:-)\n\nSO, LETS CATCH THIS CAT!!!.................\n\n";
    while(true)
    {
        cout<<"Select your difficulty level:\n1. EASY\n2. MEDIUM\n3. HARD\n\nYour Choice:\t";
        string s;
        cin>>s;
        while(s!="1" && s!="2" && s!="3")
        {
            cout<<"Answer accepted only as numbers from 1, 2 or 3.\nEnter again\n\n";
            cin>>s;
        }
        if(s=="1")
        {
            cout<<"\nYou have selected EASY mode.\n";
            n=4;

        }
        else if(s=="2")
        {
            cout<<"\nYou have selected MEDIUM mode.\n";
            n=7;
        }
        else if(s=="3")
        {
            cout<<"\nYou have selected HARD mode.\n";
            n=10;
        }
        cout<<"\nA cat is hiding in one of "<<n<<" BOXES that are lined up in a row. The boxes are numbered 1 to "<<n<<".\nEach night the cat hides in an adjacent box, exactly one number away.\nEach morning you can open a single box to find the cat.\nCan you win this game of hide and seek?\n\n";
        cout<<"\tThis cat can be in any of the below boxes ---->>>>\tCAT\n\n\t\t";
        for(int i=0;i<n;i++)
        {
            cout<<"BOX-"<<i+1<<"\t";
        }
        cout<<"\n\nTry to figure out the strategy to catch this CAT within "<<(n-2)*2<<" tries!!!\n\n";
        srand(time(0));
        long long int i=(n-2)*2,guess,pos,initial=(rand()%n + 1),jump;
        pos=initial;

        while(true)
        {
            cout<<"\t\t\t\tTries remaining: "<<i<<"\n\nYour guess (Answer acceptable only between 1 to "<<n<<" ):\t";
            cin>>guess;
            srand(time(0));
            jump=(rand()%2 +1);
            if(jump==1)
            {
                pos--;
                if(pos==0)
                {
                    pos+=2;
                }
            }
            else
            {
                pos++;
                if(pos==n+1)
                {
                    pos=pos-2;
                }
            }
            if(guess==pos)
            {
                cout<<"\n\n\t\tWOAH!!!....You Are A True Genius Man!!!\n\t\tYou caught that CAT. :-)\n\n";
                break;
            }
            else
            {
                i--;
                cout<<"\n\tNOPE!\tNot in this one!\n\n";
                if(i==0)
                {
                    cout<<"\t\tSorry to say but you failed. The CAT escaped. :-(\n\n";
                    break;
                }
            }
        }
        cout<<"Wanna Play Again? (Type 'Y' for a YES or 'N' for a NO):\t";
        char ans='K';
        cin>>ans;
        while(ans!='Y' && ans!='N')
        {
            cout<<"'Y' or 'N'? Your answer:\t";
            cin>>ans;
        }
        if(ans=='N')
        {
            cout<<"\n\t\t Thanks For Playing. :-)\n\n";
            break;
        }
        else
        {
            cout<<"\n\nHere you go again..........:-D\n\n";
        }
    }
    return 0;
}
