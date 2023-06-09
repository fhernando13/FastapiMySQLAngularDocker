import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  createFormGroup() {
    return new FormGroup({
      email: new FormControl('', [
        Validators.required
      ]),
      password: new FormControl('', [
        Validators.required
      ]),
    });
  }

  loginForm: FormGroup | any;

  constructor(private loginService: LoginService, 
              private router: Router) {
  this.loginForm = this.createFormGroup();
  }

  get email() {
    return this.loginForm.get('email');
  }

  get password() {
    return this.loginForm.get('password');
  }

  ngOnInit(): void {
      console.log("hello")
  }

  logIn() 
  {    
    if(this.loginForm != null){
      this.loginService.login(this.loginForm.value).subscribe({
        next: res => this.loginForm.value = console.log("logeado"),
        error: (err) => console.log(err)
      })
    }    
    return console.log("hello"); 
    }//back to home
    


}
