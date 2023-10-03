#include "lists.h"

/**
 * listint_t *insert_node - inserts a new node at the
 * beginning of a listint_t list
 * @head: pointer to the head of the list
 * @number: the number to insert
 * Return: the address of the new element, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = *head;
	*head = new;

	return (new);
}
