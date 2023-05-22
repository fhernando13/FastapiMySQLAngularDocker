import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Login } from '../models/login';
import { environment } from 'src/environments/environment.prod';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  API_URI = environment.localHost;

  constructor(private http: HttpClient) {}

  login(logged: Login): Observable<any>{
    return this.http.post(this.API_URI+'login', logged);
  }

  logout(): void{
    
  }
  
}
