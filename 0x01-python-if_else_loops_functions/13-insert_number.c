#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node so that linked list remains sorted
 * @head: pointer to the beginning of linked list
 * @number: value for n
 * Return: address of new node or NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *hold = *head;
	unsigned int i = 0;

	if (!(hold) || (*hold).n > number) /* add to beginning of linked list*/
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		(*new).n = number;
		(*new).next = *head;

		*head = new;

		return (*head);
	}

	while (hold)
	{
		if (!((*hold).next) || (*hold).next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			(*new).n = number;
			(*new).next = (*hold).next;
			(*hold).next = new;
			return (new);
		}
		hold = (*hold).next;
		i++;
	}

	return (NULL);
}
