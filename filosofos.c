#define NUMFILO 5
semaphore hashi [5]; 
int filosofos_na_sala = 0;

task filosofo(int i) { 

    entrar_na_sala();

    int dir = 1;
    int esq = (1+1) % NUMFILO;

    while(1){
        meditar ();
        down (hashi [dir]);
        down (hashi [esq]);
        comer () ;
        up (hashi [dir]);
        up (hashi [esq]);
    }

    sair_da_sala ();
} 

void entrar_na_sala() {
    mutex_lock(mutex);
        while(filosofos_na_sala == NUMFILO-1)
            cond_wait(sala_nao_cheia, mutex);
        filosofos_na_sala++;
    mutex_unlock(mutex);
}

void sair_da_sala() {
    mutex_lock(mutex);
        filosofos_na_sala--;
        pthread_cond_signal( &condition );
    mutex_unlock(mutex);
}