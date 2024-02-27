#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
/**
 * execute_command - function that forks and exectes a command
 * @command: pointer pointing to an array of strings that contain the command
 *
 */
void execute_command(char *command[])
{
	pid_t process;
	int status;

	process = fork();
	if (process == -1)
	{
		perror("fork failed\n");
		exit(EXIT_FAILURE);
	}
	else if (process == 0)
	{
		execvp(command[0], command);
		perror("Execution failed\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		waitpid(process, &status, 0);
	}
}
/**
 * main - main function
 * @argc: number of argument passed
 * @argv: array of pointer to an array of strings of argruments
 *
 * Return: 0 on success
 */
int main(int argc, char *argv[])
{
	char *commit_[5];
	char *commit;
	char *git_add[] = {"git", "add", ".", NULL};
	char *git_push[] = {"git", "push", NULL};
	int i;

	if (argc != 2)
	{
		fprintf(stderr, "Error: Please input one argument after git__ or use \"\"\n");
		return (1);
	}
	commit = argv[1];
	if (commit == NULL || strcmp(commit, " ") == 0)
	{
		fprintf(stderr, "Commit should not be empty\n");
		return (1);
	}
	for (i = 0; commit[i] != '\0'; i++)
	{
		if (!((commit[i] >= 'A' && commit[i] <= 'Z') ||
					(commit[i] >= 'a' && commit[i] <= 'z') ||
					(commit[i] >= '0' && commit[i] <= '9')))
		{
			fprintf(stderr, "Commit should be Alphabet messages only\n");
			return (1);
		}
	}
	commit_[0] = "git";
	commit_[1] = "commit";
	commit_[2] = "-m";
	commit_[3] = commit;
	commit_[4] = NULL;
	execute_command(git_add);
	execute_command(commit_);
	execute_command(git_push);
	return (0);
}
