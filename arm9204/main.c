#include "main.h"
int f0(int i){
  f1(1);
  g1(1);
  int_array_ret(0);
}
int f1(int i){
  f2(2);
  g2(2);
  int_array_ret(1);
}
int f2(int i){
  f3(3);
  g3(3);
  int_array_ret(2);
}
int f3(int i){
  f4(4);
  g4(4);
  g1(1);
  int_array_ret(3);
}
int f4(int i){
  f5(5);
  g5(5);
  int_array_ret(4);
}
int f5(int i){
  f6(6);
  g6(6);
  int_array_ret(5);
}
int f6(int i){
  f7(7);
  g7(7);
  int_array_ret(6);
}
int f7(int i){
  f8(8);
  g8(8);
  int_array_ret(7);
}
int f8(int i){
  f9(9);
  g9(9);
  int_array_ret(8);
}
int f9(int i){
  int_array_ret(9);
}


int g0(int i){
  g1(1);
 int_array_ret(0);
 }

int g1(int i){
  g2(2);  
  int_array_ret(1);
}
int g2(int i){
  g3(3);
  int_array_ret(2);
}
int g3(int i){
  g4(4);
  int_array_ret(3);
}
int g4(int i){
  g5(5);
  int_array_ret(4);
}
int g5(int i){
  g6(6);
  int_array_ret(5);
}
int g6(int i){
  g7(7);
  int_array_ret(6);
}
int g7(int i){
  g8(9);
  int_array_ret(7);
}
int g8(int i){
  g9(9);
  int_array_ret(8);
}
int g9(int i){
  int_array_ret(9);
}

int main(){
  f0(99);
  return 0;
}

