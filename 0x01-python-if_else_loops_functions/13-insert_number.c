#include "lists.h"

/**
 * insert_node - insert a node in sorted list
 * @head: input list
 * @number: input number
 * Return: return the new node, NULL otherwise
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *curr, *fast;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);

	newNode->n = number;
	if (*head == NULL)
	{
		newNode->next = NULL;
		return (*head = newNode);
	}
	curr = *head;
	fast = (*head)->next;
	if (curr->n > number)
	{
		newNode->next = curr;
		return (*head = newNode);
	}

	while (curr && fast)
	{
        if (curr->n ==   number || fast->n == number)
            return (NULL);
		if (curr->n < number && fast->n > number)
		{
			curr->next = newNode;
			newNode->next = fast;
			return (newNode);
		}

		curr = curr->next;
		fast = fast->next;
	}

	fast->next = newNode;
	newNode->next = NULL;

	return (newNode);
}
