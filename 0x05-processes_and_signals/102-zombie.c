#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 *main - create zombie processes
 *Return: 0 if sucessful
 */
int main(void)
{
	int itera = 0;
	pid_t nino;

	while (itera < 5)
	{
		nino = fork();
		if (nino > 0)
		{
			sleep(1);
		}
		else
		{
			exit(0);
		}
		printf("Zombie process created, PID: %d\n", nino);
		itera++;
	}
	infinite_while();
	return (0);

}
/**
 *infinite_while - The name explains itself
 *Return: 0 if sucessful
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
