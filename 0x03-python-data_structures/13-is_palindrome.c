#include "lists.h"
#include <stdlib.h>

/**
 * reverse_array - reverses the content of an array of integers
 * @a: int array to reverse
 * @n: number of elements in the array
 * Return: concatenated string
 */

void reverse_array(int *a, int n)
{
        int *begin = a;
        int *end;
        int hold = 0;

        end = a + n - 1;
        for (; begin < end; begin++, end--)
        {
                hold = *end;
                *end = *begin;
                *begin = hold;
        }
}

/**
 * is_palindrome - Return 1  if palindrome, 0 if not
 * @head: linked list
 * Return: Return 1  if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
        int size, *list, *rev;
        listint_t *copy = *head;

        if (!head || !copy)
                return (0);
        if (!copy->next)
                return (1);

        list = malloc(sizeof(int *));
        if (!list)
                return (0);
        rev = malloc(sizeof(int *));
        if (!rev)
                return (0);
        for (size = 0; copy; copy = copy->next, size++)
                list[size] = copy->n;

        list = rev;
        reverse_array(rev, size);
        if (list == rev)
                return (1);
        return (0);
}