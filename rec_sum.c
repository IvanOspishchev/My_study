#include <stdio.h>
#include <string.h>

int		lenarr(int *arr)
{
	int i;

	i = 0;
	while (*arr++)
		i++;
	return (i);
}

int 	ft_rec_sum(int arr)
{
	int i;
	int len;
	int *p_arr;

	p_arr = &arr;
	i = 0;
	len = lenarr(p_arr);
	if (len == 1)
		return (*p_arr);
	else
		return(*p_arr + ft_rec_sum(*p_arr + 1));
}

int main()
{
	int arr[] = {1, 2, 3, 4};
	

	printf("%d\n,%d\n", ft_rec_sum(*arr), lenarr(arr));
} 
