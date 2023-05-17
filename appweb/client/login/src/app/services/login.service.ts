import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from '../models/user';
import { environment } from 'src/environments/environment.prod';;

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  API_URI = environment.localHost;

  constructor(private http: HttpClient) 
  { 

  }

  login(user: User){
    return this.http.get(this.API_URI+'login');
  }
  
}
