#include <stdio.h>
int main(int argc, char *argv[])
{
	execvp("/bin/sh","/bin/sh",NULL);
	return 0;
}
