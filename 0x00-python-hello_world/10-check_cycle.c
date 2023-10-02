#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
	{
		return (0);
	}

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}

/**
 * main - Free mallac
 * Return: 0
 */
int main(void)

{
	listint_t *head = malloc(sizeof(listint_t));
	listint_t *second = malloc(sizeof(listint_t));
	listint_t *third = malloc(sizeof(listint_t));

	head->n = 1;
	head->next = second;

	second->n = 2;
	second->next = third;

	third->n = 3;
	third->next = head;

	int hasCycle = check_cycle(head);

	if (hasCycle)
	{
		printf("The linked list has a cycle.\n");
	}

	else

	{
		printf("The linked list does not have a cycle.\n");
	}

	free(head);
	free(second);
	free(third);

	return (0);
}
