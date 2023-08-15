#include "lists.h"
/**
 * is_palindrome - check if a list palindrome
 * @head: input list
 * Return: 1 if list palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *curr, *reversed, *rev;

	if (!head || !*head)
		return (1);

	curr = *head;
	reversed = reverse_listint(head);
	rev = reversed;

	while (curr)
	{
		if (curr != rev)
			return (0);

		curr = curr->next;
		rev = rev->next;
	}

	return (1);
}
/**
 * reverse_listint - a function that reverses a listint_t linked list.
 * @head: input list
 * Prototype: listint_t *reverse_listint(listint_t **head);
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prevNode, *nextNode, *currNode;

	if (!head || !*head)
		return (NULL);

	currNode = *head;
	prevNode = NULL;
	while (currNode)
	{
		nextNode = currNode->next;
		currNode->next = prevNode;
		prevNode = currNode;
		currNode = nextNode;
	}
	*head = prevNode;

	return (*head);
}
