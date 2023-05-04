#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
    /*
    int num;
    string str = "7";
    cout << "string - " << str << endl;
    num = stoi(str);
    cout <<"numero - "<< num << endl;
    */
   ofstream write;
   ifstream read;
   read.open("imagem.ppm");
   write.open("imagemSaida.ppm");
  
    string tipo = "", width = "", heigt = "", RGB = "",line = "";
    read >> tipo;
    read >> width;
    read >> heigt;
    read >> RGB;

    string red = "", gree = "", blue = "" ;
    int intR = 0, intG = 0, intB = 0 ;

    write << tipo << endl;
    write << width << " " << heigt<< endl;
    write << RGB << endl;

    while (!read.eof())
        {
            read >> red;
            intR = stoi(red);
            write << intR << endl;

            read >> gree;
            intG = stoi(gree);
            write << intG << endl;

            read >> blue;
            intB = stoi(blue);
            write << intB << endl;

            write << endl;
        }

    /*if (read.is_open()){
        while (getline(read, line))
        {
            if(!read.eof()){
             write << line << endl;
            }
        }
        
    }*/

    
   /*
    file << "p3"<<endl;
    file << "250 250"<<endl;
    file << "255"<<endl;

    for (int i = 0; i < 250; i++)
    {
        for (int j = 0; j < 250; j++)
        {
            file << j << " " << j << " " << j << endl;
        }
    }*/
    
    write.close();
    read.close();
    return 0;
}
