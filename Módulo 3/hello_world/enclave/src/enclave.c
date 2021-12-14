#include <stdio.h>      /* vsprintf */
#include <stdarg.h>
#include <string.h>

#include "enclave.h"
#include "enclave_t.h"  /* ocall_print_string */

const char enclave_secret[] = "Hello World!";

/* 
 * printf: 
 *   Invokes OCALL to display the enclave buffer to the terminal.
 */
int printf( const char *fmt, ... )
{
	char buf[BUFSIZ] = {'\0'};
	va_list ap;

	va_start( ap, fmt );
	vsnprintf(buf, BUFSIZ, fmt, ap);
	va_end( ap );

	ocall_print_string( buf );

    return ( (int) strnlen( buf, BUFSIZ - 1 ) + 1 );
}

int ecall_print_secret()
{
	printf( "%s\n", enclave_secret);
	return 0;
}

