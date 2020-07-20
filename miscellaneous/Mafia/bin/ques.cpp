#include<bits/stdc++.h>
#include <signal.h>
#include <unistd.h>
using namespace std;

char decide(int val1, int val2){
	if(val1>val2)
		return 'G';
	else if(val2>val1)
		return 'L';
	else
		return 'E';
}

void exitfunc(int sig)
{
    exit(0);
}

void sleepcp(int milli) {
   // Cross-platform sleep function
   clock_t end_time;
   end_time = clock() + milli * CLOCKS_PER_SEC/1000;
   while (clock() < end_time) {
      //blank loop for waiting
   }
}

int main(){

	(SIGALRM, exitfunc);
    alarm(30);

	random_device rd;
	mt19937 mt(rd());
	uniform_int_distribution<int>maxi(1,1000000);

	string flag="csictf{y0u_ar5_t8e_k!ng_0f_rAnd0mne55}";

	int arr[300];
	for(int i=0;i<300;i++)
		arr[i]=0;
	int queries=0;
	int max_ele=maxi(mt);
	uniform_int_distribution<int>num(1,max(2,max_ele)-1);
	int currfilled=0;


	while(queries<=1000){
		int choice,pos,val,inp;
		cin>>choice;
		alarm(20);
		char ret;
		if(choice==1){
			cin>>pos>>val;
			alarm(20);
			if(pos<1 or pos>300){
				exit(0);
			}
			if(val<1 or val>1000000){
				exit(0);
			}
			queries+=1;
			if(arr[pos-1]==0){
				if(currfilled==290){
					arr[pos-1]=max_ele;
					currfilled+=1;
					ret=decide(arr[pos-1],val);
					sleepcp(3);
					cout<<ret<<endl;
				}
				else{
					arr[pos-1]=num(mt);
					currfilled+=1;
					ret=decide(arr[pos-1],val);
					sleepcp(3);
					cout<<ret<<endl;
				}
			}
			else{
				ret=decide(arr[pos-1],val);
				sleepcp(3);
				cout<<ret<<endl;
			}
		}
		else if(choice==2){
			cin>>inp;
			if(inp==max_ele){
				cout<<"Congratulations you guessed it right, here is the reward: "<<flag<<endl;;
			}
			else{
				cout<<"Oops, looks like you missed something, try again!"<<endl;
			}
			exit(0);
		}
		else{
			exit(0);
		}
	}

	int choice,inp;
	cin>>choice;
	if(choice==2){
		cin>>inp;
		if(inp==max_ele){
			cout<<"Congratulations you guessed it right, here is the reward: "<<flag<<endl;;
		}
		else{
			cout<<"Oops, looks like you missed something, try again!"<<endl;
		}
		exit(0);
	}
	else{
		exit(0);
	}

	
	return 0;
}
