#include <stdio.h>
#include <string.h>
#include <cmath>

#define INPUT_FILE_NAME "learning_data.txt"
//#define INPUT_FILE_NAME "test_data.txt"
#define OUTPUT_FILE_NAME "accuracy.txt"
#define ARRAY_SIZE 50000

void calculate();

FILE* in_fp, *out_fp;

int main(){

	in_fp = fopen(INPUT_FILE_NAME, "r+");
	out_fp = fopen(OUTPUT_FILE_NAME, "w+");

	calculate();

	return 0;
}

void calculate(){

	float temperature[ARRAY_SIZE] = {0}, dewPoint[ARRAY_SIZE] = {0}, precipitation[ARRAY_SIZE] = {0}, windDirection[ARRAY_SIZE] = {0}, windSpeed[ARRAY_SIZE] = {0}, seaPressure[ARRAY_SIZE] = {0}, vaporPressure[ARRAY_SIZE] = {0}, humidity[ARRAY_SIZE] = {0}, cloudiness[ARRAY_SIZE] = {0}, solarRadiation[ARRAY_SIZE] = {0}, sunshine[ARRAY_SIZE] = {0}, expectedPrecipitation[ARRAY_SIZE] = {0};  
	int i = 0;
	float accuracy[ARRAY_SIZE] = {0};

	while(!file.eof()){
		fscanf(in_fp, "%f %f %f %f %f %f %f %f %f %f %f %f", &temperature[i], &dewPoint[i], &precipitation[i], &windDirection[i], &windSpeed[i], &seaPressure[i], &vaporPressure[i], &humidity[i], &cloudiness[i], &solarRadiation[i], &sunshine[i], &expectedPrecipitation[i]);
	
		printf("%f\n", temperature[i]);
	
		if(i > 0){
			if(precipitation[i] == 0){
				accuracy[i-1] = fabs(precipitation[i]-expectedPrecipitation[i-1])/(precipitation[i]+1);
				accuracy[i-1] = 1-accuracy[i-1];
			}
			
			else{
				accuracy[i-1] = fabs(precipitation[i]-expectedPrecipitation[i-1])/precipitation[i];
				accuracy[i-1] = 1-accuracy[i-1];
			}
			
			fprintf(out_fp, "%f\n", accuracy[i-1]);
		}
		i++;		
	}
}
