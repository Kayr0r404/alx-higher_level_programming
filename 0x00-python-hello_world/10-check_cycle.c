#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a cycle exist in a list
 * @list: input list
 * Return: 0 if no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *curr, *ahead;

	if (!list)
		return (0);

	curr = list, ahead = list;

	while (ahead && ahead->next)
	{
		curr = curr->next;
		ahead = ahead->next->next;

		if (curr == ahead)
			return (1);
	}

	return (0);
}
