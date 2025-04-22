#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <stdio.h>
#include <string.h>
#include "struct.h"

void initializeBooks(Book *books, int count) {
    const char *titles[MAX_BOOKS] = {
        "O Primo Basílio", "Memórias de um Sargento de Milícias", "Perto do Coração Selvagem", "Gabriela, Cravo e Canela", "Senhora",
        "Caetés", "Cidadã de Segunda Classe", "A Moreninha", "Memórias Póstumas de Brás Cubas", "A Viuvinha"
    };

    const char *authors[MAX_BOOKS] = {
        "Machado de Assis", "Aloisio Azevedo", "Clarice Lispector", "Jorge Amado", "Jose de Alencar",
        "Graciliano Ramos", "Rachel de Queiroz", "Joaquim M. de Macedo", "Machado de Assis", "Jose de Alencar"
    };

    for (int i = 0; i < count; i++) {
        strcpy(books[i].title, titles[i]);
        strcpy(books[i].author, authors[i]);
        books[i].total_borrows = 0;
        books[i].status = DISPONIVEL;
        books[i].borrowed_by = -1;
    }
}

void initializeUsers(User *users, int *userCount) {
    *userCount = 0;
}

int createdUser(User *users, int count, const char *name) {
    for (int i = 0; i < count; i++) {
        if (strcmp(users[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}

int addUser(User *users, int *count, const char *name) {
    if (*count >= MAX_USERS) {
        printf("Limite de usuários atingido.\n");
        return -1;
    }
    strcpy(users[*count].name, name);
    users[*count].id = *count;
    (*count)++;
    return *count - 1;
}

void borrowBook(Book *book, int userId) {
    if (book->status == EMPRESTADO) {
        printf("Este livro já está emprestado.\n");
    } else if (book->total_borrows >= MAX_BORROWS) {
        printf("Limite de empréstimo atingido para este livro.\n");
    } else {
        book->status = EMPRESTADO;
        book->total_borrows++;
        book->borrowed_by = userId;
        printf("Livro emprestado com sucesso.\n");
    }
}

void returnBook(Book *book, int userId) {
    if (book->status == DISPONIVEL) {
        printf("Este livro já está disponível.\n");
    } else if (book->borrowed_by != userId) {
        printf("Você não pode devolver um livro que não foi emprestado.\n");
    } else {
        book->status = DISPONIVEL;
        book->borrowed_by = -1;
        printf("Livro devolvido com sucesso.\n");
    }
}

void printBook(const Book *book) {
    printf("Titulo: %s\n", book->title);
    printf("Autor: %s\n", book->author);
    printf("Total de empréstimos: %d\n", book->total_borrows);
    printf("Status: %s\n\n", book->status == DISPONIVEL ? "Disponível" : "Emprestado");
}

void listBooks(const Book *books, int count) {
    for (int i = 0; i < count; i++) {
        printf("=== LIVRO [%d] ===\n", i + 1);
        printBook(&books[i]);
    }
}

void showLibraryReport(const Book *books, int count) {
    int available = 0, borrowed = 0;
    for (int i = 0; i < count; i++) {
        if (books[i].status == DISPONIVEL) available++;
        else borrowed++;
    }
    printf("\n=== RELATÓRIO DA BIBLIOTECA ===\n");
    printf("Total de livros: %d\nDisponível: %d\nEmprestado: %d\n", count, available, borrowed);
}

void showUserBooks(const Book *books, int count, const User *user) {
    printf("\nLivros emprestados por %s:\n", user->name);
    int found = 0;
    for (int i = 0; i < count; i++) {
        if (books[i].borrowed_by == user->id) {
            printf(" - %s by %s\n", books[i].title, books[i].author);
            found = 1;
        }
    }
    if (!found) {
        printf("Nenhum livro emprestado no momento.\n");
    }
}
#endif