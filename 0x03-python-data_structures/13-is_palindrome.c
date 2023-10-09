#include "lists.h"
#include <stdlib.h>

/**
 * reverse_linked_list - Reverses a linked list in place.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_linked_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;

	/*Find the middle of the linked list using slow and fast pointers*/
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/*Reverse the second half of the linked list*/
	second_half = reverse_linked_list(&slow);

	/*Compare the first and second halves for palindrome*/
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}

	return (1);
}
