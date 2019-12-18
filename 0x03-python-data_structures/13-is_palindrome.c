#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - Tests if thr=e list is a palindrome
 * @head: The head
 *
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
listint_t *f = *head;
listint_t *d = *head;
int l = 0, i = 0, j = 0;

if (*head == NULL)
return (1);
while (f->next != NULL)
{
f = f->next;
l++;
}
if (l == 1)
return (0);
if (d->n == f->n)
{
while (i <= (l / 2))
{
f = *head;
for (j = 0; j < (l - i); j++)
f = f->next;
if (d->n != f->n)
return (0);
i++;
d = d->next;
}
}
return (1);
}
