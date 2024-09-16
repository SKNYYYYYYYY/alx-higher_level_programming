#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *p = *head;
    listint_t *q = *head;
    listint_t *start_second, *prev = NULL, *current, *next = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return 1; 
    // Find the middle of the list
    while (p != NULL && p->next != NULL)
    {
        p = p->next->next;
        q = q->next;
    }

    // Handle odd-length lists
    if (p != NULL) 
    {
        q = q->next;
    }

    // Reverse the second half of the list
    start_second = q;
    current = start_second;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    start_second = prev;
    
    p = *head;
    while (start_second != NULL)
    {
        if (p->n != start_second->n)
        {
            return (0);
        }
        p = p->next;
        start_second = start_second->next;
    }
    return (1);
}