 /********************************************************************
 * abracadabra.c - este programa deve ser completado para criar cinco
 * threads, cada uma podendo escrever apenas uma das letras da palavra
 * ABRACADABRA na tela (A, B, C, D e R). As threads devem usar uma
 * variavel de exclusao mutua e uma variavel de condicao para
 * fazerem a coordenacao necessaria para gerar o resultado esperado.
 ********************************************************************/

/* VOCE DEVE COMPLETAR O PROGRAMA APENAS ACRESCENTANDO NOVAS LINHAS
 * DE CODIGO. NAO ALTERE NADA NAS LINHAS JA EXISTENTES. O SISTEMA
 * DE CORRECAO DEPENDE DA EXISTENCIA DAS OUTRAS LINHAS PARA QUE A
 * AVALIACAO SEJA FEITA. PROGRAMAS QUE ALTEREM ALGUMA LINHA JA 
 * EXISTENTE SERAO PENALIZADOS, MESMO SE FUNCIONAREM CORRETAMENTE.  
 */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


/* As variaveis a seguir deverao ser usadas para implementar a sincronizacao
 * entre as threads que escrevem cada letra: uma variavel de exclusao mutua,
 * uma variavel de condicao e uma variavel para indicar qual thread deve
 * executar em seguida.
 * Não e permitido acrescentar outras variaveis globais, expecialmente 
 * para fins de sincronizacao.
 */

pthread_mutex_t mutex;
pthread_cond_t  condition;
int next_letter;

/*
 * As contantes a seguir facilitam a identificacao as funcoes que vao 
 * escrever cada letra. Elas devem ser usadas para os parametros my_letter
 * e to_letter nas duas funcoes a seguir.
 */

#define LETTER_A 0
#define LETTER_B 1
#define LETTER_C 2
#define LETTER_D 3
#define LETTER_R 4

/* As funcoes a seguir fazem a sincronizacao */

#define DONE 1     /* usado p/ indicar quando uma letra nao sera mais usada */
#define NOT_DONE 0 /* o inverso, isto e, a letra ainda sera usada de novo */

void from_letter_to_letter( int my_letter, int to_letter, int done )
{   
    /* Esta funcao e chamada quando a thread que escreveu a letra "my_letter"
     * quer passar a vez para a thread que vai escrever a letra "to_letter".
     * Se a thread que acabou de escrever ja terminou sua parte (nao tem que
     * escrever mais nada), "done" deve ser verdadeiro.
     * Se, por outro lado, a thread que esta "passando a vez" ainda precisa
     * esperar pela sua vez de novo, "done" deve ser falso.
     */

    pthread_mutex_lock( &mutex );

    next_letter = to_letter;
    pthread_cond_broadcast( &condition );
    if(done == 0) {
        while(next_letter != my_letter){
            pthread_cond_wait( &condition, &mutex ); 
        }      
    }

    pthread_mutex_unlock( & mutex );
}

void wait_for_letter( int my_letter )
{
    /* Esta funcao e chamada por toda thread ao comecar, para esperar
     * ate que seja sua vez de escrever pela primeira vez.
     */
    while(next_letter != my_letter){
        
    }
}

void *thread_a(void* not_used)
{
    // printf("Thread A\n");
    wait_for_letter( LETTER_A );
    printf("A");
    from_letter_to_letter( LETTER_A, LETTER_B, NOT_DONE );
    printf("A");
    /* complete o codigo para cada thread */
    from_letter_to_letter( LETTER_A, LETTER_C, NOT_DONE );
    printf("A");
    from_letter_to_letter( LETTER_A, LETTER_D, NOT_DONE );
    printf("A");
    from_letter_to_letter( LETTER_A, LETTER_B, NOT_DONE );
    printf("A");
    pthread_exit(NULL);
}

void *thread_b(void* not_used)
{
    /* complete o codigo para cada thread */
    // printf("Thread B\n");
    wait_for_letter( LETTER_B );
    printf("B");
    from_letter_to_letter( LETTER_B, LETTER_R, NOT_DONE );
    printf("B");
    from_letter_to_letter( LETTER_B, LETTER_R, DONE );
    pthread_exit(NULL);
}

void *thread_c(void* not_used)
{
    /* complete o codigo para cada thread */
    // printf("Thread C\n");
    wait_for_letter( LETTER_C );
    printf("C");
    from_letter_to_letter( LETTER_C, LETTER_A, DONE );
    pthread_exit(NULL);
}

void *thread_d(void* not_used)
{
    /* complete o codigo para cada thread */
    // printf("Thread D\n");
    wait_for_letter( LETTER_D );
    printf("D");
    from_letter_to_letter( LETTER_D, LETTER_A, DONE );
    pthread_exit(NULL);
}

void *thread_r(void* not_used)
{
    /* complete o codigo para cada thread */
    // printf("Thread R\n");
    wait_for_letter( LETTER_R );
    printf("R");
    from_letter_to_letter( LETTER_R, LETTER_A, NOT_DONE );
    printf("R");
    from_letter_to_letter( LETTER_R, LETTER_A, DONE );
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
    int NUM_THREADS = 5;
    pthread_t threads[NUM_THREADS];

    /* Defina as demais variaveis locais de main como você precisar */
    int rc;

    /* Nao se esqueca de inicializar as variaveis de sincronizacao */
    pthread_mutex_init(&mutex,NULL);
    pthread_cond_init(&condition, NULL);

    /* Crie as cinco threads e depois espere pelo fim de cada uma. */
    //garantir que o next letter nao é nenhuma das letras para nao começar um processo antes da hora
    next_letter = 5;

    // printf("main: criando thread A\n");
    rc = pthread_create(&threads[0], NULL, thread_a, NULL);
    if (rc){
        printf("ERROR; return code from pthread_create() is %d\n", rc);
        exit(-1);
    }

    // printf("main: criando thread B\n");
    rc = pthread_create(&threads[1], NULL, thread_b, NULL);
    if (rc){
        printf("ERROR; return code from pthread_create() is %d\n", rc);
        exit(-1);
    }

    // printf("main: criando thread C\n");
    rc = pthread_create(&threads[2], NULL, thread_c, NULL);
    if (rc){
        printf("ERROR; return code from pthread_create() is %d\n", rc);
        exit(-1);
    }

    // printf("main: criando thread D\n");
    rc = pthread_create(&threads[3], NULL, thread_d, NULL);
    if (rc){
        printf("ERROR; return code from pthread_create() is %d\n", rc);
        exit(-1);
    }

    // printf("main: criando thread R\n");
    rc = pthread_create(&threads[4], NULL, thread_r, NULL);
    if (rc){
        printf("ERROR; return code from pthread_create() is %d\n", rc);
        exit(-1);
    }

    pthread_mutex_lock(&mutex);
    next_letter = LETTER_A;
    pthread_mutex_unlock(&mutex);

    for(int t=0;t<NUM_THREADS;t++){
        pthread_join(threads[t], NULL);
    }

    printf("\n"); /* So para quebrar a linha ao fim da palavra. */

    /* INCLUA MAIS UM printf AQUI PARA ESCREVER SEU NOME AO FINAL */
    printf("Giovanna Louzi Bellonia\n");

    pthread_exit(NULL);
}