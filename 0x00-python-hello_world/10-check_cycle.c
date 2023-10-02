#include "lists.h"
/**
 * check_cycle - checks if SLL has a cycle
 * @list: head
 * Return: 1 is cycle is present, 0 if null
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
