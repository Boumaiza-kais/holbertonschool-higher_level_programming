#include "lists.h"
/**
 * check_cycle - check a linked list to is there a cycles in it
 * @list: listint_t type
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
listint_t *temp, *new;
temp = list;
new = list;
while (temp != NULL && new != NULL && new->next != NULL)
{
new = new->next->next;
temp = temp->next;
if (new == temp)
return (1);
}
return (0);
}
