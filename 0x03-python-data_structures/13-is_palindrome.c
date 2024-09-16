#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *midnode = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_of_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		midnode = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_of_slow->next = NULL;
	reverse(&second_half);
	is_palindrome = compare_lists(*head, second_half);

	reverse(&second_half);

	if (midnode != NULL)
	{
		prev_of_slow->next = midnode;
		midnode->next = second_half;
	}
	else
		prev_of_slow->next = second_half;

	return (is_palindrome);
}

/**
 * reverse - Reverses a linked list
 * @head_ref: Pointer to pointer of first node of listint_t list
 */
void reverse(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}

/**
 * compare_lists - Compares two linked lists
 * @head1: Pointer to the first list
 * @head2: Pointer to the second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}
