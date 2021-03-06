#include <stdio.h>

#include <sgx_urts.h>

#include "app.h"
#include "sgx_utils.h"

#include "enclave_u.h"

/* Global EID shared by multiple threads */
sgx_enclave_id_t global_eid = 0;

/* OCall functions */
void ocall_print_string( const char *str )
{
	/* Proxy/Bridge will check the length and null-terminate 
	 * the input string to prevent buffer overflow. 
	 */
	printf( "%s", str );
}

/* Application entry */
int SGX_CDECL main( int argc, char *argv[] )
{
	(void)(argc);
	(void)(argv);

	sgx_status_t ret = SGX_ERROR_UNEXPECTED;
    
	/* Call sgx_create_enclave to initialize an enclave instance */
	/* Debug Support: set 2nd parameter to 1 */
	ret = sgx_create_enclave( ENCLAVE_FILENAME, SGX_DEBUG_FLAG, NULL, NULL, &global_eid, NULL) ;
	if ( ret != SGX_SUCCESS ) {
		print_error_message( ret );
		return -1;
	}

    ret = SGX_ERROR_UNEXPECTED;
    int ecall_return = 0;

	ret = ecall_print_secret( global_eid, &ecall_return );
	if ( ret != SGX_SUCCESS ) {
		print_error_message(ret);
	}

	/* Destroy the enclave */
	sgx_destroy_enclave( global_eid );

	return ecall_return;
}

