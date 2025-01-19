import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

/**
 * AuthService handles authentication-related operations such as login, logout, and token management.
 */
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  // BehaviorSubject to track the login status
  private isLoggedInSubject = new BehaviorSubject<boolean>(false);
  // Observable to expose the login status
  public isLoggedIn$ = this.isLoggedInSubject.asObservable();
  
  /**
   * Constructor to initialize the AuthService.
   * @param http - HttpClient to make HTTP requests.
   */
  constructor(private http: HttpClient) {
    // Check if there's a stored token and update the login status
    const token = this.getToken();
    this.isLoggedInSubject.next(!!token);
  }

  /**
   * Logs in the user by sending a POST request to the server.
   * @param username - The username of the user.
   * @param password - The password of the user.
   * @returns An Observable of the server response.
   */
  login(username: string, password: string): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:5000/users/login', { username, password }).pipe(
      tap(response => {
        if (response && response.access_token) {
          // Store the access token in local storage
          localStorage.setItem('access_token', response.access_token);
          // Update the login status
          this.isLoggedInSubject.next(true);
        }
      })
    );
  }

  /**
   * Logs out the user by removing the token from local storage and updating the login status.
   */
  logout(): void {
    localStorage.removeItem('access_token');
    this.isLoggedInSubject.next(false);
  }

  /**
   * Retrieves the stored access token from local storage.
   * @returns The access token or null if not found.
   */
  getToken(): string | null {
    return localStorage.getItem('access_token');
  }

  /**
   * Checks if the user is logged in.
   * @returns A boolean indicating the login status.
   */
  isLoggedIn(): boolean {
    return this.isLoggedInSubject.value;
  }
}