// Encryption and decryption by RC4 algorithm
// Author: jason71319jason
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 256

void swap(unsigned char *a, unsigned char *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int KSA(char* key, unsigned char *S) {
    int len = strlen(key);
    int j = 0;

    for(int i=0; i<N; i++) {
        S[i] = i;
    }

    for(int i=0; i<N; i++) {
        j = (j + S[i] + key[i%len]) % N;
        swap(&S[i], &S[j]);
    }

    return 0;
}

int PRGA(unsigned char *S, char *plaintext, unsigned char *ciphertext) {

    int i = 0, j = 0;

    for(size_t n = 0, len = strlen(plaintext); n < len; n++) {
        i = (i+1) % N;
        j = (j+S[i]) % N;
        swap(&S[i], &S[j]);
        int rnd = S[(S[i] + S[j]) % N];

        ciphertext[n] = rnd ^ plaintext[n];
    }

    return 0;
}

int RC4(char *key, char *plaintext, unsigned char *ciphertext) {

    unsigned char S[N];
    KSA(key, S);

    PRGA(S, plaintext, ciphertext);
    
    return 0;
}

int main(int argc, char *argv[]) {

    char key[] = "FizzBuzz";
    char *secret = "C6C62A087299478DE48625F2CE0BCB89C8E3B6B5AB8FB0E0D694471654455F595EBF7D3BC4BD928FC28F4A23B1E3FF5E1CD749C56CB51A287E1B27DCC255A6CC041DA3BE35047CD710F0FED39687346816386ADC35429E1A168663DC0FF2C4D411EF8772EA4129A2E778D0163D0DFBC4D204FD38307817DEE802C3DF7A88A9041295B8A689F862498673AD15387488C727AE455B43C69D739D0FB304293D082B3DBC57AA5E97CB5121C40C432DD25B49B4755C7EEF830E1B29CC74F10F425A6F24A1088D47CE246BBCC02FB32935E883930FD370F6F8B4DADC793B1F4B69D3A92F0DEF2FB5A0F8A66421BDACEA5831FD079D87945E114828EDEE55ADEB3FB98B76BD284202A887A5B2D13F62612187B916990FF640C74E2C26346A3EB671C04B4746E4F113C81A200B7730E738B173D8870B37E8A1BAEE5B50119CFA12258E720C492280A941147B8D51AA761D4F14EA27CFDF9946B37C67170F084B560F03BB68EF385106A12732B2D94C19C9E1B49F490BF5E80D254E86C6BF9BCC6A683F2258EB033CAA059BFF5490C1EF3449B23C79BE3606D07E6EA4A81C0DB519\0";

    // convert
    char *converted_secret = malloc(strlen(secret));
    unsigned char *p = (unsigned char*)converted_secret;
    char* c = (char*)malloc(3);
    *(c+2) = '\0';

    for(int i=0, len=strlen(secret); i<len; i+=2) {
        *c = *(secret+i);
        *(c+1) = *(secret+i+1);
        *p = strtoul(c, NULL, 16);
        p++;
    }

    // RC4
    unsigned char *pt = malloc(strlen(secret)/2);
    RC4(key, converted_secret, pt);

    for(int i=0, len=strlen((char*)pt); i<len; i++) {
        printf("%c", pt[i]);
    }
    return 0;
}
