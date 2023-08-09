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
	listint_t *curr = list, *head = list;

	while (curr != NULL)
	{
		curr = curr->next;
		if (curr == head)
			return (1);
	}

	if (!curr)
		return (0);

	return (1);
}
