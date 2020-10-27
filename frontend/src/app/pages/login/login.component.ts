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

  constructor(
    public apiService: ApiService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  onSubmit(event): void {
    event.preventDefault();
    this.authenticateUser(this.login);
  }

  setUserData(): void {
    this.apiService.getUserData().toPromise().then(data => {
      window.localStorage.setItem('userId', data[0].id);
      window.localStorage.setItem('userName', data[0].name);
    }).then(() => this.router.navigate(['']));
  }

  authenticateUser(credentials): void {
    this.apiService.authenticateUser(credentials).subscribe(data => {
      window.localStorage.setItem('token', data.token);
      this.setUserData();
    },
      error => { console.log(error); }
    );
  }
}
