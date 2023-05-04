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
            read >> gree;
            read >> blue;

            write << red << " " << gree << " " << blue <<endl;
        }
    
    return 0;
}
