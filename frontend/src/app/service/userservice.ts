import { UserRegister } from './../interfaces/usersignup';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, signal } from '@angular/core';
import { UserLogin } from '../interfaces/userlogin';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Userservice {
  private isAuthenticated = signal(false);

  private readonly API_URL = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  isLoggedIn() {
    return this.isAuthenticated();
  }

  login(body: string, headers: HttpHeaders): Observable<UserLogin> {
    const url = `${this.API_URL}/token-login`;
    return this.http.post<UserLogin>(url, body, { headers }).pipe(
      tap({
        next: () => this.isAuthenticated.set(true),
        error: () => this.isAuthenticated.set(false),
      })
    );
  }

  register(data: UserRegister): Observable<UserRegister> {
    const url = `${this.API_URL}/create-user`;
    return this.http.post<UserRegister>(url, data);
  }
}
