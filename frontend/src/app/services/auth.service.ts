import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private URL = 'http://localhost:8000';
  constructor(private http: HttpClient, private router: Router) { }

  signUpUser(user) {
    return this.http.post<any>(this.URL + '/api/1/users/', user);
  }

  signInUser(user) {
    return this.http.post<any>(this.URL + '/api/token/', user);
  }

  loggedIn() {
    return !!localStorage.getItem('token');
    //return !!localStorage.getItem('user_id');
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigate(['/signin']);
  }

  getToken() {
    //localStorage.getItem('user_id');
    return localStorage.getItem('token');
  }

}
