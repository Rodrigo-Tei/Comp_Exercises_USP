#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){

double pontos_apostador, pontos_banca, carta, teto, rifa, caixa;
int N, e;
int derrotas, seed, estrelas, apostador, banca;

pontos_apostador = 0;
pontos_banca = 0;
derrotas = 0;

printf("Digite um valor inteiro: ");
scanf("%d", &seed);
caixa = semente (seed);

/*     jogo acontece aqui     */

for (teto = 0.5; teto < 8; teto = teto + 0.5){
	for (N = 0; N < 10000; N++){
		while(apostador == TRUE || banca == TRUE){

/*  estrategia do apostador   */

			if (pontos_apostador < teto){
		

			rifa = 9821.0 * RaizCubica(caixa) + 0.211327;
			caixa = rifa - chao(rifa);
			carta = chao(caixa*10 - 1);
			pontos_apostador = pontos_apostador + carta;
		
			}
			
			else 
				apostador = FALSE;

/*   estrategia da banca    */
		
			if (pontos_apostador < 7.5 && pontos_banca < 7.5){

			rifa = 9821.0 * RaizCubica(caixa) + 0.211327;
			caixa = rifa - chao(rifa);
			carta = chao(caixa*10 - 1);
			pontos_banca = pontos_banca + carta;
			}
			
			else 
				banca = FALSE;

		}

		if (pontos_apostador > pontos_banca)
			derrotas = derrotas + 1;
		
		pontos_apostador = 0;
		pontos_banca = 0;


	}

	estrelas = chao(100*(derrotas/N + 0.5);
	printf ("\n%d %d", teto, derrotas);
	for (e = 0; e < estrelas; e++){
		printf ("*");
	}
	derrotas = 0;
	apostador = TRUE;
	banca = TRUE;
 
}
return 0;
}






/*         funcoes            */

double NovaCaixa (double novacaixa){



return novacaixa
}


double RaizCubica (double x){

	double rn_anterior;
	int n;

	rn_anterior = 0;
	n = 0;
	rn = x;

	while (rn - rn_anterior > 0.000000001){
	
		rn = (2/3)*rn_aterior + x/(3*rn_aterior*rn_anterior);
	
	}

return rn;

}

double chao (){

	

}


double semente (int original){

double num;
int divisor;
	
num = original;

while (orignal % divisor != original){
				
	divisor = divisor * 10;

}

num = original/divisor;
return num;

}
