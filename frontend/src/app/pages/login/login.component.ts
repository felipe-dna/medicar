import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {ApiService} from '../../shared/service/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public hidePassword = true;
  public login = {
    email: '',
    password: ''
  };
  public loginFormStateControl = {
    email: null,
    password: null,
    non_field_errors: null
  };

  constructor(
    public apiService: ApiService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  async submitForm(event): Promise<void> {
    event.preventDefault();
    await this.authenticateUser(this.login);
  }

  async setUserData(): Promise<void> {
    this.apiService.getUserData().toPromise().then(data => {
      window.localStorage.setItem('userId', data[0].id);
      window.localStorage.setItem('userName', data[0].name);
    }).then(() => this.router.navigate(['']));
  }

  async authenticateUser(credentials): Promise<void> {
    this.apiService.authenticateUser(credentials).subscribe(
      async data => {
        window.localStorage.setItem('token', data.token);
        await this.setUserData();
      },
      error => {
        this.loginFormStateControl = {...error.error};
      }
    );
  }
}
