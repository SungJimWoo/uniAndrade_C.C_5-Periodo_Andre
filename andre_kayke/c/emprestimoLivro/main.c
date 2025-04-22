#ifndef MAIN_H
#define MAIN_H

/*
** Kayky Risalda Alves da Silva
** André Henrique Fiatkoski Lustosa
*/

#include "stdlib.h"
#include "functions.h"
#include "string.h"

void waitForKeyPress() {
    printf("\nPressione qualquer tecla para voltar ao menu...\n");
    getchar();  // Espera a entrada de uma tecla
}

int main() {
    Book library[MAX_BOOKS];
    User users[MAX_USERS];
    int userCount = 0;
    int loggedInUser;
    char inputName[100];

    initializeBooks(library, MAX_BOOKS);
    initializeUsers(users, &userCount);

    system("clear");
    printf("Digite seu nome: ");
    fgets(inputName, sizeof(inputName), stdin);
    inputName[strcspn(inputName, "\n")] = '\0';

    int created = createdUser(users, userCount, inputName);
    if (created == -1) {
        loggedInUser = addUser(users, &userCount, inputName);
        system("clear");
        printf("Bem Vindo, %s! Seu ID é %d\n", users[loggedInUser].name, users[loggedInUser].id);
    }

    int option, bookId;

    do {
        // Menu principal
        system("clear");
        printf("\n=== SISTEMA DE EMPRÉSTIMO DE LIVROS ===\n");
        printf("1. Listar todos os livros\n");
        printf("2. Pegue um livro emprestado\n");
        printf("3. Devolva um livro\n");
        printf("4. Mostrar relatório da biblioteca\n");
        printf("5. Mostrar meus livros emprestados\n");
        printf("0. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &option);
        getchar();  // Limpa o buffer após scanf
        system("clear");

        switch (option) {
            case 1:
                system("clear");
                listBooks(library, MAX_BOOKS);
                waitForKeyPress();  // Espera o usuário pressionar uma tecla
                break;
            case 2:
                system("clear");
                printf("Digite o ID do livro para emprestar (1 a %d): ", MAX_BOOKS);
                scanf("%d", &bookId);
                getchar();  // Limpa o buffer
                bookId--;
                if (bookId >= 0 && bookId < MAX_BOOKS) {
                    borrowBook(&library[bookId], loggedInUser);
                } else {
                    printf("ID do livro inválido.\n");
                }
                waitForKeyPress();  // Espera o usuário pressionar uma tecla
                break;
            case 3:
                system("clear");
                printf("Digite o ID do livro para retornar (1 a %d): ", MAX_BOOKS);
                scanf("%d", &bookId);
                getchar();  // Limpa o buffer
                bookId--;
                if (bookId >= 0 && bookId < MAX_BOOKS) {
                    returnBook(&library[bookId], loggedInUser);
                } else {
                    printf("ID do livro inválido.\n");
                }
                waitForKeyPress();  // Espera o usuário pressionar uma tecla
                break;
            case 4:
                system("clear");
                showLibraryReport(library, MAX_BOOKS);
                waitForKeyPress();  // Espera o usuário pressionar uma tecla
                break;
            case 5:
                system("clear");
                showUserBooks(library, MAX_BOOKS, &users[loggedInUser]);
                waitForKeyPress();  // Espera o usuário pressionar uma tecla
                break;
            case 0:
                printf("Saindo do programa...\n");
                system("clear");
                break;
            default:
                printf("Opção inválida.\n");
                waitForKeyPress();  // Espera o usuário pressionar uma tecla
        }

    } while (option != 0);

    return 0;
}
#endif