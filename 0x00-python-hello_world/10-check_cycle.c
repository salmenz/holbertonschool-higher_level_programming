#include "lists.h"

/**
 * check_cycle - Checks a singly linked lists for a cycle
 * @list: The list
 *
 * Return: 1 if there is a cycle else 0.
 */

int check_cycle(listint_t *list)
{
listint_t *c = list;
listint_t *n = list;

if (c == NULL || n == NULL)
return (0);
while (c && (c = c->next))
{
if (c == n)
return (1);
c = c->next;
if (c == n)
return (1);
n = n->next;
}
return (0);
}
