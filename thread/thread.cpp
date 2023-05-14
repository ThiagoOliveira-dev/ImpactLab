#include <iostream>
#include <thread>
#include <mutex>

using namespace std;
mutex mtx;


void print(){
    unique_lock<mutex> lock(mtx);
    cout << "meu nome ";
    lock.unlock();
     
}
void print2(){
    
        cout << "sobre nome ";  
}


int main(){

    thread t(print);
    cout << "ufam ";
    t.join();
   
    thread t2(print2);
    cout << "icomp ";
    t2.join();
    
    return 0;
}
 