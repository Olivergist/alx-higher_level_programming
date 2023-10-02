#ifndef VICTOR_H
#define VICTOR_H

#include <stddef.h>

/**
 *struct listint_s - define the structure
 *@v: int value stored
 *@forward: the next node
 *Description: node structure for singly linked
 *
 */

typedef struct listint_s
{
	int v;
	struct listint_s *forward;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int v);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* VICTOR_H */
