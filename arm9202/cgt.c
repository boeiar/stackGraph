#include "cgt.h"

static int ia[]={0,1,2,3,9,5,6,7,8,};
int cgt1(int i)
{
  cgt2(ia[i]);
  return 0;
}

int cgt2(int i)
{
  return i + 5;
}
